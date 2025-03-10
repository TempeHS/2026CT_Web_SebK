player_name = prompt("enter your name");
alert("Hello " + player_name);
player_guess = prompt("Let's Play Scissors, Paper, Rock");
computer_guess = randomIntFromInterval(1, 3);

scissors = 1;
paper = 2;
rock = 3;

if (player_guess == computer_guess) {
  document.getElementById("user_feedback").innerHTML = "Correct, you win";
} else {
  document.getElementById("user_feedback").innerHTML =
    "Incorrect, you lose\n" + "the computer guessed " + computer_guess;
}

function randomIntFromInterval(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}
