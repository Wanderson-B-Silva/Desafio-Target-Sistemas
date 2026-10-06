import json

import os

pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_json = os.path.join(pasta_atual, "estoque.json")


with open(caminho_json, "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

# Guarda as movimentações realizadas
movimentacoes = []

# Número inicial da movimentação
proximo_id = 1


while True:

    print("\n===== CONTROLE DE ESTOQUE =====")

    # Mostra os produtos
    for produto in dados["estoque"]:
        print(
            f'Código: {produto["codigoProduto"]} | '
            f'{produto["descricaoProduto"]} | '
            f'Estoque: {produto["estoque"]}'
        )

    codigo = int(input("\nDigite o código do produto: "))

    produto_encontrado = None

    # Procura o produto informado
    for produto in dados["estoque"]:

        if produto["codigoProduto"] == codigo:
            produto_encontrado = produto
            break


    # Verifica se o produto existe
    if produto_encontrado is None:
        print("Produto não encontrado.")
        continue


    print("\n1 - Entrada")
    print("2 - Saída")

    tipo = int(input("Digite o tipo da movimentação: "))

    quantidade = int(input("Digite a quantidade: "))


    # Entrada
    if tipo == 1:

        produto_encontrado["estoque"] += quantidade
        descricao = "Entrada de mercadoria"


    # Saída
    elif tipo == 2:

        # Evita estoque negativo
        if quantidade > produto_encontrado["estoque"]:
            print("Erro: quantidade maior que o estoque disponível.")
            continue

        produto_encontrado["estoque"] -= quantidade
        descricao = "Saída de mercadoria"


    else:
        print("Tipo de movimentação inválido.")
        continue


    # Cria o registro da movimentação
    movimentacao = {

        "id": proximo_id,

        "descricao": descricao,

        "codigoProduto": produto_encontrado["codigoProduto"],

        "produto": produto_encontrado["descricaoProduto"],

        "quantidade": quantidade,

        "estoqueFinal": produto_encontrado["estoque"]
    }


    movimentacoes.append(movimentacao)

    # Aumenta o número para a próxima movimentação
    proximo_id += 1


    print("\nMovimentação realizada com sucesso!")

    print(
        f'Estoque final de '
        f'{produto_encontrado["descricaoProduto"]}: '
        f'{produto_encontrado["estoque"]}'
    )


    continuar = input("\nDeseja realizar outra movimentação? (s/n): ")

    if continuar.lower() != "s":
        break


# Salva o estoque atualizado no JSON
with open("estoque.json", "w", encoding="utf-8") as arquivo:

    json.dump(
        dados,
        arquivo,
        indent=4,
        ensure_ascii=False
    )


print("\n===== MOVIMENTAÇÕES REALIZADAS =====")

for movimentacao in movimentacoes:
    print(movimentacao)