const formulario = document.getElementById('calculadora')

const eventoFormulario = (evt)=>{
    evt.preventDefault()}

formulario.addEventListener('submit', eventoFormulario)

const calcular = ()=>{
    let num1 = document.getElementById('num1').value
    let num2 = document.getElementById('num2').value

    suma = (num1) + parseInt(num2)

    alert(`La suma de los numeros es: ${suma}`)
    
}
