'''Construa um programa para fazer uma pequena entrevista com
os alunos de uma turma. Na entrevista, são informados o sexo e
a idade de cada aluno. Considere que o usuário não sabe quantos alunos existem na turma. O programa deve exibir a quantidade de homens acima de 18 anos e a quantidade de mulheres de
qualquer idade. Para encerrar o programa, o usuário deve informar uma idade negativa'''
homens = 0
mulher=0
while True:
    idade = int(input(" Informe sua idade: "))
    if idade < 0:
       break
    sexo = input("Informe seu Sexo [F/M]: ")
    if sexo.upper()=='M':
        if idade>18:
            homens+=1
    if sexo.upper()=='F':
        mulher+=1
print(f'A quantidade de homens é:  {homens}')     
print(f'A quantidade de mulheres é:  {mulher}')    
print('Programa encerrado')