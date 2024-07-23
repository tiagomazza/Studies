class Pessoa:
    def __init__(self, pnome,unome,idade,profissao):
        self.pnomeInit = pnome
        self.unomeInit = unome
        self.idadeInit = idade
        self.profissaoInit = profissao
    
    def obterNome(self):
        return self.pnomeInit, self.unomeInit
    
    def obterIdade(self):
        return self.idadeInit
    
    def obterProfissao(self):
        return self.profissaoInit

objPessoas = []