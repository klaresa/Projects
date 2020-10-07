
let userName = document.querySelector('input[name="user"]');
let $btn = document.querySelector('button');

let $myUL = document.createElement('ul');
$myUL.setAttribute('id', 'myRepos');
let $container = document.querySelector('.container');
$container.appendChild($myUL);

var data = [];
var user = '';

$btn.onclick = query;

function query() {
        let userText = userName.value;
        user = userText;

        if (user){
        userName.value = '';
        userName.focus();

        myPromise().then(function (response) {
            var res = response;
            for (item of res){
                data.push(item.name);
            }
            renderItems();
        }).catch(function (error) {
            console.warn(error)
        });
    } else {
        alert("Entre com um usuario!")
    }

}

function renderItems(){
    deteleItems();

    for (item of data){
        let repoElement = document.createElement('li');
        repoElement.setAttribute('id', item);
        repoElement.setAttribute('item', 'added');
        let repoName = document.createTextNode(item);
        repoElement.appendChild(repoName);
        $myUL.appendChild(repoElement);
    }

    data = [];
}

function deteleItems() {
    let deleteRepos = document.querySelectorAll('[item="added"]');

    if (deleteRepos.length > 0){
        for (repo of deleteRepos) {
            repo.remove()
        }
    }
}

function myPromise() {
    return new Promise(function (resolve, reject) {
        var request = new XMLHttpRequest();

        request.open('GET', `https://api.github.com/users/${user}/repos`);
        request.send(null);

        request.onreadystatechange = function () {
            if (request.readyState === 4){
                if (request.status === 200 ){
                    resolve(JSON.parse(request.responseText));
                } else {
                    erro();
                    reject(request.message);
                }
            }
        }
    });
}

// there are other errors tho
function erro(){
  deteleItems();
    let erro = document.createElement('li');
    erro.setAttribute('item', 'added');
    erro.appendChild(document.createTextNode("User not found"));
    $myUL.appendChild(erro);
}



