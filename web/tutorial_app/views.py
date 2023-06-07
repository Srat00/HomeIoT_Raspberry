from django.shortcuts import render, HttpResponse
# from .data_fetcher import get_decibel_data
from pymongo import MongoClient


import os


# def execute_function(request):
#     # 실행할 함수 내용 작성
#     # 여기서는 단순히 콘솔에 로그를 출력하는 예시를 작성했습니다.
#     # MongoDB에 연결
#     client = MongoClient('mongodb+srv://pi:pi@cluster0.z4b5des.mongodb.net/?retryWrites=true&w=majority')
#
#     # 데이터베이스와 컬렉션 선택
#     db = client['mydatabase']
#     collection = db['myactuator']
#
#     collection.update_one({}, {"$set": {"Trigger": 1}})
#
#     return HttpResponse("Django function executed")
#

# def execute_function1(request):
#     # 실행할 함수 내용 작성
#     # 여기서는 단순히 콘솔에 로그를 출력하는 예시를 작성했습니다.
#     # MongoDB에 연결
#     client = MongoClient('mongodb+srv://pi:pi@cluster0.z4b5des.mongodb.net/?retryWrites=true&w=majority')
#
#     # 데이터베이스와 컬렉션 선택
#     db = client['mydatabase']
#     collection = db['myactuator']
#
#     collection.update_one({}, {"$set": {"buzzer": 1}})
#
#     return HttpResponse("Django function executed1")
#


# Create your views here.
client = MongoClient('mongodb+srv://pi:pi@cluster0.z4b5des.mongodb.net/?retryWrites=true&w=majority')
db = client['mydatabase']
collection = db['sensor_data']
actuator = db['myactuator']


def execute_function(request):
    # 실행할 함수 내용 작성
    # 여기서는 단순히 콘솔에 로그를 출력하는 예시를 작성했습니다.
    # MongoDB에 연결
    list = get_actuator_status()
    if list[3] == 0:
        actuator.update_one({}, {"$set": {"Trigger": 1}})
    if list[3] == 1:
        actuator.update_one({}, {"$set": {"Trigger": 0}})

    return HttpResponse("Django function executed")


def execute_function1(request):
    # 실행할 함수 내용 작성
    # 여기서는 단순히 콘솔에 로그를 출력하는 예시를 작성했습니다.
    # MongoDB에 연결
    list = get_actuator_status()
    if list[0] == 0:
        actuator.update_one({}, {"$set": {"buzzer": 1}})
    if list[0] == 1:
        actuator.update_one({}, {"$set": {"buzzer": 0}})

    return HttpResponse("Django function executed1")


# 팬 작동 함수
def execute_function2(request):
    list = get_actuator_status()
    if list[1] == 0:
        actuator.update_one({}, {"$set": {"fan": 1}})
    if list[1] == 1:
        actuator.update_one({}, {"$set": {"fan": 0}})

    return HttpResponse("Django function executed2")


# LED 작동 함수
def execute_function3(request):
    list = get_actuator_status()
    if list[2] == 0:
        actuator.update_one({}, {"$set": {"LED": 1}})
    if list[2] == 1:
        actuator.update_one({}, {"$set": {"LED": 0}})

    return HttpResponse("Django function executed3")


def get_actuator_status():
    data = actuator.find_one({})
    # [0,1,0]이런식으로 데이타를 읽어옴
    # status_list[0] : buzzer값
    # status_list[1] : fan값
    # status_list[2] : LED값
    # status_list[3] : Trigger값
    status_list = [data['buzzer'], data['fan'], data['LED'], data['Trigger']]
    return status_list





# def connect_to_mongodb():
#     client = MongoClient('mongodb+srv://pi:pi@cluster0.z4b5des.mongodb.net/?retryWrites=true&w=majority')
#     db = client['mydatabase']
#     collection = db['sensor_data']
#     return collection

# 가장 마지막으로 삽입된 데이터 조회 함수
def get_last_data():
    # collection = connect_to_mongodb()
    data = collection.find_one({}, sort=[('$natural', -1)])
    return data

# 온도 조회 함수
def get_temperature():
    data = get_last_data()
    return data['temperature'] if data else None

# 습도 조회 함수
def get_humidity():
    data = get_last_data()
    return data['humidity'] if data else None

# 가스 누출 감지 여부 조회 함수
def get_gas_leak_detected():
    data = get_last_data()
    return data['gas_leak_detected'] if data else None

# 데시벨 조회 함수
def get_decibel():
    data = get_last_data()
    return data['decibel'] if data else None

# 초음파 거리 조회 함수
def get_ultrasonic_distance():
    data = get_last_data()
    return data['Unusual'] if data else None

# 조도 조회 함수
def get_brightness():
    data = get_last_data()
    return data['brightness'] if data else None



def index(request):
    # 몽고디비에서 데이터 가져오기

    ultrasonic = int(get_ultrasonic_distance())
    Unusual = int(get_ultrasonic_distance())

    brightness = get_brightness()
    humidity = get_humidity()
    decibel = get_decibel()
    temperature = get_temperature()
    gas = get_gas_leak_detected()

    # 데이터를 템플릿에 전달하여 렌더링
    return render(request, 'tutorial_app/index.html', {
        'Unusual' : Unusual,
        'ultrasonic': ultrasonic,
        'brightness': brightness,
        'gas' : gas,
        'humidity' : humidity,
        'decibel' : decibel,
        'temperature' : temperature,



    })

# def index(request):
#     return render(request, 'tutorial_app/index.html')

def test(request):
    return render(request, 'tutorial_app/test.html')

def rsp(request):
    return render(request, 'tutorial_app/rsp.html')

def test3(request):
    return render(request, 'tutorial_app/test3.html')

def test2(request):
    return render(request, 'tutorial_app/test2.html')

def middle(request):
    return render(request, 'tutorial_app/middle.html')

def game(request):
    return render(request, 'tutorial_app/game.html')

def ib(request):
    return render(request, 'tutorial_app/ib.html')

def alice(request):
    return render(request, 'tutorial_app/alice.html')

def ow(request):
    return render(request, 'tutorial_app/ow.html')

def sling(request):
    return render(request, 'tutorial_app/sling.html')


def dino(request):
    return render(request, 'tutorial_app/dino.html')

