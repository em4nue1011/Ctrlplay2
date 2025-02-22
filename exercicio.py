DDD = {61:"brasilia", 11:"são paulo", 71:"salvador"}

iDDD = int(input("digite o numero do ddd: "))

if iDDD in DDD:
    print(DDD[iDDD])
else:
    print("não tem no dicionario")

    