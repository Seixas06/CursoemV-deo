let num=[4,1,5,7,2]


console.log(num)
console.log(num.length)
num.sort()
console.log(num)
num.push(3)
console.log(num)


for (let c=0;c<num.length;c++){
    console.log(`A posição ${c} tem o valor ${num[c]}`)
}


for (let c in num ){
    console.log(num[c])
}


let c=num.indexOf(2)
if (c == -1){
    console.log('O número não foi encontrado!')
} else{
    console.log(`O valor está na posição ${c}`)
}
