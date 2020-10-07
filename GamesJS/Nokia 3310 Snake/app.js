document.addEventListener('DOMContentLoaded', () => {
  const squares = document.querySelectorAll('.grid div');
  const scoreDisplay = document.querySelector('span');
  const startBtn = document.querySelector('.start');

  const width = 10;
  let appleIndex = 0;
  let currentSnake = [2, 1, 0]; // size of the snake
  let direction = 1;
  let score = 0;
  let speed = 0.9;
  let intervalTime = 0;
  let interval = 0;

  function startGame() {
    currentSnake.forEach(index => squares[index].classList.remove('snake'));
    squares[appleIndex].classList.remove('apple');
    clearInterval(interval);
    score = 0;
    randomApple();
    direction = 1;
    scoreDisplay.innerHTML = score;
    intervalTime = 1000;
    currentSnake = [2, 1, 0];
    currentSnake.forEach(index => squares[index].classList.add('snake'));
    interval = setInterval(moveOutcomes, intervalTime);
  }

  // resultados
  function moveOutcomes() {
    if (
        (currentSnake[0] + width >= (width * width) && direction === width) || // if snake hits bottom
        (currentSnake[0] % width === width -1 && direction === 1) || // if it hits right wall
        (currentSnake[0] % width === 0 && direction === -1) || // if it hits left wall
        (currentSnake[0] - width < 0 && direction === -width) || // if it hits top
        squares[currentSnake[0] + direction].classList.contains('snake') // if it hits itself
    ) {
      return clearInterval(interval); // stop time
    }

    const tail = currentSnake.pop(); // discovers the last item of the array
    squares[tail].classList.remove('snake'); // removes the class snake off the tail
    currentSnake.unshift(currentSnake[0] + direction); // directs the head of the array

    // deals with the snake getting apples
    if (squares[currentSnake[0]].classList.contains('apple')) {
      squares[currentSnake[0]].classList.remove('apple');
      squares[tail].classList.add('snake');
      currentSnake.push(tail); // adds the last item to the array snake

      randomApple();
      score++;
      scoreDisplay.textContent = score;
      clearInterval(interval);
      intervalTime = intervalTime * speed;
      interval = setInterval(moveOutcomes, intervalTime);
    }

    squares[currentSnake[0]].classList.add('snake');
  }

  // creates a random apple
  function randomApple() {
    do {
      appleIndex = Math.floor(Math.random() * squares.length);

    } while (squares[appleIndex].classList.contains('snake'));
      squares[appleIndex].classList.add('apple');
  }

  function control(e) {
    // ele sempre entra aqui como 0
    // squares[currentIndex].classList.remove('snake'); // eh o que deixa o div um branco

    if (e.keyCode === 39) { // go right
      direction = 1;
    } else if (e.keyCode === 38) { // go up
      direction = -width;
    } else if (e.keyCode === 37) { // go left
      direction = -1;
    } else if (e.keyCode === 40) { // go down
      direction = +width;
    }
  }

  document.addEventListener('keyup', control);
  startBtn.addEventListener('click', startGame);
});
