'''Calculadora com while'''

while  True: #Interação com o usuário
    numero1 = input ('Digite um número: ')
    operador = input ('Digite seu operador: (+-/*)')
    numero2 = input ('Digite outro número: ')
    
    numero_validos = None

    try:
        num1 = float(numero1)
        num2 = float(numero2)
        numeros_validos = True

    except:
        numeros_validos = None #Mantém None se não for algum número digitado

    if numeros_validos == None:
        print(
            'Você digitou um ou ambos dos números incorretamente! '
        )
        continue

    operador_validado = '+, -, /, *'
    if operador not in operador_validado: #Confere se o usuário digitou operadores validos
        print(
            'Você digitou algum sinal não permitido! '
        )
        continue

    if len(operador) < 1: #Verifica se foi digitado somente um operador
        print(
            'Você digitou mais de um sinal, digite apenas um! '
        )
        continue            

    if operador == '+':
        soma = num1 + num2
        print(
            f'A soma de {num1} + {num2} é igual a: {soma}'
        )
    if operador == '-':
        subtracao = num1 - num2
        print(
            f'A subtração de {num1} + {num2} é igual a: {subtracao}'
        )
    if operador == '/':
        divisao = num1 / num2
        print(
            f'A divisão entre o número {num1} e {num2} é igual a {divisao}'
        )
    if operador == '*':
        multiplicacao = num1 * num2
        print(
            f'A multiplicação entre o número {num1} e {num2} é igual a {multiplicacao}'
        )
    
    sair = input('Quer sair? [s]im').lower().startswith('s')
    
    if sair is True:
        break

    