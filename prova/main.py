from Furadeira import Furadeira
from Lixadeira import Lixadeira


def menu():
    return input(f"""
    =======================================
    |{"MENU":>20}                 |
    =======================================
    |  0 - Sair                           |
    |  1 - Cadastrar Furadeiras           |
    |  2 - Cadastrar Lixadeiras           |
    |  3 - Listar Furadeiras              |
    |  4 - Listar Lixadeiras              |
    =======================================
    Escolha: """)

listaFuradeira = []
listaLixadeira = []

while True:
    escolha = menu()
    if escolha.isnumeric():
        if escolha == "0":
            break
        elif escolha == "1":
            print("Cadastramento de Furadeira\n")
            nomeFuradeira = input("Digite o nome: ")
            tensaoFuradeira = int(input("Digite a tensão: "))
            precoFuradeira = float(input("Digite o preço: "))
            potenciaFuradeira = float(input("Digite a potencia: "))
            d1 = Furadeira(nomeFuradeira,tensaoFuradeira ,precoFuradeira, potenciaFuradeira)
            listaFuradeira.append([d1.nome, d1.tensao,d1.tensao, d1.potencia])
            print("\nFuradeira cadastrada com sucesso.")
        elif escolha == "2":
            print("Cadastramento de Lixadeira\n")
            nomeLixadeira = input("Digite o nome: ")
            tensaoLixadeira = int(input("Digite a tensão: "))
            precoLixadeira = float(input("Digite o preço: "))
            rotacaoLixadeira = float(input("Digite a Rotação: "))
            l1 = Lixadeira(nomeLixadeira,tensaoLixadeira ,precoLixadeira, rotacaoLixadeira)
            listaLixadeira.append([l1.nome, l1.tensao,l1.tensao, l1.rotacoes])      
            print("\nLixadeira cadastrada com sucesso.")
        elif escolha == "3":
            for c,i in enumerate(listaFuradeira):
                print(f"{c} - {i}")
        elif escolha == "4":
            for x,i in enumerate(listaLixadeira):
                print(f"{x} - {i}")
    else:
        print("Digite somente números.")