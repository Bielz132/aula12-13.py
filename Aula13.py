# Match Case

n = int(input('Digite um numero de 0 a 3: '))
match n:
    case 0:
        print('é zero')
    case 1:
        print('é um')  
    case 2:
        print('é dois')
    case _:
        print('desconhecido')


print(list(range(18,61)))
