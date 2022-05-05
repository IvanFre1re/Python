print('Economia')

meta_economia = int(input('Qual sua meta de economia?\n'))

saldo = int(input('Quanto você tem guardado\n'))

print('Ok, agora vamos analisar sua economia')

if saldo > meta_economia:
    print('Parabéns você conseguiu ultrapassar sua meta')

elif saldo == meta_economia:
    
    print('Boa, você conseguiu bater sua meta')

else: 
    print('Putz, você gastou muito com bebida')
    
    