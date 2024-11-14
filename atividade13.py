# 1: Verificando se o número é par ou ímpar

n = int(input('Digite um numero: '))

match n:
    case n if n % 2 == 0 :
        print('é par')
    case _:
        print('é ímpar')


# 2: Verificando se um número é positivo, negativo ou zero

# n = int(input('Digite um numero de 0 a 3: '))
# match n:
#     case 0:
#         print('é zero')
#     case 1:
#         print('é um')  
#     case 2:
#         print('é dois')
#     case _:
#         print('desconhecido')


# 3: Verificando se uma string é vazia ou não

# n = int(input('Digite um numero de 0 a 3: '))
# match n:
#     case 0:
#         print('é zero')
#     case 1:
#         print('é um')  
#     case 2:
#         print('é dois')
#     case _:
#         print('desconhecido')


# 4: Verificando se um número é maior, menor ou igual a 10

n = 10
num = int(input('Digite um numero: '))
match num:
    case n if n <10:
        print('é menor que 10')
    case n:
        print('é igual a 10')  
    case n if n >10:
        print('é maior que 10')

# 5: Classificando uma idade em faixas etárias -  criança, jovem, adulto, idoso

idade = int(input('Digite sua idade: '))
match idade:
    case idade if idade <11:
        print('é uma criança')
    case idade if idade >12:
        print('é um jovem') 
    case idade if idade <18:
        print('é um jovem') 
    case idade if idade >19:
        print('é um adulto')
    case idade if idade <60:
        print('é um adulto')
    case idade if idade >61:
        print('é um idoso')