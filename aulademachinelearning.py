from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
# saber se e porco ou cachorro
# 1 pelo longo
# 2 perna curta
# 3 au au

porco1 = [0 ,1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1, 0]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

treino_x = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
treino_y = [1, 1, 1, 0, 0, 0]

modelo = LinearSVC()
modelo.fit(treino_x, treino_y)

animal_misterioso1 = [1, 1, 1]
animal_misterioso2 = [1, 1, 0]
animal_misterioso3 = [0, 1, 1]

teste_x = [animal_misterioso1, animal_misterioso2, animal_misterioso3]
teste_y = [0, 1, 1]

Resultado = modelo.predict(teste_x)
print(Resultado)

accuracy = accuracy_score(teste_y, Resultado)
print(accuracy * 100)