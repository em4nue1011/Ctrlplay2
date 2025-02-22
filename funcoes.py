def soma(a,b,c):
    return a + b + c

print(soma(5,3,4))
print(soma(5,2,2))

def multiplicao(d,e,f):
    return d*e*f

print(multiplicao(784,549,724))

def bemVindo():
    print("BIEN VINIDO")

def menor(a,b):
    if a <=b:
        return a
    else:
        return b
    

print(menor(25,15))

def velocidademedia(tempo,distancia):
    return distancia/tempo

distancia = float(input("Digite a distancia: "))
tempo = float(input("Digite o tempo em horas: "))

print(velocidademedia(tempo,distancia))