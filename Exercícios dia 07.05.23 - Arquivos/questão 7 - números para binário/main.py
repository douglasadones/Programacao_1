"""Faça um programa que recebe um vetor de n números, converta cada um desses números
para binário e grave a sequência de 0s e 1s em um arquivo texto. Cada número deve ser
gravado em uma linha."""

import os

vetor = input('Informe os número: ').split()
with open('convertido.txt', 'w') as file:
    convertido = []
    for num in vetor:
        resto = 0
        num = int(num)
        string_bin = ''
        while num >= resto:
            resto = num % 2
            num = num // 2
            string_bin += str(resto)
        convertido.append(string_bin[::-1])
    for bin in convertido:
        file.write(bin + '\n')



# os.remove('convertido.txt')  # Remove um arquivo específico
# os.rename()  # renomear um arquivo
# os.mkdir()  # Criar uma pasta
# os.chdir()  # Direcionar para um diretório
