function getGasSensorData() {
    // 이 부분은 실제 가스 센서 데이터를 받아오는 코드로 수정해야 합니다.
    return new Promise((resolve) => {
     var gasValue = parseFloat(document.getElementById("gasValue").innerText);
        setTimeout(() => {
            resolve(gasValue);
//            resolve(Math.floor(Math.random() * 1000)); // 0 ~ 999 사이의 임의의 수를 반환
        }, 1000);
    });
}

document.addEventListener("DOMContentLoaded", () => {
    const gasLevelElement = document.getElementById("gas-level");
    const alertElement = document.getElementById("alert");

    function updateGasLevel() {
        getGasSensorData().then((gasLevel) => {
            gasLevelElement.textContent = "가스 레벨: " + gasLevel;
            alertElement.style.display = gasLevel > 0 ? "block" : "none"; // 가스 레벨이 500 이상이면 경고 메시지를 표시
            setTimeout(updateGasLevel, 1000);
        });
    }

    updateGasLevel();
});
