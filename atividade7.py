#CLIENTE
print("=======Mercado101 Utilidades========")
print("Seja bem-vindo ao mercado101, aqui voce encontra tudo o que precisa para o seu dia a dia!")
#antes cadastro do cliente
nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
sexo = input("Digite seu sexo (Masculino/Feminino/Outro): ")
numero = input("Digite seu número de telefone: ")
cpf = input("Digite seu CPF: ")
#bloquear se colocar o cpf pequeno ou grande
while len(cpf) != 11:
    print("CPF inválido. O CPF deve conter exatamente 11 dígitos.")
    cpf = input("Digite seu CPF: ")
tentativas = 0
while tentativas < 3:
    cpf_input = input("Digite seu CPF para confirmar o cadastro: ")
    if cpf_input == cpf:
        print("Cadastro confirmado! Bem-vindo ao mercado101, ", nome)
        break
    else:
        tentativas += 1
        print(f"CPF incorreto. Você tem {3 - tentativas} tentativas restantes.")
 #Produto mais barato
precos = [10, 8, 5, 4, 15]
produto_mais_barato = min(precos)
print(f"O produto mais barato é: RS:{produto_mais_barato}")  

#produto mais caro
produto_mais_caro = max(precos)
print(f"O produto mais caro é: RS:{produto_mais_caro}")


#Produtos disponiveis
print("Produtos disponiveis:")
print("1. Arroz - RS10,00")
print("2. Feijão - RS8,00")
print("3. Macarrão - RS5,00")
print("4. Açúcar - RS4,00")
print("5. Café - RS15,00")
#codigo para escolher o produto
produto_escolhido = int(input("Digite o número do produto que deseja comprar: "))
if produto_escolhido == 1:
    print("Você escolheu Arroz - RS10,00")
elif produto_escolhido == 2:
    print("Você escolheu Feijão - RS8,00")      
elif produto_escolhido == 3:
    print("Você escolheu Macarrão - RS5,00")
elif produto_escolhido == 4:
    print("Você escolheu Açúcar - RS4,00")
elif produto_escolhido == 5:
    print("Você escolheu Café - RS15,00")
else:
    print("Produto inválido, por favor escolha um número de 1 a 5.")
#Quantos produtos deseja comprar
quantidade = int(input("Digite a quantidade que deseja comprar: "))
if produto_escolhido == 1:
    total = 10 * quantidade
    print(f"O total a pagar por {quantidade} unidades de Arroz é: RS{total}")   
elif produto_escolhido == 2:
    total = 8 * quantidade
    print(f"O total a pagar por {quantidade} unidades de Feijão é: RS{total}")
elif produto_escolhido == 3:
    total = 5 * quantidade
    print(f"O total a pagar por {quantidade} unidades de Macarrão é: RS{total}")
elif produto_escolhido == 4:
    total = 4 * quantidade
    print(f"O total a pagar por {quantidade} unidades de Açúcar é: RS{total}")
elif produto_escolhido == 5:
    total = 15 * quantidade
    print(f"O total a pagar por {quantidade} unidades de Café é: RS{total}")
else:
    print("Produto inválido, por favor escolha um número de 1 a 5.")

#Deseja Fazer o cartao da loja?
cartao = input("Deseja fazer o cartao da loja? (sim/nao): ").lower()
if cartao == "sim": 
    print("Parabéns! Você agora é um cliente VIP do mercado101 e tem acesso a descontos exclusivos!")
else:    print("Sem problemas! Você ainda pode aproveitar nossas ofertas e promoções regulares.")

#forma de pagamento
forma_pagamento = input("Escolha a forma de pagamento (dinheiro/cartao): ").lower()
if forma_pagamento == "dinheiro":
    print("Compra Realizada.")
    exit()


elif forma_pagamento == "cartao":
    print("Você escolheu pagar com cartão. Por favor, insira seu cartão e siga as instruções.") 
else:    print("Forma de pagamento inválida, por favor escolha entre dinheiro ou cartão.")
#SENHA CARTAO
senha_cartao = input("Digite a senha do seu cartão: ")
if senha_cartao == "1234":
    print("Senha correta! Sua compra foi aprovada.")    
#quando fizer a compra
print("Obrigado por comprar no mercado101! Esperamos vê-lo novamente em breve!")



 #sistema de vendas CLT
vendas = int(input("Digite o número de vendas realizadas hoje: "))
if vendas < 10:
    print("Hoje foi um dia tranquilo, mas temos certeza que amanhã será melhor!")
elif vendas < 20:
    print("Ótimo trabalho! Estamos vendo um aumento nas vendas, continue assim!")
elif vendas < 30:
    print("Excelente! As vendas estão crescendo rapidamente, parabéns!")
else:    print("Incrível! Vocês estão arrasando, as vendas estão em alta, continuem assim!")



 




    






