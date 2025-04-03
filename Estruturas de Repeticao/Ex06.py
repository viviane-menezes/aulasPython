# Ler a letra

letra = input('Letra (F ou M):').upper()

# Verificar e mostrar a mensagem

if letra == 'F':
  print('F-Feminino')
elif letra == 'M':
  print('M-Masculino')
else:
  print('Sexo inválido')
