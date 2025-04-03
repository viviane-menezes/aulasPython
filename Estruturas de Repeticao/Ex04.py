print("****************Python Calculator****************")
print("Selecione o número da operação desejada:")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

def soma(x,y):
  s =x+y
  print( "A soma é :",s)

def subtracao(x,y):
  sub =x-y
  print("A subtração é :",sub)

def multiplicacao(x,y):
  mult = x*y
  print("A multiplicação é :",mult)

def divisao(x,y):
  div = x/y
  print(" A divisão é: ", div)

opcao=int(input("Digite sua opção:"))
num1= int(input("Digite o primeiro número:"))
num2=int(input("Digite o segundo número:"))
if opcao ==1:
  soma(num1,num2)

elif opcao==2:
  subtracao(num1,num2)

elif opcao==3:
  multiplicacao(num1,num2)
elif opcao ==4:
  divisao(num1,num2)	
else:
  print("Opção inválida")