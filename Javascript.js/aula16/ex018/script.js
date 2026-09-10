let numbs=[]
let res=document.getElementById('res')
let list=document.getElementById('list')
let num=document.getElementById('num')


function isNumero(n){
    if(Number(n) >=1 && Number(n) <=100){
        return true
    } else{
        return false
    }
}


function inLista(n,l){
    if (l.indexOf(Number(n)) != -1){
        return true
    } else{
        return false
    }


}
function adicionarnum(){
    if (isNumero(num.value) && !inLista(num.value,numbs)){
        numbs.push(Number(num.value))
        let item=document.createElement('option')
        item.text=`Valor ${num.value} adicionado.`
        list.appendChild(item)
        res.innerHTML=''
    } else{
        window.alert('Valor inválido ou não encontrado na lista')
        
    }
    num.value=''
    num.focus()
}


function finalizar(){
    if (numbs.length == 0){
        window.alert('Adicione valores antes de finalizar!')
    } else{
        let tot=numbs.length
        let maior=numbs[0]
        let menor=numbs[0]
        let soma=0
        let media=0
        for(let pos in numbs){
            soma+=numbs[pos]
            media=soma/tot
            if (numbs[pos] > maior)
                maior=numbs[pos]
            if (numbs[pos]<menor)
                menor=numbs[pos]
        }
        res.innerHTML=''
        res.innerHTML+=`<p>A lista tem ${tot} números cadastrados.</p>`
        res.innerHTML+=`<p>O maior número informado foi ${maior}.</p>`
        res.innerHTML+=`<p>O menor valor adicionado foi ${menor}.</p>`
        res.innerHTML+=`<p>A soma de todos os valores é ${soma}.</p>`
        res.innerHTML+=`<p>A média entre os ${tot} valores é ${media}.</p>`
    }
}
