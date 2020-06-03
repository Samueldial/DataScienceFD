pessoa = "Michael"

def mais_um_ano(idade):
    return idade + 1

print(mais_um_ano(30))

filme1 = "Toy Story"
filme2 = "Xuxa"
filme3 = "Matrix"

filmes = ["toy story", "xuxa", "matrix"]

print(filmes[1])

def imprime_filmes(filmes):
    print("A lista de filmes e")
    for filme in filmes:
        print(filme)

imprime_filmes(filmes)

print(filmes[1:])
print(filmes[-2:])

dados = {"nome" : "guilherme", "idade" : 37, "empresa" : "Alura"}
print(dados["empresa"])