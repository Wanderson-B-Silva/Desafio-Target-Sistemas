from datetime import datetime, date


# Recebe o valor
valor = float(input("Digite o valor da conta: R$ "))

# Recebe a data como texto
data_texto = input("Digite a data de vencimento (dd/mm/aaaa): ")

# Converte o texto para uma data
data_vencimento = datetime.strptime(
    data_texto,
    "%d/%m/%Y"
).date()

# Obtém a data atual
data_atual = date.today()


# Verifica se a conta está atrasada
if data_atual > data_vencimento:

    # Calcula quantos dias está atrasada
    dias_atraso = (data_atual - data_vencimento).days

    # 2,5% = 0,025
    taxa = 0.025

    # Calcula os juros
    juros = valor * taxa * dias_atraso

    # Valor original + juros
    valor_total = valor + juros


    print("\n===== RESULTADO =====")

    print(f"Dias de atraso: {dias_atraso}")

    print(f"Valor original: R$ {valor:.2f}")

    print(f"Juros: R$ {juros:.2f}")

    print(f"Valor total: R$ {valor_total:.2f}")


else:

    print("\nA conta ainda não está vencida.")

    print(f"Valor a pagar: R$ {valor:.2f}")