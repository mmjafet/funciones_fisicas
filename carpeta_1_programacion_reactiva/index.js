const mensaje = document.getElementById('mensaje');
const boton = document.getElementById('boton');



const eventoSaludar = () => {
    let texto = "hola desde js con este Dom manipulado";
    mensaje.innerText = texto;
    mensaje.innerText += texto;
}