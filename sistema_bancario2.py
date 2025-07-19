import textwrap

i = -1

def realizar_saque(*, saldo, extrato, limite, numero_saques, limite_saques):
    valor = float(input("\nDigite o valor do saque: R$"))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def realizar_deposito(saldo, extrato, /):
    valor = float(input("\nDigite o valor do depósito: R$"))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario(lista_usuarios):
    cpf = input("Digite o CPF (apenas números): ")
    if buscar_usuario_por_cpf(cpf, lista_usuarios):
        print("\n@@@ Este CPF já está cadastrado! @@@")
        return

    nome = input("Digite o nome completo: ")
    nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o endereço (logradouro, número - bairro - cidade/UF): ")

    novo_usuario = {
        "nome": nome,
        "data_nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    lista_usuarios.append(novo_usuario)
    print("=== Usuário registrado com sucesso! ===")

def buscar_usuario_por_cpf(cpf, lista_usuarios):
    for usuario in lista_usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def abrir_conta(agencia, numero, lista_usuarios):
    cpf = input("Informe o CPF do titular da conta: ")
    usuario = buscar_usuario_por_cpf(cpf, lista_usuarios)
    if usuario:
        print("\n=== Nova conta aberta com sucesso! ===")
        return {
            "agencia": agencia,
            "numero_conta": numero,
            "usuario": usuario,
            "saldo": 0,
            "numero_saques": 0,
            "LIMITE_SAQUES": 3,
            "limite": 500,
            "extrato": ""
        }
    print("\nCPF não localizado, encerrando abertura de conta!")
    return None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\ 
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    usuarios = []
    contas = []
    agencia = "0001"
    numero_conta = 1

    conta_padrao = {
        "saldo": 450,
        "numero_saques": 0,
        "LIMITE_SAQUES": 3,
        "limite": 500,
        "extrato": ""
    }
    contas.append({
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": {"nome": "Titular Padrão", "cpf": "00000000000", "data_nascimento": "", "endereco": ""},
        **conta_padrao
    })

    while True:
        print('''
========Digite a opção desejada=========
    1. Depósito
    2. Saque
    3. Extrato
    4. Criar usuário
    5. Criar conta
    6. Listar contas
    0. Sair
''')
        i = int(input("Opção: "))

        if i == 1:
            conta = contas[0]
            contas[0]["saldo"], contas[0]["extrato"] = realizar_deposito(conta["saldo"], conta["extrato"])
        elif i == 2:
            conta = contas[0]
            contas[0]["saldo"], contas[0]["extrato"], contas[0]["numero_saques"] = realizar_saque(
                saldo=conta["saldo"],
                extrato=conta["extrato"],
                limite=conta["limite"],
                numero_saques=conta["numero_saques"],
                limite_saques=conta["LIMITE_SAQUES"]
            )
        elif i == 3:
            mostrar_extrato(contas[0]["saldo"], extrato=contas[0]["extrato"])
        elif i == 4:
            cadastrar_usuario(usuarios)
        elif i == 5:
            nova_conta = abrir_conta(agencia, numero_conta + 1, usuarios)
            if nova_conta:
                contas.append(nova_conta)
                numero_conta += 1
        elif i == 6:
            listar_contas(contas)
        elif i == 0:
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada!")

if __name__ == "__main__":
    main()