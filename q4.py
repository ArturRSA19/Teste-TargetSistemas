#Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado
#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

sp = 67.83643
rj = 36.67866
mg = 29.22988
es = 27.16548
outros = 19.84953 

total = sp + rj + mg + es + outros

print(f'O percentual de representação de SP é: {(sp/total)*100:,.3f} %')
print(f'O percentual de representação de RJ é: {(rj/total)*100:,.3f} %')
print(f'O percentual de representação de MG é: {(mg/total)*100:,.3f} %')
print(f'O percentual de representação de ES é: {(es/total)*100:,.3f} %')
print(f'O percentual de representação de Outros é: {(outros/total)*100:,.3f} %')

