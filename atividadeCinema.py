# =========================
# SISTEMA DE CINEMA
# =========================

# Valor do ingresso
valor_ingresso = 20


# =========================
# MENU
# =========================

def menu():

    print("\n===== CINEMA =====")

    print("1 - Vingadores")
    print("2 - Batman")
    print("3 - Homem-Aranha")


# =========================
# ESCOLHER FILME
# =========================

def escolher_filme():

    opcao = input("Escolha um filme: ")

    if opcao == "1":
        return "Vingadores"

    elif opcao == "2":
        return "Batman"

    elif opcao == "3":
        return "Homem-Aranha"

    else:
        print("Filme inválido.")
        return escolher_filme()


# =========================
# CALCULAR VALOR
# =========================

def calcular_valor(quantidade):

    total = quantidade * valor_ingresso

    return total


# =========================
# PAGAMENTO
# =========================

def pagamento():

    print("\n===== PAGAMENTO =====")

    print("1 - Pix")
    print("2 - Cartão")
    print("3 - Dinheiro")

    opcao = input("Escolha a forma de pagamento: ")

    if opcao == "1":
        return "Pix"

    elif opcao == "2":
        return "Cartão"

    elif opcao == "3":
        return "Dinheiro"

    else:
        print("Opção inválida.")
        return pagamento()


# =========================
# FINALIZAR COMPRA
# =========================

def finalizar_compra(nome, filme, quantidade, total, forma_pagamento):

    print("\n===== COMPRA FINALIZADA =====")

    print("Cliente:", nome)

    print("Filme:", filme)

    print("Quantidade de ingressos:", quantidade)

    print("Valor total: R$", total)

    print("Pagamento:", forma_pagamento)

    print("\nCompra realizada com sucesso!")


# =========================
# PROGRAMA PRINCIPAL
# =========================

print("===== BEM-VINDO AO CINEMA =====")

nome = input("Digite seu nome: ")

menu()

filme = escolher_filme()

quantidade = int(input("Quantidade de ingressos: "))

total = calcular_valor(quantidade)

print("Valor total da compra: R$", total)

forma_pagamento = pagamento()

finalizar_compra(
    nome,
    filme,
    quantidade,
    total,
    forma_pagamento
)