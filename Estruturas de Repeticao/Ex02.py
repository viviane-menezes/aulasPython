'''Para construir o programa a seguir, considere que os usuários só informarão números inteiros positivos. Crie um programa que receba 5 números digitados e, ao fim, exibir quantos
números são pares'''

qtd = 0
pares = 0
impares = 0
while qtd<5:
    numeros = int(input('Informe um número: '))
    qtd+=1
    if numeros % 2 == 0:
        pares+=1
    else:
        impares+=1
print(f'Quantidade de números pares: {pares}')        
print(f'Quantidade de números ímpares: {impares}')