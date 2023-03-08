#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

x1 = int(0)
x2 = int(1)
x3 = int(0)
N = int(input('Digite um número: '))
while N > x3:
    x3 = x1 + x2
    x1 = x2
    x2 = x3
if N == 0 or N == 1:
    print('O número faz parte da sequência de Fibonacci.')
elif N == x3:
    print('O número faz parte da sequência de Fibonacci.')
else:
    print('O número digitado não faz parte da sequência de Fibonacci.')