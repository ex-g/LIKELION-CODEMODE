let target = document.querySelector("#dynamic");

function randomString(){
  let stringArr = [
    "come on let's go to bed, we're going rock the night away (Square, Yerin Baek)",
    "I'm only one call away, I'll be there to save the day (One call away, Charlie Puth)",
    "I can't stop loving you(장난 아닌데, Day6)",
    "꽃잎의 색은 우리 마음 가는대로 칠해 시들 때도 예쁘게 (Blueming, IU)",
    "괜시리 웃음이 나 또 생각이 나 사랑이란 게 비슷한 걸까 (Be With You, AKMU)",
    "but I've got a blank space baby, and I'll write your name (Blank space, Taylor Swift)"
  ];
let selectString = stringArr[Math.floor(Math.random() * stringArr.length)];
let selectStringArr = selectString.split("");

return selectStringArr;
}

function resetTyping(){
  target.textContent = "";
  dynamic(randomString());
}

function dynamic(randomArr){
  console.log(randomArr);
  if(randomArr.length > 0){
    target.textContent += randomArr.shift();
    setTimeout(function(){
      dynamic(randomArr);
    },80);
  }else{
    setTimeout(resetTyping, 3000);
  }
}

dynamic(randomString());

function blink(){
  target.classList.toggle("active");
}
setInterval(blink, 500)