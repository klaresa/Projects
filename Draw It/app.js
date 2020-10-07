document.addEventListener("DOMContentLoaded", () => {

  let listOfColors = [];
  let pickedColor = null;
  let $con = document.querySelector('body');

  $con.innerHTML = `
    <h3>Draw it!</h3>
    <div id="app"></div>
    <div class="pick">
      <input class="color" type="color"/>
      <button id="saveColor">Save Color</button>
      <div id="savedColors"></div>
    </div>
    <footer>&copy; by klaresa</footer>
  `;

  let $app = document.querySelector('#app');

  for (let i = 0; i < 324; i++) {
    $app.innerHTML += `<div class="square"></div>`;
  }

  let $squares = document.querySelectorAll('.square');

  for (let square of $squares){
    square.addEventListener('click', () => {
      if (pickedColor === null) {
        createColorClass(getColor(), square)
      } else {
        createColorClass(pickedColor, square);
      }
    });
  }

  let $color = document.querySelector('.color');

  $color.addEventListener('change', () => {
    pickedColor = null;
  });

  function getColor() {
    return $color.value;
  }

  function createColorClass(color, square){
    let squareClasses = square.className.split(' '); // pega as classes cores, remove e deixa apenas square
    for (let squareClass of squareClasses){
      if (squareClass.toString() !== 'square') {
        square.classList.remove(squareClass);
      }
    }
    square.classList.add(`c${color.slice(1)}`); // adiciona a classe com o formato da cor e poe a cor no background da div
    square.style.backgroundColor = color;
  }

  let $savedColors = document.querySelector('#savedColors');
  let $saveBtn = document.querySelector('#saveColor');
  $saveBtn.addEventListener('click', loadColor);

  function loadColor(){
    let c = getColor();
    if (!listOfColors.includes(c)){
      listOfColors.push(c);
      $savedColors.innerHTML += `<div class="saved c${c.slice(1)}"></div>`;
      let $d = document.querySelector(`.saved:last-child`);
      $d.style.backgroundColor = c;

      setSavedDivListeners()
    }
  }

  function setSavedDivListeners() {
    let savedColorDivs = document.querySelectorAll('.saved');

    for (let savedColor of savedColorDivs) {
      savedColor.addEventListener('click', () => {
        pickedColor = returnSavedColor(savedColor);
      }, true)
    }
  }

  function returnSavedColor(div) {
    return div.className.split(' ')[1].replace('c', '#');
  }

});
