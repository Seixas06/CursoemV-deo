class Seixas:
    def __init__(self):
        self.nome=''
        self.idade=0
        
    def aniversario(self):
        self.idade+=1
    
    def msg(self):
        return f'{self.nome} Seixas tem {self.idade} anos de idade.'
    
p1=Seixas()
p1.nome='mateus'
p1.idade=16
p1.aniversario()
print(p1.msg().title())