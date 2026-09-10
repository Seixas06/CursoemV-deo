function gerar(){
    let numtxt=document.getElementById('num')
    let sel=document.getElementById('seltab')
    if (numtxt.value.length==0){
        window.alert('Por favor, digite um número!')
    } else{
        let num=Number(numtxt.value)
        let cont=1
        sel.innerHTML=''
        while(cont!=11){
            let item=document.createElement('option')
            item.text=`${num} x ${cont} = ${num*cont}`
            item.value=`sel${cont}`
            sel.appendChild(item)
            cont++
        }
    }
}
