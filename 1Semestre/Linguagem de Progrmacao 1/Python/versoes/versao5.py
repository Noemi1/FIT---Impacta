def bisexto(ano):
    return ano % 4 == 0 and ano % 10 != 0 or ano %400 == 0
        
def qtdDias(mes, ano):
    if mes == 1:
        return 31
    elif mes == 2:
        if bisexto(ano):
            return 29
        else:
            return 28
    elif mes == 3:
        return 31
    elif mes == 4:
        return 30
    elif mes == 5:
        return 31
    elif mes == 6:
        return 30
    elif mes == 7:
        return 31
    elif mes == 8:
        return 31
    elif mes == 9:
        return 30
    elif mes == 10:
        return 31
    elif mes == 11:
        return 30
    elif mes == 12:
        return 31
    else:
        return -1

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