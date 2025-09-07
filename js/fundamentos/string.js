let nome = "Momed";
let numero = 3;

console.log(typeof(nome));
console.log(typeof(numero));
console.log(nome.charAt(0));
console.log(nome.charCodeAt(3));
console.log(nome.indexOf('d'));
console.log(nome.indexOf('M'));//Retorna o indice associado ao digito no caso M
console.log(nome.substring(0, 3))

console.log('Nome: '.concat(nome).concat("!"))
console.log(nome.replace('e', '3'))

console.log('Momed, Abdala, Ossufo'.split(','))