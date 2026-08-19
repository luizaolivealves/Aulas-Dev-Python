"""""
Problema 3 — Maior e menor com empates parciais
Nível: Moderado/Difícil

Receba três números inteiros a, b e c.

O programa deve:

informar Todos iguais se os três valores forem iguais;
caso contrário, exibir o maior valor;
exibir o menor valor.
Atenção: empates parciais são válidos
Seu programa deve funcionar também para:

8, 8, 3
4, 9, 9
5, 2, 5
Restrição
Não utilize min() nem max().

Microdefesa
Explique por que testar apenas a > b and a > c não é suficiente para todos os casos.
"""

a = int(input("Digite um numero: "))
b = int(input("Digite um segundo numero: "))
c = int(input("Digite um terceiro numero: "))

if a == b == c:
    print(f"Todos iguais")
else: 
    if a >= b and a >= c:
        maior = a
    if b >= a and b >= c:
        maior = b
    if c >= a and c >= b:
        maior = c
    print(f"o numero {maior} é maior que o restante")

    if a <= b and a <= c:
        menor = a
    if b <= a and b <= c:
        menor = b
    if c <= b and c <= a:
        menor = c
    print(f"o numero {menor} é maior que o restante")

    #MICRO DEFESA: não é suficente pois pode gerar empate em umeros maiores do mesmo valor, 
    #devemos utilizar = com mais ou menos para que os empates parciais ocorram