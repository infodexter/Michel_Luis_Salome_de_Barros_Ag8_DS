print("========================================")
print("       PESQUISA DE SATISFAÇÃO")
print("             TudoWeb")
print("========================================")

excelente = 0
ruim = 0

for entrevistado in range(1, 11):

    print(f"\n--- Entrevistado {entrevistado} ---")

    nome = input("Nome: ")
    idade = int(input("Idade: "))

    print("\nOpinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opção: "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        pass
    elif opiniao == 3:
        ruim += 1
    else:
        print("Opção inválida.")

print("\n========================================")
print("       RESULTADO DA PESQUISA")
print("========================================")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")
print("========================================")
