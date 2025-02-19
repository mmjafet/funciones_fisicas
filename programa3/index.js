document.addEventListener('DOMContentLoader', () => {
  const formulario = document.getElementById('formulario');
  const tarea = document.getElementById('tarea');

   formulario.addEventListener('submit', (evt) => {
    evt.preventDefault();    
    const task = tareaInput.value;
  });

  
});