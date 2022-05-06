print('Verificando o tempo de vida');

idadeVar = int(input('Qual sua idade \n'));

diasVar = idadeVar * 365;

mesesVar = int(diasVar / 30);

semanaVar = int(diasVar / 7);

totalDiaVar = 90 * 365;

totalSemanaVar = int(totalDiaVar / 7);

totalMesVar = int(totalDiaVar / 30);

print(f'Você tem {diasVar} dias de vida, {semanaVar} semanas e também {mesesVar} meses');

print(f'Considerando que você viva até os 90 você tem apenas\n' + ' '+ str(totalDiaVar - diasVar) + ' ' + 'dias,' + ' ' + str(totalSemanaVar - semanaVar) + ' ' + 'semanas' 
      + ' ' + str(totalMesVar - mesesVar)+ ' ' + 'meses');


