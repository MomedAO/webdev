//Funcao sem retorno
function imprimirSoma(a, b) {
    console.log(a + b)
}
imprimirSoma(2, 3)
imprimirSoma(2)
imprimirSoma(3, 10, 11, 2)
imprimirSoma()

//fFuncao com retorno
function soma(a, b = 1) {
    return a + b
}

console.log(soma(8, 5))
console.log(soma(2))
console.log(soma())