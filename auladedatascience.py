import pandas as pd

uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.3/movies.csv"

filmes = pd.read_csv(uri)

filmes.columns = ["filmeId", "titulo", "generos"]

uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"
notas = pd.read_csv(uri)

notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
#print(notas.head())

#print(notas["nota"].head()) #series

unico = notas["nota"].unique()
#print(unico)
media = notas["nota"].mean()
minimo = notas["nota"].min()

descrever = notas.describe()
print(descrever)