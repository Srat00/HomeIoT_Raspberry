function getSensorData() {
  // 라즈베리 파이로부터 받아온 데이터를 리턴하는 함수를 여기에 구현하세요.
  // 예시: return fetch("라즈베리_파이_데이터_요청_URL").then(response => response.json());

  return new Promise((resolve) => {

       var ultrasonicValue = parseFloat(document.getElementById("ultrasonicValue").innerText);

    setTimeout(() => {
        resolve(ultrasonicValue);
//      resolve(Math.floor(Math.random() * 400) + 1); // 임시로 1-400 사이의 랜덤한 숫자를 리턴
    }, 1000);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  const distanceElement = document.getElementById("distance");

  function updateDistance() {
    getSensorData().then((distance) => {
      distanceElement.textContent = distance;
      setTimeout(updateDistance, 1000);
    });
  }

  updateDistance();
});
