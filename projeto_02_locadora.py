import os

carros_disponiveis = [
    ("Fiat Mobi", 50),
    ("Fiat Argo", 60),
    ("Fiat Uno", 60),
    ("Chevrolet Onix", 60),
    ("Nissan Versa", 90),
    ("Nissan HB20S", 90),
    ("Chevrolet Spin", 140),
    ("Fiat Cronos", 190),
    ("Chevrolet Voyage", 190),
    ("Toyota Corolla Cross", 300)
]

carros_alugados = []

def mostrar_lista_de_carros(lista_de_carros):
    for i, carro in enumerate(lista_de_carros):
        print(f"[{i + 1}] {carro[0]} - R$ {carro[1]} / dia")

def mostrar_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=============================")
    print("Bem-vindo à locadora de carro")
    print("=============================")
    print("")
    print("O que você deseja fazer?")
    print("""
    1 - Mostrar portifólio
    2 - Alugar um carro
    3 - Devolver um carro
    """)

while True:
    mostrar_menu()
    opcao_escolhida = int(input())

    if opcao_escolhida == 1:
        mostrar_lista_de_carros(carros_disponiveis)

    elif opcao_escolhida == 2:
        mostrar_lista_de_carros(carros_disponiveis)

        print("Escolha o código do carro:")
        codigo_carro = int(input())

        print("Por quantos dias você deseja alugar esse carro?")
        dias = int(input())

        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"Você escolheu {carros_disponiveis[codigo_carro - 1][0]} por {dias} dias.")
        print(f"O aluguel totalizaria R$ {dias * carros_disponiveis[codigo_carro - 1][1]}.")
        print("Deseja alugar?")
        print("S - Sim | N - Não")

        aluga = input().upper()

        if aluga == "S":
            print(f"Parabéns! Você alugou o {carros_disponiveis[codigo_carro - 1][0]} por {dias} dias")
            carros_alugados.append(carros_disponiveis.pop(codigo_carro - 1))

    elif opcao_escolhida == 3:
        if len(carros_alugados) == 0:
            print("Não há carros para devolver.")
        else:
            print("Qual dos carros abaixo você deseja devolver? ")
            mostrar_lista_de_carros(carros_alugados)
            print("")
            print("Escolha o código do carro que deseja devolver:")
            codigo_carro_devolvido = int(input())
            carros_disponiveis.append(carros_alugados.pop(codigo_carro_devolvido - 1))

            os.system('cls' if os.name == 'nt' else 'clear')
            print("Carros disponíveis agora:")
            mostrar_lista_de_carros(carros_disponiveis)
    
    print("")
    print("=========================")
    print("Digite 1 para continuar ou 0 para sair")
    if int(input()) == 0:
        break

