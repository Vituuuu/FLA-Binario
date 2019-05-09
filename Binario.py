#=============Variaveis========================================
#Usei uma variavel para um comando do usuario, e a outra serve
#para depois colocar o resultado dos calculos

user =int(input('Digite um numero: '))

pegresult = ''
#==============================================================
#===================Repetir ate nao dar mais===================
#Serve para dividir ate nao poder mais repetir, e, transformar
#os resultados dessas didvisoes(inteiras) e transforma-las de int em str
#==============================================================

while user > 0:
    pegresult = pegresult + str(user % 2)
    user = user // 2

#============Colocar os resultados de tras pra frente==========

print (pegresult [::-1])
