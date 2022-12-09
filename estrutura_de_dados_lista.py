# Programa trabalhando com a estrutura de dados lista
# Autor: Emerson Lima dos Santos

# Estrutura de dados é o ramo da computação que estuda os diversos mecanismos de organização de dados para atender aos diferentes requisitos de processamento.

# Lista
# Listas em Python são similares a tuplas, pois podem conter elementos de tipos distintos, embora usualmente os elementos de listas tenham todos o mesmo tipo. Listas são mutáveis.

# Métodos para trabalhar com lista

# definindo uma lista de inteiros
lista = [1,2,3,4,5,1]
# acessando o primeiro elemento da lista
lista[0]
# acessando o último elemento da lista
lista[4]

# definindo uma lista de inteiros
lista1 = [1,2,3,4,5,1]
#alterando o primeiro elemento da lista
lista1[0] = 6
# inserir um valor x na posição y da lista - insert(y,x)
lista1.insert(0,10)
lista1
# inserir um valor x na última posição da lista - append(x)
lista1.append(25)
lista1

# definindo uma lista de inteiros
lista2 = [1,2,3,4,5,1]
# remover e retornar o elemento de indice y da lista - pop(y)
lista2.pop(5)
lista2

# definindo uma lista de inteiros
lista3 = [1,2,3,4,5,1]
# remover a primeira ocorrência do elemento x da lista - remove(x)
lista3.remove(1)
lista3

# definindo uma lista de inteiros
lista4 = [1,2,3,4,5,1]
# retornando o número de ocorrências de x na lista - count(x)
lista4.count(1)

# definindo uma lista de inteiros
lista5 = [1,2,3,4,5,1]
# retornando o índice de x na lista - index(x)
lista5.index(2)

# definindo uma lista de inteiros
lista6 = [1,2,3,4,5,1]
# inverte a lista
lista6.reverse()
lista6

# definindo uma lista de inteiros
lista7 = [1,2,3,4,5,1]
# retorna a lista em ordem crescente
lista7.sort()
lista7

# definindo uma lista de inteiros
lista8 = [1,2,3,4,5,1]
# retorna o menor e o maior valor da lista
print(min(lista8))
print(max(lista8))

# definindo uma lista de inteiros
lista9 = [1,2,3,4,5,1]
# soma todos os valores da lista
print(sum(lista9))

# definindo uma lista de inteiros
lista10 = [1,2,3,4,5,1]
# retorna a quantidade de elementos da lista
print(len(lista10))