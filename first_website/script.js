gamerScore = "1"
computerScore = 1

sumScore = gamerScore + computerScore;

alert(sumScore);

function myGame() {
  player_name = prompt("enter your name");
  alert("Hello " + player_name);
  player_guess = prompt("Let's Play Scissors, Paper, Rock");
  computer_guess = randomIntFromInterval(1, 3);

if ((player_guess == "scissors") & (computer_guess == "rock"))
  else if((player_guess == "paper") & (computer_guess == "rock"))
  else if(player_guess == "rock")



if (computer_guess == 1) {
  computer_guess = "scissors";
} else if (computer_guess == 2) {
  computer_guess = "paper";
} else if (computer_guess == 3) {
  computer_guess = "rock";
}

  if (player_guess == computer_guess) {
    document.getElementById("user_feedback").innerHTML = "Correct, you win";
  } else {
    document.getElementById("user_feedback").innerHTML =
      "Incorrect, you lose\n" + "the computer guessed " + computer_guess;
  }

  function randomIntFromInterval(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
  }
}
