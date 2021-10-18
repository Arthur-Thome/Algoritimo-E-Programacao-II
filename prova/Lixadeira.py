from Ferramenta import Ferramenta

class Lixadeira( Ferramenta ):
    def __init__(self,nome, tensao, preco, rotacoes):
        self._nome = nome
        self._tensao = tensao
        self._preco = preco
        self.__rotacoes = rotacoes

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,valor):
        self._nome = valor

    @property
    def tensao(self):
        return self._tensao
    
    @tensao.setter
    def tensao(self,valor):
        self._cor = valor
    
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self,valor):
        self._preco = valor

    @property
    def rotacoes(self):
        return self.__rotacoes

    @rotacoes.setter
    def rotacoes(self,valor):
        self.__rotacoes = valor

    def Cadastrar(self):
        super().getInformacoes()
        print(f"Rotações: {self.__rotacoes}RPM")