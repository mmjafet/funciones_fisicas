const mensaje = document.getElementById('mensaje');
const boton = document.getElementById('btn-saludo');



const eventoSaludar = () => {
    let texto = "hola desde js con este Dom <a> manipulado </a>";
    
    mensaje.innerText += texto;
    }

boton.addEventListener('click', eventoSaludar);