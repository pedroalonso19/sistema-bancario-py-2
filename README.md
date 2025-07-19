# 💳 Sistema Bancário em Python

Este é um sistema bancário simples desenvolvido em Python para simular operações básicas como **depósitos**, **saques**, **emissão de extratos**, **cadastro de usuários** e **gerenciamento de contas**.

---

## 📋 Funcionalidades

- [x] Depósito em conta  
- [x] Saque com limite de valor e número de operações  
- [x] Emissão de extrato bancário  
- [x] Cadastro de novos usuários  
- [x] Criação de novas contas bancárias vinculadas a usuários  
- [x] Listagem de contas cadastradas  

---

## 🚀 Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Salve o código em um arquivo chamado `banco.py`.
3. No terminal, navegue até a pasta onde está o arquivo e execute:

```bash
python banco.py
```

---

## 🧠 Estrutura do Projeto

### Funções principais:

- `realizar_saque(...)`: Realiza saque com validação de saldo, limite e número de saques diários.
- `realizar_deposito(...)`: Permite depósitos com valor positivo.
- `mostrar_extrato(...)`: Exibe o extrato da conta e o saldo atual.
- `cadastrar_usuario(lista_usuarios)`: Registra um novo usuário com CPF único.
- `abrir_conta(agencia, numero, lista_usuarios)`: Cria uma nova conta bancária vinculada a um CPF existente.
- `listar_contas(contas)`: Exibe todas as contas bancárias registradas.

### Execução principal:

- O programa inicia com um menu interativo que permite ao usuário escolher entre as operações disponíveis.
- Uma conta padrão já é criada automaticamente para facilitar testes rápidos.

---

## 💡 Exemplo de Uso

```
========Digite a opção desejada=========
    1. Depósito
    2. Saque
    3. Extrato
    4. Criar usuário
    5. Criar conta
    6. Listar contas
    0. Sair
```

---

## 🛠 Tecnologias Utilizadas

- **Python 3.10+**
- Estruturas básicas de dados: listas e dicionários
- Modularização de funções
- Manipulação de entrada/saída no terminal

---

## 📌 Observações

- O número máximo de saques por conta é **3**.
- O valor máximo por saque é de **R$ 500,00**.
- O CPF deve ser único no sistema.
- A conta é criada apenas se o CPF já estiver cadastrado.

---

## 🧑‍💻 Autor

Pedro Alonso Ribeiro Ferreira da Silva  
Projeto desenvolvido para fins educacionais.

---

