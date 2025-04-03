'''Crie um programa no qual o usuário informe um número inteiro positivo N e armazene-o em uma variável. Em seguida, o usuário deve digitar N números. Ao fim, o programa deve imprimir a média aritmética dos N números digitados. 
'''
num=int(input('Informe a quantidade de números: '))
soma=0
for c in range(num):
    numero = int(input('Informe um número: '))
    soma+=numero
media=soma/num
print(f'Média = {media:.2f}') 



