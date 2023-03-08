#Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#O menor valor de faturamento ocorrido em um dia do mês;
#O maior valor de faturamento ocorrido em um dia do mês;
#Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

vetor = [22174.1664, 24537.6698, 26139.6134, 26742.6612, 42889.2258, 46251.174, 11191.4722, 3847.4823, 373.7838, 2659.7563, 48924.2448, 18419.2614, 35240.1826, 43829.1667, 18235.6852, 4355.0662, 13327.1025, 25681.8318, 1718.1221, 13220.495, 8414.61]
print(f'O menor valor de faturamento ocorrido em um dia do mês é: {min(vetor)}')
print(f'O maior valor de faturamento ocorrido em um dia do mês é: {max(vetor)}')

vetorSuperior = []

soma = sum(vetor)
media = soma/30

for i in vetor:
    if i > media:
        vetorSuperior.append(i)

print(f'O número de dias no mês em que o valor de faturamento diário foi superior a média mensal foi de {len(vetorSuperior)} dias!')

