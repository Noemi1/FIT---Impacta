def bisexto(ano):
    return ano % 4 == 0 and ano % 10 != 0 or ano %400 == 0
        
def qtdDias(mes, ano):

    if mes == 1:
        print('Quantidade de dias: %d' % 31)
    elif mes == 2:
        if bisexto(ano):
            print('Quantidade de dias: %d' % 29)
        else:
            print('Quantidade de dias: %d' % 28)
    elif mes == 3:
        print('Quantidade de dias: %d' % 31)
    elif mes == 4:
        print('Quantidade de dias: %d' % 30)
    elif mes == 5:
        print('Quantidade de dias: %d' % 31)
    elif mes == 6:
        print('Quantidade de dias: %d' % 30)
    elif mes == 7:
        print('Quantidade de dias: %d' % 31)
    elif mes == 8:
        print('Quantidade de dias: %d' % 31)
    elif mes == 9:
        print('Quantidade de dias: %d' % 30)
    elif mes == 10:
        print('Quantidade de dias: %d' % 31)
    elif mes == 11:
        print('Quantidade de dias: %d' % 30)
    elif mes == 12:
        print('Quantidade de dias: %d' % 31)
    else:
        print('Mês inválido')

mes = int(input('Mês: '))
ano = int(input('Ano: '))

qtdDias(mes, ano)