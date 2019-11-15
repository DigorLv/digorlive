n1 = float(input("Insira o primeiro número: "))
operador = str(input("Escolha uma operação +,-,* ou /: "))
n2 = float(input("Insira o segundo número: "))

def soma(x,y):
    global n1
    global n2
    print(n1+n2)
def subtracao(x,y):
    global n1
    global n2
    print(n1-n2)
def multiplicacao(x,y):
    global n1
    global n2
    print(n1*n2)
def divisao(x,y):
    global n1
    global n2
    print(n1/n2)

while(n1 != 0):
    if(operador == '+'):
        soma(n1,n2)
    elif(operador == '-'):
        subtracao(n1,n2)
    elif(operador == '*'):
        multiplicacao(n1,n2)
    elif(operador == '/'):
        divisao(n1,n2)
    n1 = float(input("Insira o primeiro número (Se quiser terminar o programa, digite 0): "))
    if(n1 != 0):
        operador = str(input("Escolha uma operação +,-,* ou /: "))
        n2 = float(input("Insira o segundo número: "))
