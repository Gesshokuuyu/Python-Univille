def _get_estoque():
    return [
        {"id": 1, "nome": "Notebook", "preco": 3500.0, "qtd": 5},
        {"id": 2, "nome": "Mouse", "preco": 80.0, "qtd": 15},
        {"id": 3, "nome": "Teclado", "preco": 150.0, "qtd": 10}
    ]

def _painel_inicial():
    print("\n" + "=" * 30)
    print("      SISTEMA DE ESTOQUE      ")
    print("=" * 30)
    print("1. Listar Produtos")
    print("2. Adicionar ao Carrinho")
    print("3. Exibir Carrinho e Total")
    print("4. Cadastrar Novo Produto")
    print("0. Sair")

    return input("\nEscolha uma opção: ").strip()


def _mostrar_estoque(estoque):
    print("\n--- PRODUTOS DISPONÍVEIS ---")
    if not estoque:
        print("Estoque vazio.")
    else:
        for item in estoque:
            _show_item_info(item)
            
def _show_item_info(item):
    print(f"ID: {item['id']} | Nome: {item['nome']} | Preço: R$ {item['preco']:.2f} | Estq: {item['qtd']}")

def _adding_to_cart_section(estoque, carrinho):
    print("\n--- ADICIONAR AO CARRINHO ---")
    id_busca = input("Digite o ID do produto: ")
    
    # Validação simples se é número
    if id_busca.isdigit():
        produto_encontrado = _search_item(id_busca, estoque)
        
        if produto_encontrado:
            _show_adding_item_cart_form(produto_encontrado, carrinho)
        else:
            print("Erro: Produto não encontrado.")
    else:
        print("Erro: ID deve ser um número inteiro.")


def _search_item(id_busca, estoque):

    id_busca = int(id_busca)
    produto_encontrado = None
    
    # Busca manual no estoque
    for item in estoque:
        if item["id"] == id_busca:
            produto_encontrado = item
            break
    return produto_encontrado

def _show_adding_item_cart_form(item_cadastro, carrinho ):

    qtd_desejada = input(f"Quantidade desejada de '{item_cadastro['nome']}': ")

    if qtd_desejada.isdigit():
        qtd_desejada = int(qtd_desejada)

        if qtd_desejada > 0 and qtd_desejada <= item_cadastro["qtd"]:
            # Atualiza estoque e adiciona ao carrinho
            item_cadastro["qtd"] -= qtd_desejada

            # Verifica se já está no carrinho para somar a quantidade
            no_carrinho = False
            for item_c in carrinho:
                if item_c["id"] == item_cadastro["id"]:
                    item_c["qtd"] += qtd_desejada
                    no_carrinho = True
                    break
                
            if not no_carrinho:
                carrinho.append({
                    "id": item_cadastro["id"],
                    "nome": item_cadastro["nome"],
                    "preco": item_cadastro["preco"],
                    "qtd": qtd_desejada
                })

            print(f"Sucesso: {qtd_desejada}x '{item_cadastro['nome']}' adicionado(s) ao carrinho!")
        else:
            print("Erro: Quantidade indisponível no estoque.")
    else:
        print("Erro: Quantidade inválida.")


def _my_cart(taxa_imposto_padrao, carrinho):

    print("\n--- SEU CARRINHO ---")
    if not carrinho:
        print("O carrinho está vazio.")
    else:
        subtotal = _get_total_carrinho(carrinho)
        
        # Pergunta se deseja aplicar taxa customizada ou usar a padrão (Ideal para parâmetro default)
        aplicar_taxa = input("\nDeseja aplicar taxa de entrega/serviço customizada? (S/N): ").strip().lower()
        
        taxa_aplicada = _get_taxa_aplicada(aplicar_taxa, taxa_imposto_padrao)
        
        total_final, valor_imposto = _calcula_total_final(subtotal, taxa_aplicada)

        _mostra_valores_finais_cart(subtotal, taxa_aplicada, valor_imposto, total_final)
        
        

def _get_total_carrinho(carrinho):
    subtotal = 0.0
    for item in carrinho:
        total_item = item["preco"] * item["qtd"]
        subtotal += total_item
        print(f"- {item['nome']} (x{item['qtd']}): R$ {total_item:.2f}")
    return subtotal

def _get_taxa_aplicada(aplicar, taxa_padrao):
    taxa_aplicada = taxa_padrao
    if aplicar == 's':
        val_taxa = input("Digite a taxa decimal (ex: 0.10 para 10%): ")
        try:
            taxa_aplicada = float(val_taxa)
        except ValueError:
            print("Valor inválido. Mantendo taxa padrão de 5%.")

    return taxa_aplicada

def _calcula_total_final(subtotal, taxa_aplicada):
    valor_imposto = subtotal * taxa_aplicada
    total_final = subtotal + valor_imposto

    return [total_final, valor_imposto]

def _mostra_valores_finais_cart(subtotal, taxa_aplicada, valor_imposto, total_final):
    print("-" * 30)
    print(f"Subtotal: R$ {subtotal:.2f}")
    print(f"Taxa ({taxa_aplicada * 100:.1f}%): R$ {valor_imposto:.2f}")
    print(f"TOTAL FINAL: R$ {total_final:.2f}")

def _create_item(estoque):
    print("\n--- CADASTRO DE PRODUTO ---")
    nome_novo = input("Nome do produto: ").strip()
    preco_novo = input("Preço do produto: ")
    qtd_nova = input("Quantidade inicial em estoque: ")

    try:
        preco_novo = float(preco_novo)
        qtd_nova = int(qtd_nova)

        if nome_novo and preco_novo > 0 and qtd_nova >= 0:
            # Gerar ID automático
            novo_id = 1
            if estoque:
                novo_id = max(item["id"] for item in estoque) + 1

            estoque.append({
                "id": novo_id,
                "nome": nome_novo,
                "preco": preco_novo,
                "qtd": qtd_nova
            })
            print(f"Produto '{nome_novo}' cadastrado com sucesso! ID: {novo_id}")

            return estoque
        else:
            print("Erro: Dados inválidos para o produto.")
    except ValueError:
        print("Erro: Preço e Quantidade devem ser numéricos.")