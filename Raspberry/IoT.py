import RPi.GPIO as GPIO
import Adafruit_DHT
import spidev
import sys
import time
import datetime
from pymongo import MongoClient

# Connect MongoDB
client = MongoClient('mongodb+srv://pi:pi@cluster0.z4b5des.mongodb.net/?retryWrites=true&w=majority')

# Database & Collection
db = client['mydatabase']
collection = db['sensor_data']
actuator = db['myactuator']

# GPIO Setting
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# ADC Setting
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000 # 1MHz

def analogread(channel):
    r = spi.xfer2([1, (0x08 + channel) << 4, 0])
    adc_out = ((r[1] & 0x03) << 8) + r[2]
    return adc_out

# GPIO Pin
# Actuator
FAN = 5 #wiringPi 21
LED = 6 #wiringPi 22
BUZZER = 19 #wiringPi 23

# Sensor

TEMP = 24  #wiringPi 5
ULTRA_T = 18 #wiringPi 1
ULTRA_E = 21 #wiringPi 29

# ADC
LIGHT = 0 #ADC 0
MIC = 1 #ADC 1
GAS = 2 #ADC 2
    
#GPIO Setup
GPIO.setup(FAN, GPIO.OUT)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)

GPIO.setup(GAS, GPIO.IN)
GPIO.setup(TEMP, GPIO.IN)

GPIO.setup(ULTRA_T, GPIO.OUT)
GPIO.setup(ULTRA_E, GPIO.IN)

# Actuator
def fan(status):
    if status == True:
        GPIO.output(FAN, GPIO.HIGH)
    if status == False:
        GPIO.output(FAN, GPIO.LOW)

def led(status):
    if status == True:
        GPIO.output(LED, GPIO.HIGH)
    if status == False:
        GPIO.output(LED, GPIO.LOW)
        

def buzzer(status):
    if status == True:
        GPIO.output(BUZZER, GPIO.HIGH)
    if status == False:
        GPIO.output(BUZZER, GPIO.LOW)
        
# 액추에이터 상태 조회 함수, DB에서 값을 읽어옴
def get_actuator_status():
    data = actuator.find_one({})  
    #[0,1,0,1]이런식으로 데이타를 읽어옴
    #status_list[0] : buzzer값
    #status_list[1] : fan값
    #status_list[2] : LED값
    #status_list[3] : 수동/자동 트리거
    status_list = [data['buzzer'], data['fan'], data['LED'], data['Trigger']]
    return status_list

# Gas
def gas():
    gas_value = analogread(GAS)
    if get_actuator_status()[3] == 0:
        print(gas_value)
        # 누출 기준 300
        if gas_value > 300:
            fan(True)
            return 1
        elif gas_value < 300:
            fan(False)
            return 0
    return gas_value
    
# Temperature & Humidity
def temp():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, TEMP)
    return temperature, humidity

# Light
def light():
    light_value = analogread(LIGHT)
    # 액추에이터 제어
    # 평균 = 218, 어두움 800
    if get_actuator_status()[3] == 0:
        if light_value > 800:
            led(True)
        elif light_value < 800:
            led(False)

    return light_value


# Ultrasound
def ultra():
    GPIO.output(ULTRA_T, False)
    time.sleep(0.5)
    GPIO.output(ULTRA_T, True)
    time.sleep(0.00001)
    GPIO.output(ULTRA_T, False)

    while GPIO.input(ULTRA_E) == 0:
        pulse_start = time.time()

    while GPIO.input(ULTRA_E) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = (pulse_duration * 34300) / 2

    if get_actuator_status()[3] == 0:
        # 액추에이터 제어
        if distance < 15:
            buzzer(True)
        elif distance > 15:
            buzzer(False)

    return distance 

# Microphone
def mic():
    mic_value = analogread(MIC)
    # 기준값 520
    # 측정값 - 520의 절대값이 40이 넘어가면 소음으로 간주
    return abs(mic_value - 520)

# Main
if __name__ == "__main__":
    print("HomeIoT Running...")

    try:
        while True:
            # 1 Sec Refresh
            # Actuator 0 = Auto 1 = Manual
            if get_actuator_status()[3] == 1:
                # Actuator
                buzzer(get_actuator_status()[0])
                fan(get_actuator_status()[1])
                led(get_actuator_status()[2])

            # Ultrasound
            ultra_distance = ultra()
            # Light
            light_value = light()
            # Microphone
            mic_value = mic()
            # Temperature & Humidity
            temperature, humidity = temp()
            # Gas
            gas_value = gas()
                
            data = {
                "Unusual":  ultra_distance,
                "temperature": temperature,
                "humidity": humidity,
                "brightness": light_value,
                "decibel": mic_value,
                "gas_leak_detected": gas_value
            }
            # DB Insertion
            collection.insert_one(data)
            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()

    finally:
        GPIO.cleanup()
        sys.exit()
