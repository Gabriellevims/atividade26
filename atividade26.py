# Exercício Python 26: Desenvolva um programa que leia o primeiro termo e a razão de uma Pogreçao Aritimetica.
# No final, mostre os 10 primeiros termos dessa progressão.
# Solicita o primeiro termo e a razão da PA ao usuário
termo1= int(input("Digite o número:"))
pro= int(input("Digite a razão:"))
for i in range (10):
    print(i)
    termo = termo1 + i * pro
    print(f'Termo {i+1}: {termo}')