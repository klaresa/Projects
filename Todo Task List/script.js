
// my central app id
var app = document.querySelector('#app');

// creating my form cuz i want to hide that submit button
let formElement = document.createElement('form');
app.appendChild(formElement);

// creating input
var input = document.createElement('input');
input.setAttribute('type', 'text');
input.setAttribute('placeholder', 'Add..');
formElement.appendChild(input);

// creating submit button
let btnSubmit = document.createElement('button');
btnSubmit.setAttribute('type', 'submit');
btnSubmit.setAttribute('hidden', 'hidden');
btnSubmit.setAttribute('onsubmit', 'addTodo()');
formElement.appendChild(btnSubmit);

// creating an UL element
var ulElement = document.createElement('ul');
ulElement.setAttribute('id', 'listTodos');
app.appendChild(ulElement);

// selects DOM elements
// it is important to note that only listTodos is an ID
var listElement = document.querySelector('#listTodos');
var inputElement = document.querySelector('#app input');
var btnElement = document.querySelector('#app button');

// my array out of localStorage or an empty array
var todos = JSON.parse(localStorage.getItem('list_todos')) || [];


// rendering my little list
function renderTodos() {

    // every time it renders my list it resets before moving on
    listElement.innerHTML = '';

    // for each item of my list
    for (var todo of todos){

        // it creates an li with my to-do text
        var todoElement = document.createElement('li');
        var todoText = document.createTextNode(todo);
        todoElement.appendChild(todoText);

        // it creates an link and adds an value to make clicking more visible
        let linkElement = document.createElement('a');
        linkElement.setAttribute('href', "#");

        // it creates a text and adds it to the link
        let linkText = document.createTextNode('delete');
        linkElement.appendChild(linkText);
        todoElement.appendChild(linkElement);

        // it creates an index and adds an attribute *avec le* position for each to-do
        let pos = todos.indexOf(todo);
        linkElement.setAttribute('onclick', 'deleteTodo(' + pos +')');

        // it adds the final li product as an uls child
        ulElement.appendChild(todoElement);
    }
}
renderTodos();

btnElement.onclick = addTodo;

// it just creates a new to-do
function addTodo() {
    var todoText = inputElement.value;
    todos.push(todoText);
    inputElement.value = '';
    renderTodos();
    saveToStorage()
}

// it deletes that unwanted to-do
function deleteTodo(pos) {
    todos.splice(pos, 1);
    renderTodos();
    saveToStorage()
}

// it saves our list to localStorage. DONT forget to stringify it! :)
function saveToStorage() {
    localStorage.setItem('list_todos', JSON.stringify(todos));
}