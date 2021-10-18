from abc import ABCMeta, abstractmethod, abstractproperty

class Ferramenta(metaclass = ABCMeta):
    @property
    def nome(self):
        pass

    @nome.setter
    @abstractmethod
    def nome(self,valor):
        pass

    @property
    def tensao(self):
        pass

    @tensao.setter
    @abstractmethod
    def tensao(self,valor):
        pass
    
    @property
    def preco(self):
        pass

    @preco.setter
    @abstractmethod
    def preco(self,valor):
        pass

    def getInformacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Tensão: {self.tensao}")
        print(f"Preço: R$ {self.preco}")

    @abstractmethod
    def Cadastrar(self):
        pass