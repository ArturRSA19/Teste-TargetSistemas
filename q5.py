#Escreva um programa que inverta os caracteres de um string.

print('Digite uma STRING abaixo:')
txt = str(input())
print(f'A STRING escrita foi: {txt}')
txtInvertido = txt[::-1]
print(f'A STRING escrita de forma invertida é: {txtInvertido}')