let addToDoButton = document.getElementById('addToDo');
let toDoContainer = document.getElementById('toDoContainer');
let inputField = document.getElementById('inputField');
let inputField1 = document.getElementById('inputField1');
let inputField2 = document.getElementById('inputField2');
let rem=0;
addToDoButton.addEventListener('click', function(){
    rem+=1;
    document.getElementById("remain").innerHTML="Remaining : "+rem;
    var paragraph = document.createElement('p');
    var paragraph1 = document.createElement('p');
    var paragraph2 = document.createElement('p');
    var div = document.createElement('div');
    var btn = document.createElement('button');
    btn.appendChild(document.createTextNode('close'));
    btn.classList.add('btn');
    div.classList.add('div-style');
    paragraph.classList.add('paragraph-styling');
    paragraph1.classList.add('paragraph1');
    paragraph2.classList.add('paragraph1');
    paragraph.innerText = "Title       : "+inputField.value;
    paragraph1.innerText ="Description : "+inputField1.value;
    paragraph2.innerText ="Deadline    : "+inputField2.value;
    div.appendChild(btn);
    div.appendChild(paragraph);
    div.appendChild(paragraph1);
    div.appendChild(paragraph2);
    toDoContainer.appendChild(div);
    inputField.value = "";
    inputField1.value = "";
    inputField2.value = "";
    paragraph.addEventListener('click', function(){
        paragraph.style.textDecoration = "line-through";
        paragraph1.style.visibility="visible";
        paragraph2.style.visibility="visible";
    })
    btn.addEventListener('click', function(){
        toDoContainer.removeChild(div);
        rem-=1;
        document.getElementById("remain").innerHTML="Remaining : "+rem;
    })
})
