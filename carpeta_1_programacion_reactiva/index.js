// Esperar a que el DOM esté completamente cargado antes de ejecutar el código
document.addEventListener("DOMContentLoaded", () => {
    // Obtener el formulario por su ID
    const formulario = document.getElementById("calculadora");
    // Obtener el elemento de resultado por su ID
    //const txtResult = document.getElementById("result");

    // Definir la función que se ejecutará cuando se envíe el formulario
    const eventoFormulario = evt => {
        // Prevenir el comportamiento por defecto del formulario (recargar la página)
        evt.preventDefault();
        
        // Crear un objeto FormData con los datos del formulario
        const data = new FormData(evt.target);
        // Obtener los valores de los campos del formulario
        //definir que son numeros con float o int parseando 
        //parse float o parse int
        const num1 = parseFloat(data.get("numero1"));
        const num2 = parseFloat(data.get("numero2"));

        // Sumar los valores obtenidos
        let result = +num1 + +num2;
        // Mostrar el resultado en la consola
        console.log(`num1: ${num1}, result: ${result}, num2: ${num2}`);
        // Mostrar el resultado en el elemento de resultado
       // alert(`La suma de ${num1} + ${num2} es: ${result}`);
        //Swal.fire(`La suma de ${num1} + ${num2} es: ${result}`);
        Swal.fire({
            title: "suma ",
            text:  `La suma de ${num1} + ${num2} es: ${result}`,
            icon: "warning",
            timer:3000,
            showConfirmButton: false
          });
    };
    

    // Añadir el evento de envío al formulario
    formulario.addEventListener("submit", eventoFormulario);
});