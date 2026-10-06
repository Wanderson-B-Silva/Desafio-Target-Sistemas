import json

# Abre e lê o arquivo JSON
with open("vendas.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

# Dicionário que vai guardar a comissão total de cada vendedor
comissoes = {}

# Percorre todas as vendas
for venda in dados["vendas"]:
    vendedor = venda["vendedor"]
    valor = venda["valor"]

    # Calcula a comissão desta venda
    if valor < 100:
        comissao = 0

    elif valor < 500:
        comissao = valor * 0.01

    else:
        comissao = valor * 0.05

    # Se o vendedor ainda não estiver no dicionário,
    # começa sua comissão com zero
    if vendedor not in comissoes:
        comissoes[vendedor] = 0

    # Soma a comissão desta venda ao total do vendedor
    comissoes[vendedor] += comissao


# Exibe o resultado
print("COMISSÕES DOS VENDEDORES")
print("------------------------")

for vendedor, comissao in comissoes.items():
    print(f"{vendedor}: R$ {comissao:.2f}")