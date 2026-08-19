"""
Problema 4 — Intervalo e paridade
Nível: Moderado

Receba um número inteiro.
Calcule três valores booleanos:
se o número está entre 10 e 50, inclusive;
se é par;
se atende às duas condições ao mesmo tempo.

Exiba:
Está no intervalo: True/False
É par: True/False
Atende às duas regras: True/False

Casos obrigatórios de teste
10, 50, 9, 51, 11

Microdefesa
Explique a diferença entre usar and e or na terceira regra.
"""

numero = int(input("Digite um numero inteiro: "))

intervalo = numero >= 10 and numero <= 50
par = numero % 2 == 0
duascondicao = intervalo and par

print("Esta no intervalo:", intervalo)
print("E par:", par)
print("Atende às duas regras:", duascondicao)

#Micro defesa: o and impõe que as duas sejam verdadeiras, enquanto o or só impõe que pelo uma das duas
# sejam verdadeiras, a terceira regra exige que esteja dentro da regra do 10 e 50 e também seja par,
# deve ser utilizado o and