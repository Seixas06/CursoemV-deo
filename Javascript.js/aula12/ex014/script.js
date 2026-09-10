function carregar(){
    var msg=document.getElementById('msg')
    var img=document.getElementById('imagem')
    var data=new Date()
    var hora=data.getHours()
    //var hora=15
    msg.innerHTML=`Agora são ${hora} horas`
    if (hora >=0 && hora<12 ){
        img.src='ftmanha.png'
        document.body.style.background='#d6c99c'
    } else if (hora>=12 && hora<18){
        img.src='fttarde.png'
        document.body.style.background='#cf7624'
    } else{
        img.src='ftnoite.png'
        document.body.style.background='#0a0b06'
    }
}
