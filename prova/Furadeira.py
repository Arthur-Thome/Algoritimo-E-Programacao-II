from Ferramenta import Ferramenta

class Furadeira( Ferramenta ):
    def __init__(self,nome, tensao, preco, potencia):
        self._nome = nome
        self._tensao = tensao
        self._preco = preco
        self._potencia = potencia

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
        self._tensao = valor
    
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self,valor):
        self._preco = valor

    @property
    def potencia(self):
        return self._potencia
    
    @potencia.setter
    def potencia(self,valor):
        self._potencia = valor

    def Cadastrar(self):
        super().getInformacoes()
        print(f"Potencia: {self._potencia}W")