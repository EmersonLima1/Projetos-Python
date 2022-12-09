# Programa para encontrar nomes que começam com determinada letra
# Autor: Emerson Lima dos Santos

# lista de nomes
nomes = ["Emerson", "Tarciana", "Vicente", "Dandara", "Eduarda", "Luiz", "Thiago", "Vanessa", "Marta", "Mateus", "Tainara", "Pedro", "Emily", "Amanda"]

# definindo a função
def encontrando_nomes_comecando_com(letra,dados):
  saida = []
  for nome in dados:
    if nome[0] == letra:
      saida.append(nome)
  return saida

nomes_teste = encontrando_nomes_comecando_com("E",nomes)
print(nomes_teste)