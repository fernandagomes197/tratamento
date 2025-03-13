while True:
    try:
        n1 = int(input('digite um numero: '))
        n2 = int(input('digite outro numero: '))

        conta = n1 / n2

    except ZeroDivisionError:
        print('NÂO PERMITIDO DIVIDIR 0, REFAÇA O CÁUCULO')
    except ValueError:
        print('por favor, faça a conta digitando apenas números inteiros ')

    else: 
        print(f'{n1} dividido por {n2} é = {conta}')
        break


