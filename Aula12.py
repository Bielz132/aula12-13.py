import os
# with open('teste.txt','r') as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

         # ^ 
#----------|__> abre algum arquivo para o o codigo atual  

# os.rename('teste.c', 'teste_2.0.c') --> renomear arquivos


with os.scandir('C:/Users/aluno/Desktop/Aluno') as pasta:
    for p in pasta:
        print('arquivos', p.name) # p.name = mostra todas as possibilidades em outras palavras mostra tudo dentro da pasta




