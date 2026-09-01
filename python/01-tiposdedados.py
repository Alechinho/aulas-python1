#comentarios de uma linha

''' comentarios: auxiliam
a deixar
"anotaçoes" no codigo fonte'''

# concatenaçao
print("Boas Vindas a aula de" + " Python!")

#interpolaçao 
print("Olá {}" . format(input("Qual o seu nome? ")))

#tipo de dados em python - numeros
# Inteiro
idade = 30
print(idade)

# Decimal (float)
altura = 1.75
print(altura)

# número complexo
numero_complexo = 2+3j
print(numero_complexo)

#texto(str)
nome = "Alexandre"
print(nome)

#booleano(bool)
ativo = True
print(ativo)

logado = False
print(logado)

#nenhum valor (NoneType)
valor = None
print(valor)

#Lista(list) mutável
frutas = ["maçã", "banana", "uva"]
print(frutas)

#tupla(tuple) imutável
cores = ("vermelho", "azul", "verde")
print(cores)

#conjunto(set)
numeros = {1, 2, 3, 4}
print(numeros)

#Diconário(dict) pares chave-valor
pessoa = {
    "nome": "Alexandre",
    "idade": 30
}
print(pessoa)


''' Python não tem constantes
verdadeiras, mas usamos convenção
para indicar que um valor não deve ser alterado'''
PI = 3.14159
GRAVIDADE = 9.8

print("O valor de PI é", PI , "\nO valor de Gravidade é" , GRAVIDADE)

