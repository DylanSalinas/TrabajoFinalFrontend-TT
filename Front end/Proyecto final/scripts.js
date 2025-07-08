const productos = [
    {
        id: "01",
        imagen: "imagenes/botas1.png",
        nombre: "Botas Alaska",
        precio: "30,000",
    },
    {
        id: "02",
        imagen: "imagenes/botas1.png",
        nombre: "Botas Alaska",
        precio: "30,0020",
    }
];

let carrito = [];

function manejarClicComprar(evento) {
    if (evento.target.classList.contains("btn-comprar")) {
        const productoId = evento.target.dataset.id;
        agregarProductosAlCarrito(productoId);
    }
}

function agregarProductosAlCarrito(productoId) {
    const productoSeleccionado = productos.find(p => p.id === productoId);
    if (productoSeleccionado) {
        carrito.push(productoSeleccionado);
        console.log("Producto agregado:", productoSeleccionado);
        console.log("Carrito actual:", carrito);
    }
}

function agregarProductos() {
    const divProductos = document.querySelector(".galeria-productos");

    for (let i = 0; i < productos.length; i++) {
        const producto = productos[i];

        divProductos.insertAdjacentHTML("afterbegin", `
            <div class="card">
                <a href="#"><img src="${producto.imagen}" alt="${producto.nombre}" class="card"></a>
                <div class="info">
                    <h3>${producto.nombre}</h3>
                    <span>${producto.precio}</span>
                    <button class="btn-comprar" type="button" data-id="${producto.id}">Comprar</button>
                </div>
            </div>
        `);
    }

    // Delegación del evento
    divProductos.addEventListener("click", manejarClicComprar);
}

// Llamás a la función para mostrar los productos
agregarProductos();

function agregarProductosAlCarrito(idProducto) {
        let productoEnCarrito = null;
    for (let i = 0; i< carrito.length; i++){


    }
        
    if (productoEnCarrito) {
        productoEnCarrito.cantidad++;

    } else {
        let productoOriginal = null;
        for (let i = 0; i < productos.length; i++) {
            if (producots[i].id === idProducto){
                productoOriginal = productos[i];
                break;
            }
        }

        carrito.push({ ...productoOriginal, cantidad: 1});
    }
    actualizarcarrito
}
