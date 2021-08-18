from Produto import Produto



p1 = Produto(10)

p1.imprimir()



p1.preco = 19.9

p1.nome = "iPhone"



print( "Novo preço do ", p1.nome)

print( p1.aumentarPreco( 10 ) )





print( "-----\n" ) 

p1.imprimir() 