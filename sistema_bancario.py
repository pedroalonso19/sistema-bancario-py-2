i = -1
saldo = 450
numero_saques = 0
LIMITE_SAQUES = 3
limite = 500
extrato = ""

def realizar_saque(saldo, extrato, numero_saques, LIMITE_SAQUES, limite):
    if numero_saques < LIMITE_SAQUES:
        saque = float(input("\nDigite o valor do saque: R$"))

        if saque > saldo: 
            print("Saldo insuficiente")

        elif saque < 0:
            print("Valor de saque inválido!")

        elif saque > limite:
            print("Valor acima do limite de saque permitido!")

        else:
            saldo -= saque
            extrato += f"Saque: R${saque:.2f}\n"
            numero_saques += 1   
    else: 
        print("Atingiu o valor diário de saques!")
    return saldo, extrato, numero_saques

def realizar_deposito(saldo, extrato):
    deposito = float(input("\nDigite o valor do depósito: R$"))

    if deposito < 0:
        print("Depósito inválido!\n")

    else:
        saldo += deposito
        extrato += f"Depósito: R${deposito:.2f}\n"
    return saldo, extrato

def mostrar_extrato(saldo, extrato):
    if extrato == "":
        print("Não foram realizadas operações!") 

    else: 
        print(f'''============= EXTRATO =============
Operações: 
{extrato}

Saldo final: {saldo}
''')
    return saldo, extrato

while True: 
    i = int(input('''
========Digite a opção desejada=========
    1. Depósito
    2. Saque
    3. Extrato     
    0. Sair                  
\n'''))
    
    if i == 1:
        saldo, extrato = realizar_deposito(saldo, extrato)

    elif i == 2:
        saldo, extrato, numero_saques = realizar_saque(saldo, extrato, numero_saques, LIMITE_SAQUES, limite)

    elif i == 3:
        saldo, extrato = mostrar_extrato(saldo, extrato)
            
    elif i == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada!")