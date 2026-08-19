"""
Problema 2 — Ano bissexto: o caso 1900
Nível: Moderado

Receba um ano inteiro e informe:

Bissexto ou Não bissexto

Use exatamente estas regras:

divisível por 400 → bissexto;
divisível por 100, mas não por 400 → não bissexto;
divisível por 4, mas não por 100 → bissexto;
demais anos → não bissextos.
Casos obrigatórios de teste
1900, 2000, 2024, 2100
Microdefesa
Explique por que apenas testar ano % 4 == 0 produz uma resposta errada para pelo menos um dos casos obrigatórios.
"""

ano = int(input(f"informe o ano: "))

if ano % 400 == 0:
    print("Bissexto")
elif ano % 100 == 0:
    print("Não bissexto")
elif ano % 4 == 0:
    print("Bissexto")
else:
    print("Não bissexto")
