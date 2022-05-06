print('Seja bem vindo ao programa de calculadora');

total = float(input('Qual o total da conta?'));

pessoas = int(input('Quantas pessoas vão dividir a conta'));

porcentagem = float(input('Quantos porcento vai dar de gorjeta?'));

calc = (total / pessoas) + (total / pessoas * porcentagem / 100)
calc_rounded = round(calc, 2);

print(f'Cada pessoa deve pagar {calc_rounded}');




