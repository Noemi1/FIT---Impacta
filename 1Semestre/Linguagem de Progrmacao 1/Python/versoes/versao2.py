mes = int(input('Mês: '))
ano = int(input('Ano: '))

if mes == 1:
    print('Quantidade de dias: %d' % 31)
elif mes == 2:
    # Opa, depende se o ano é bissexto!
    # um ano é bissexto se: 
    # - É múltiplo de 4 e não de 100
    # - Ou se é múltiplo de 400.
    if ano % 4 == 0 and ano % 10 != 0 or ano %400 ==0:
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