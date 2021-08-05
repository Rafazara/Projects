# Calculadora Simples

# Função para soma de dois números 
def add(x, y):
    return x + y

# Função para subtração de dois números
def subtract (x, y):
    return x - y

# Função para multiplicar dois números
def multiply(x, y):
    return x * y

# Função para dividir dois números
def divide(x, y):
    return x / y

print("Selecione a operação.")
print("1.Adição")
print("2.Subtração")
print("3.Multiplicação")
print("4.Divisão")

while True:
   
    escolha = input("Enter choice(1/2/3/4): ")

    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if escolha == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif escolha == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif escolha == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif escolha == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")