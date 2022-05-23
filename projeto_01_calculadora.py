import os

print("==========")
operacoes = {
    "+": "Soma",
    "-": "Subtração",
    "*": "Multiplicação",
    "/": "Divisão",
    "^": "Exponenciação"
}

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    i = 1
    for operacao, nome in operacoes.items():
        print(i, ": ", nome)
        i += 1
    operacao_escolhida = int(input("Escolha a operação que deseja realizar: "))
    operacao_escolhida_chave = list(operacoes.keys())[operacao_escolhida - 1]
    
    print(f"operação [{operacao_escolhida_chave}] escolhida.")

    valor_1 = float(input("Qual o primeiro valor? "))
    valor_2 = float(input("Qual o segundo valor? "))

    if operacao_escolhida == 1:
        resultado = valor_1	+ valor_2
    elif operacao_escolhida == 2:
        resultado = valor_1 - valor_2
    elif operacao_escolhida == 3:
        resultado = valor_1 * valor_2
    elif operacao_escolhida == 4:
        resultado = valor_1 / valor_2
    elif operacao_escolhida == 5:
        resultado = valor_1 ** valor_2
    
    print("==========")
    print(f"{valor_1} {operacao_escolhida_chave} {valor_2} = {resultado}")
    print("==========")

    sair = input("Deseja fazer mais alguma operação? (Digite 0 para sair ou qualquer outra tecla para continuar): ")

    if sair == "0":
        print("Obrigado e até mais!")
        break

