# ==========================================
# SISTEMA DE GESTÃO DE ESTOQUE E COMPRAS
# ==========================================

from funcoes_cpl_estoque import (
    _get_estoque, _painel_inicial, _mostrar_estoque, _adding_to_cart_section,
    _my_cart, _create_item
)

# Base de dados (Escopo global do script)
estoque = _get_estoque()

carrinho = []
taxa_imposto_padrao = 0.05  # 5% de taxa padrão

executando = True

while executando:
    # --- Exibição do Menu Principal ---
    opcao = _painel_inicial()

    # --- Opção 1: Listar Produtos ---
    if opcao == "1":
        _mostrar_estoque(estoque)

    # --- Opção 2: Adicionar Produto ao Carrinho ---
    elif opcao == "2":
        _adding_to_cart_section(estoque, carrinho)

    # --- Opção 3: Exibir Carrinho e Calcular Total ---
    elif opcao == "3":
        _my_cart(taxa_imposto_padrao, carrinho)

    # --- Opção 4: Cadastrar Novo Produto ---
    elif opcao == "4":
        estoque = _create_item(estoque) 
        
    # --- Opção 0: Sair ---
    elif opcao == "0":
        print("\nEncerrando o sistema. Até logo!")
        executando = False

    else:
        print("\nOpção inválida! Tente novamente.")