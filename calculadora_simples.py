# Programa de uma calculadora simples
# Autor: Emerson Lima dos Santos

# Essa funcao soma dois numeros
def soma(x,y):
	return x+y

# Essa funcao subtrai dois numeros
def subt(x,y):
	return x-y

# Essa funcao multiplica dois numeros
def mult(x,y):
	return x*y

# Essa funcao divide dois numeros
def div(x,y):
	return x/y

print("Selecione a operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

while True:
	# recebe escolha do usuario
	escolha = input("Entre com uma das opções(1/2/3/4):")

	# verifica se a escolha faz parte das opções válidas
	if escolha in ('1', '2', '3', '4'):
		num1 = float(input("Entre com o primeiro número: "))
		num2 = float(input("Entre com o segundo número: "))

		if escolha == '1':
			print(num1, "+", num2, " = ", soma(num1,num2))

		elif escolha == '2':
			print(num1, "-", num2, " = ", subt(num1,num2))

		elif escolha == '3':
			print(num1, "*", num2, " = ", mult(num1,num2))

		elif escolha == '4':
			print(num1, "/", num2, " = ", div(num1,num2))

		# verifica se o usuario quer realizar outra operação
		# sai do laço se a resposta for não
		proxima_operacao = input("Deseja realizar outra operação? (sim/não): ")
		if proxima_operacao == "não":
			break

	else:
		print("Entrada Inválida")



