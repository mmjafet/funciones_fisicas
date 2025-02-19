var con = 1;
var data = [];
document.addEventListener('DOMContentLoader', () => {
  const formulario = document.getElementById('formulario');
  const tarea = document.getElementById('tarea');

   formulario.addEventListener('submit', (evt) => {
    evt.preventDefault();    
    const task = tareaInput.value.trim();

    const  newTask = {
        idCount: con++,
        task: task,
        description : description,
        status: false,
        }

    data.push(newTask);
  });

  
});