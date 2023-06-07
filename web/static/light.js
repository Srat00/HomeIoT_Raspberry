function getLightSensorData() {
  // 여기서 라즈베리 파이로부터 조도 센서 데이터를 가져옵니다.
  // 실제 코드에서는 fetch 함수나 다른 방법을 사용해야 합니다.
  // 이 예제에서는 임의의 데이터를 반환합니다.
  return new Promise((resolve) => {

   var brightnessValue = parseFloat(document.getElementById("brightnessValue").innerText);
//   값 받아오는 부분
    setTimeout(() => {
        resolve(brightnessValue);
//      resolve(Math.floor(Math.random() * 1000)); // 0-1000 사이의 랜덤한 숫자를 반환
    }, 1000);
  });
}





document.addEventListener("DOMContentLoaded", () => {
  const lightLevelElement = document.getElementById("light-level");
  const alertLightElement = document.getElementById("alert-light");

  function updateLightStatus() {
    getLightSensorData().then((lightLevel) => {
      lightLevelElement.textContent = `명도 레벨: ${lightLevel}`;
      if (lightLevel <= 800) {
        alertLightElement.textContent = '현재 상태: 밝음';
        alertLightElement.style.color = 'white';
      } else {
        alertLightElement.textContent = '현재 상태: 어두움';
        alertLightElement.style.color = 'black';
      }
      setTimeout(updateLightStatus, 1000);
    });
  }

  updateLightStatus();
});
