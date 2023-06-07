function getNoiseSensorData() {
            // Django에서 받아온 값을 가져와서 반환하는 비동기 함수 구현
            return new Promise((resolve) => {
                // Django에서 받아온 값
                var dataValue = parseFloat(document.getElementById("decibelValue").innerText);

                // 1초마다 Django에서 받아온 값 반환
                setInterval(() => {
                    resolve(dataValue);
                }, 1000);
            });
        }
        실제 장고에서 받아오는 값

//function getNoiseSensorData() {
//    // 이 부분은 실제 소음 센서 데이터를 받아오는 코드로 수정해야 합니다.
//    return new Promise((resolve) => {
//        setTimeout(() => {
//            resolve(Math.floor(Math.random() * 100)); // 0 ~ 99 사이의 임의의 수를 반환
//        }, 1000);
//    });
//}
//위에 부분 랜덤으로 값받아오는 코드



document.addEventListener("DOMContentLoaded", () => {
    const noiseLevelElement = document.getElementById("noise-level");
    const alertElement2 = document.getElementById("alert2");
    const alertElement3 = document.getElementById("alert3");
    const alertElement1 = document.getElementById("alert1");
    function updateNoiseLevel() {
        getNoiseSensorData().then((noiseLevel) => {
            noiseLevelElement.textContent = "소음 레벨: " + noiseLevel;
            alertElement3.style.display = noiseLevel > 65 ? "block" : "none"; // 소음 레벨이 70 이상이면 경고 메시지를 표시
            alertElement2.style.display = noiseLevel > 35 && noiseLevel <= 65 ? "block" : "none";
            alertElement1.style.display = noiseLevel >=0 && noiseLevel <= 35 ? "block" : "none";
            setTimeout(updateNoiseLevel, 1000);
        });
    }

    updateNoiseLevel();
});
//
//document.addEventListener("DOMContentLoaded", () => {
//    const noiseLevelElement = document.getElementById("noise-level");
//    const alertElement = document.getElementById("alert2");
//
//    function updateNoiseLevel() {
//        getNoiseSensorData().then((noiseLevel) => {
//            noiseLevelElement.textContent = "소음 레벨: " + noiseLevel;
//
//            // 소음 레벨에 따라 스타일과 메시지 설정
//            if (noiseLevel < 35) {
//                alertElement.style.backgroundColor = "blue";
//                alertElement.style.color = "black";
//                alertElement.textContent = "정상입니다.";
//            } else if (noiseLevel < 65) {
//                alertElement.style.backgroundColor = "yellow";
//                alertElement.style.color = "black";
//                alertElement.textContent = "주의합니다.";
//            } else {
//                alertElement.style.backgroundColor = "red";
//                alertElement.style.color = "black";
//                alertElement.textContent = "심각합니다.";
//            }
//
//            setTimeout(updateNoiseLevel, 1000);
//        });
//    }
//
//    updateNoiseLevel();
//});
