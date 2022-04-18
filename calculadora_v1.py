# Calculadora em Python

print("\n******************* Python Calculator *******************")


def add (x,y):
	return x + y

def subtract (x,y):
	return x - y

def multiply (x,y):
	return x * y

def divide (x,y):
	return x / y

print("\nSelecione o número da opção desejada:")
print("\n1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = int(input("\nDigite sua opção (1/2/3/4):"))

num1 = int(input("\nDigite o primeiro número:"))

num2 = int(input("\nDigite o segundo número:"))

if operacao == 1:
	print("\n")
	print(num1, "+", num2, "=", add(num1,num2))
	print("\n")

elif operacao == 2:
	print("\n")
	print(num1, "-", num2, "=", subtract(num1,num2))
	print("\n")


elif operacao == 3:
	print("\n")
	print(num1, "*", num2, "=", multiply(num1,num2))
	print("\n")

elif operacao == 4:
	print("\n")
	print(num1, "/", num2, "=", divide(num1,num2))
	print("\n")

else:
	print("Opção inválida")


