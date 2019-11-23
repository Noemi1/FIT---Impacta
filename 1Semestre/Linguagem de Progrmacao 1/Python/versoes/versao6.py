def bisexto(ano):
    return ano % 4 == 0 and ano % 10 != 0 or ano %400 == 0
        
def qtdDias(mes, ano):
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if bisexto(a): 
        dias[1] += 1
    return dias[mes-1]

mes = int(input('Mês: '))
while not(1 <= mes <= 12):
    mes = int(input('Mês: '))
    
ano = int(input('Ano: '))
while not(1 <= ano):
    ano = int(input('Ano: '))

qtdDias = qtdDias(mes, ano)
if qtdDias == -1:
    print('Mes Invalido')
else:    
    print(qtdDias)