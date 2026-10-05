import json 
from collections import defaultdict
dados_json = '''
{
  "estoque": [
    {
      "codigoProduto": 101,
      "descricaoProduto": "Caneta Azul",
      "estoque": 150
    },
    {
      "codigoProduto": 102,
      "descricaoProduto": "Caderno Universitário",
      "estoque": 75
    },
    {
      "codigoProduto": 103,
      "descricaoProduto": "Borracha Branca",
      "estoque": 200
    },
    {
      "codigoProduto": 104,
      "descricaoProduto": "Lápis Preto HB",
      "estoque": 320
    },
    {
      "codigoProduto": 105,
      "descricaoProduto": "Marcador de Texto Amarelo",
      "estoque": 90
    }
  ]
}
'''
dados = json.loads(dados_json)

print("Sistema do Estoque. Esses são os produtos disponíveis:\n")
for produto in dados['estoque']:
    print(f"Código: {produto['codigoProduto']}, Descrição: {produto['descricaoProduto']}, Estoque: {produto['estoque']}")
print("\n")
acao = int(input("O que você deseja fazer? Digite 1 para entrada de produtos ou digite 2 para saída de produtos.\n"))
produto_codigo = int(input("Digite o código do produto que deseja movimentar:\n"))
quantidade = int(input("Digite a quantidade que deseja movimentar:\n"))

produto_encontrado = None
for produto in dados['estoque']:
    if produto['codigoProduto'] == produto_codigo:
        produto_encontrado = produto
        break
if produto_encontrado is None:
    print("Produto não encontrado!")

else:
    if acao == 1:  
        produto_encontrado['estoque'] += quantidade
        print(f"Entrada realizada. Novo estoque: {produto_encontrado['estoque']}")
    elif acao == 2: 
        if produto_encontrado['estoque'] >= quantidade:
            produto_encontrado['estoque'] -= quantidade
            print(f"Saída realizada. Novo estoque: {produto_encontrado['estoque']}")
        else:
            print(f"Estoque insuficiente! Disponível: {produto_encontrado['estoque']}")
    else:
        print("Ação inválida!")

with open('estoque.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)

print("\nEstoque atualizado:")
for produto in dados['estoque']:
  print(f"Código: {produto['codigoProduto']}, Descrição: {produto['descricaoProduto']}, Estoque: {produto['estoque']}")