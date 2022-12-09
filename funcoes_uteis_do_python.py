# Programa com 5 funções úteis do Python para ser utilizada no código
# Autor: Emerson Lima dos Santos

# 1 - Usando o metódo embutido zip para combinar listas e também para extraí-las de volta

cursos = ["Ciência da Computação", "Engenharia da Computação", "Sistemas de Informação"]
aluno = ["Emerson", "Tarciana", "Vicente"]
num_de_faltas = [2, 4, 1]
dados_combinados = list(zip(cursos,aluno,num_de_faltas))

# verificando o dados combinados
dados_combinados 

# recuperando os dados mas em forma de tuplas
c,a,n = zip(*dados_combinados)
# cursos
c
# aluno
a
# número de faltas
n

# 2 - A maneira mais fácil de encontrar valores N-Maior e N-Menor de um iterável

import heapq

valores = [1,2,3,101,102,103]

# imprimir os três maiores
print(heapq.nlargest(3,valores))

# imprimir os três menores
print(heapq.nsmallest(3,valores))

# 3 - Any & All ajuda você a verificar se um determinado iterável contém todos os True ou False ou uma combinação

valores = [True, True, True]

alt_valores = [False, True, True]

# all retorna True somente se todos os valores são True
print(all(valores))
print(all(alt_valores))

# any retorna True se tiver pelo menos um valor True
print(any(valores))
print(any(alt_valores))

# 4 - Use o método join embutido para unir strings individuais para criar uma string grande

individual = ["Olá!", "Meu", "nome", "é", "Emerson!"]

string_combinada = ' '.join(individual)
string_combinada

# 5 - Na próxima vez que você precisar imprimir um iterável e o contador, use enumerate em vez de range & len como uma combinação
# Bônus: O enumerate tem um argumento opcional start para especificar qual deve ser o contador inicial

aluno = ["Emerson", "Tarciana", "Vicente"]

for counter, nome in enumerate(aluno, start=0):
  print(f"{counter}.{nome}")