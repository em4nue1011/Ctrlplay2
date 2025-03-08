

arquivo = "listaDeCompras.py"

try:
    open(arquivo, "r")
except FileNotFoundError:
    open(arquivo,"w")

# with open(arquivo,"w") as arq:
#     arq.write("primeira linha do arquivo\n")

# with open(arquivo, "a") as arq:
#     arq.write("linha adicionada no final\n")

nome = "Emanuel"
idade = 14

with open(arquivo, "w") as arq:
    arq.write(f"Nome: {nome}\n")
    arq.write(f"Nome: {idade}\n")