function contar(){
    var inc=document.getElementById('inc')
    var fim=document.getElementById('fim')
    var pas=document.getElementById('pas')
    var res=document.getElementById('res')
    if (inc.value.length==0 || fim.value.length==0 || pas.value.length==0){
        res.innerHTML='Impossível contar!'
        //window.alert('[ERRO] Faltam dados!')
    } else {
        res.innerHTML=`Contando: <br>`
        let i=Number(inc.value)
        let f=Number(fim.value)
        let p=Number(pas.value)
        if (p<=0){
            window.alert('Passo inválido! Considerando PASSO 1...')
            p=1
        }
        if (i<f){
            //Contagem crescente
            for(let c=i;c<=f;c+=p) {
                res.innerHTML+=` ${c} \u{1F449} `
            }
        } else {
            //Contagem regressiva
            for(let c=i;c>=f;c-=p){
                res.innerHTML+=` ${c} \u{1F449}`
            }
        }
        res.innerHTML+=`\u{1F3C1}`
    }
}
