complete = document.getElementsByClassName('complete')
task = document.getElementsByClassName('task')

complete.addEventListener('click', addFunction())

function addFunction(){
    task.innerHTML = "hello"
}