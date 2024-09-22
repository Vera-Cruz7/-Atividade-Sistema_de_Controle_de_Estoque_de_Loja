# Sistema de Controle de Estoque de Loja

# Lista para armazenar os produtos
estoque = []
vendas_totais = 0.0

# Função para adicionar produtos ao estoque
def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade disponível: "))
    preco = float(input("Digite o preço por unidade: "))
    
    produto = {
        'nome': nome,
        'quantidade': quantidade,
        'preco': preco
    }
    estoque.append(produto)
    print(f"\nProduto {nome} adicionado ao estoque!\n")

# Função para registrar uma venda
def registrar_venda():
    global vendas_totais
    nome_produto = input("Digite o nome do produto vendido: ")
    
    for produto in estoque:
        if produto['nome'].lower() == nome_produto.lower():
            quantidade_venda = int(input("Digite a quantidade vendida: "))
            
            if quantidade_venda > produto['quantidade']:
                print("\nErro: Quantidade insuficiente no estoque!\n")
            else:
                produto['quantidade'] -= quantidade_venda
                valor_venda = quantidade_venda * produto['preco']
                vendas_totais += valor_venda
                print(f"\nVenda registrada com sucesso! Valor da venda: R${valor_venda:.2f}\n")
            return
    
    print("\nErro: Produto não encontrado no estoque!\n")

# Função para gerar relatórios
def gerar_relatorio():
    print("\nRelatório de Estoque:")
    if not estoque:
        print("Estoque vazio.\n")
    else:
        for produto in estoque:
            print(f"Produto: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço por unidade: R${produto['preco']:.2f}")
    
    print(f"\nValor total das vendas realizadas: R${vendas_totais:.2f}\n")

# Função principal para o menu e controle do sistema
def menu():
    while True:
        print("=== Sistema de Controle de Estoque ===")
        print("1. Adicionar Produto ao Estoque")
        print("2. Registrar Venda")
        print("3. Gerar Relatório de Estoque e Vendas")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            registrar_venda()
        elif opcao == '3':
            gerar_relatorio()
        elif opcao == '4':
            print("\nSaindo do sistema...\n")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")

# Executar o programa
menu()
