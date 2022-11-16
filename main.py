print('#####################################################################################################')
print('Bem vindo a sorveteria do Leonardo')
print('#####################################################################################################')
print('------------------------------------------CARDÁPIO---------------------------------------------------')
print('CÓDIGO   |  DESCRIÇÃO   |  TAMANHO  P|  TAMANHO  M  |   TAMANHO  G')
print('   TR    | Tradicional  |  R$ 6.00   |   R$ 10.00   | R$ 18.00    ')
print('   ES    |   Especial   |  R$ 7.00   |   R$ 12.00   | R$ 21.00    ')
print('   PR    |   Premium    |  R$ 8.00   |   R$ 14.00   | R$ 24.00    ')
print('=====================================================================================================')

acumulador = 0

while True:
    tamanho = input('Entre com o Tamanho do pote desejado P/M ou G:')
    if (tamanho != 'P')and(tamanho != 'p')and(tamanho != 'm')and(tamanho !='M')and(tamanho!='g')and(tamanho!='G'):
        print('!!! TAMANHO OU CÓDIGO INVÁLIDO !!!')
        continue #Se o usuário digitar algo inválido o input do 'tamanho' será repetido.

    codigo =input('Entre com o código do sabor desejado TR/ES ou PR:')
    if (codigo != 'TR') and (codigo != 'tr') and (codigo != 'ES') and (codigo != 'es') and (codigo != 'PR') and(codigo != 'pr'):
        print('!!! TAMANHO OU CÓDIGO INVÁLIDO !!!')
        continue #Se o usuário digitar algo inválido o input do 'codigo' será repetido.

    if codigo == 'TR' or codigo == 'tr'  and (tamanho == 'P' or tamanho == 'p'):
        acumulador = acumulador + 6
        print('Você escolheu o sabor tradicional, pote no tamanho P, valor de R$ {:.2f}'.format(acumulador))

    elif codigo == 'TR' or codigo == 'tr' and (tamanho == 'M' or tamanho == 'm'):
        acumulador = acumulador +10
        print('Você escolheu o sabor tradicional, pote no tamanho M, valor de R$ {:.2f}'.format(acumulador))

    elif codigo == 'TR' or codigo == 'tr' and (tamanho == 'G' or tamanho == 'g'):
        acumulador = acumulador + 18
        print('Você escolheu o sabor tradicional, pote no tamanho G, valor de R$ {:.2f}'.format(acumulador))

    elif codigo == 'ES' or codigo == 'es' and (tamanho == 'P' or tamanho == 'p'):
        acumulador = acumulador + 7
        print('Você escolheu o sabor especial, pote no tamanho P, valor de R$ {:.2f}'.format(acumulador))

    elif codigo == 'ES' or codigo == 'es' and (tamanho == 'M' or tamanho == 'm'):
        acumulador = acumulador + 12
        print('Você escolheu o sabor especial, pote no tamanho M, valor de R$ {:.2f}'.format(acumulador))

    elif codigo == 'ES' or codigo == 'es' and (tamanho == 'G' or tamanho == 'g'):
        acumulador = acumulador + 21
        print('Você escolheu o sabor especial, pote no tamanho G, valor de R$ {:.2f}'.format(acumulador))

    elif codigo == 'PR' or codigo == 'pr' and (tamanho == 'P' or tamanho == 'p'):
        acumulador = acumulador + 8
        print('Você escolheu o sabor premium, pote no tamanho P, valor de R$ {:.2f}'.format(acumulador))

    elif codigo == 'PR' or codigo == 'pr' and (tamanho == 'M' or tamanho == 'm'):
        acumulador = acumulador + 14
        print('Você escolheu o sabor premium, pote no tamanho M, valor de R$ {:.2f}'.format(acumulador))

    elif codigo == 'PR' or codigo == 'pr' and (tamanho == 'G' or tamanho == 'g'):
        acumulador = acumulador + 24
        print('Você escolheu o sabor premium, pote no tamanho G, valor de R$ {:.2f}'.format(acumulador))

    print('-----------------------------------------------------------------------------------------------------------')
    conta = input('Deseja pedir mais alguma coisa ? [S/N]')
    conta = conta.upper()
    if conta == 'S':
        continue
    else:
        print('O valor total a ser pago é de R$ {:.2f}. '.format(acumulador))
        print('fim de programa...')
        break



