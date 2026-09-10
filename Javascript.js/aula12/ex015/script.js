function verificar(){
    var res=document.getElementById('res')
    var nasctx=document.getElementById('nasc')
    var data=new Date()
    var ano=data.getFullYear()
    if (nasctx.value.length ==0 || Number(nasctx.value) > ano){
        window.alert('[ERRO] Verifique novamente os dados e tente novamente!')
    } else{
        var fsex=document.getElementsByName('radsex')
        var idade= ano-Number(nasctx.value)
        var genero=''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (fsex[0].checked){
            genero='Homem'
            if (idade >=0 && idade<=10){
                //Criança
                img.setAttribute('src','foto-criança-m.png')
            } else if (idade < 21){
                //jovem
                img.setAttribute('src','foto-jovem-m.png')
            } else if (idade<60){
                //adulto
                img.setAttribute('src','foto-adulto-m.png')
            } else if (idade>=60){
                //idoso
                img.setAttribute('src','foto-idoso-m.png')
            }
        } else if (fsex[1].checked){
            genero='Mulher'
            if (idade >=0 && idade<=10){
                //Criança
                img.setAttribute('src','foto-criança-f.png')
            } else if (idade < 21){
                //jovem
                img.setAttribute('src','foto-jovem-f.png')
            } else if (idade<60){
                //adulto
                img.setAttribute('src','foto-adulto-f.png')
            } else if (idade>=60){
                //idoso
                img.setAttribute('src','foto-idoso-f.png')
            }
        }
        res.style.textAlign='center'
        res.innerHTML=`Detectamos ${genero} com ${idade} anos. `
        res.appendChild(img)
    }
}
