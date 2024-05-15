def calcular_preco_total(produto, quantidade):
    """
    """
    if produto in tabela:
        return tabela[produto] * quantidade
    else:
        print("Produto não encontrado na tabela.")
        return 0

tabela = { 
    "Arroz": 25.00,
    "Feijão": 9.90,
    "Batata": 6.00,
    "Alface": 5.00,
    "Picanha": 80.00,
    "Coca cola": 10.00,
    "Granola": 30.00,
    "Banana" : 6.00,
    "Barra de chocolate" : 10.00,
    "Açai": 20.00,
    "Pipoca": 3.00,
    "Corote": 5.00,
    "Heineken": 7.00,
    "Detergente": 2.49,
    "Pão Francês": 15.00,
    "Manteiga": 25.00,
    "Azeite": 40.00,
    "Oleo de Soja": 5.00,
    "Laranja": 5.00,
    "Queijo Prato": 60.00,
    "Morango": 15.00,
    "Amaciante": 25.00
}

valor_total = 0

while True: 
    produto = input("Qual o produto escolhido? ").capitalize()
    
    if produto == "Finalizar compra":
    
        print("Compra finalizada!")
        break
        
    quantidade = int(input("Quantidade: "))
    preco_produto = calcular_preco_total(produto, quantidade)
    valor_total += preco_produto
    print(f"O preço de {quantidade} {produto}(s) é R${preco_produto:.2f}")

print(f"O valor total da compra foi de: R${valor_total:.2f}")