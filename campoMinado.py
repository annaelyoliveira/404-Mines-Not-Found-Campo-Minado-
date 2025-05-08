import random

def criar_tabuleiro(tamanho=8):
    # Cria um tabuleiro vazio
    return [[0 for _ in range(tamanho)] for _ in range(tamanho)]

def colocar_minas(tabuleiro, num_minas=10):
    # Coloca minas aleatoriamente no tabuleiro 
    tamanho = len(tabuleiro)
    minas_colocadas = 0
    
    while minas_colocadas < num_minas:
        x, y = random.randint(0, tamanho-1), random.randint(0, tamanho-1)
        if tabuleiro[x][y] != -1:  # -1 representa uma mina
            tabuleiro[x][y] = -1
            minas_colocadas += 1

def calcular_vizinhos(tabuleiro):
    # Calcula quantas minas existem ao redor de cada célula
    tamanho = len(tabuleiro)
    
    for x in range(tamanho):
        for y in range(tamanho):
            if tabuleiro[x][y] == -1:
                continue  # Pula as minas
            
            contagem = 0
            # Verifica todas as células ao redor (que é uma matriz 3x3)
            for i in range(max(0, x-1), min(tamanho, x+2)):
                for j in range(max(0, y-1), min(tamanho, y+2)):
                    if tabuleiro[i][j] == -1:
                        contagem += 1
            tabuleiro[x][y] = contagem

def revelar_celula(tabuleiro, visivel, x, y):
    # Revela uma célula e suas vizinhas se for vazia
    tamanho = len(tabuleiro)
    
    # Verifica se a célula está dentro do tabuleiro
    if x < 0 or x >= tamanho or y < 0 or y >= tamanho:
        return False
    
    # Se já está visível, não faz nada
    if visivel[x][y]:
        return True
    
    # Marca como visível
    visivel[x][y] = True
    
    # Se é uma mina, fim de jogo
    if tabuleiro[x][y] == -1:
        return False
    
    # Se é vazio (0), revela os vizinhos
    if tabuleiro[x][y] == 0:
        for i in range(max(0, x-1), min(tamanho, x+2)):
            for j in range(max(0, y-1), min(tamanho, y+2)):
                if not (i == x and j == y):  # Não revela a si mesma novamente
                    revelar_celula(tabuleiro, visivel, i, j)
    
    return True

def mostrar_todas_minas(tabuleiro, visivel):
    # Mostra todas as minas no tabuleiro (quando o jogador perde)
    tamanho = len(tabuleiro)
    for x in range(tamanho):
        for y in range(tamanho):
            if tabuleiro[x][y] == -1:
                visivel[x][y] = True

def verificar_vitoria(tabuleiro, visivel):
    # Verifica se o jogador revelou todas as células sem minas
    tamanho = len(tabuleiro)
    for x in range(tamanho):
        for y in range(tamanho):
            if tabuleiro[x][y] != -1 and not visivel[x][y]:
                return False
    return True

def imprimir_tabuleiro(tabuleiro, visivel):

    # Imprime o tabuleiro atual
    tamanho = len(tabuleiro)
    
    print("\n   " + " ".join(str(i).rjust(2) for i in range(tamanho)))
    print("  " + "─" * (tamanho * 3 + 1))

    
    for x in range(tamanho):
        print(f"{x} |", end="")
        for y in range(tamanho):
            if not visivel[x][y]:
                print(" ■ ", end="")  # Célula não revelada
            elif tabuleiro[x][y] == -1:
                print(" 💣 ", end="")  # Mina
            else:
                valor = tabuleiro[x][y] if tabuleiro[x][y] > 0 else " "
                print(f" {valor} ", end="")  # Número ou espaço vazio
        print()

def jogar_campo_minado(tamanho=8, num_minas=10):
    # Função principal que controla o jogo

    # Inicializa o tabuleiro e o que está visível
    tabuleiro = criar_tabuleiro(tamanho)
    visivel = [[False for _ in range(tamanho)] for _ in range(tamanho)]
    jogo_terminado = False
    
    # Configura o tabuleiro
    colocar_minas(tabuleiro, num_minas)
    calcular_vizinhos(tabuleiro)
    
    print("\nBem vindo ao 404 Mines Not Found 💣🥶 PREPARE-SE PARA JOGAR!")
    print(f"Tabuleiro: {tamanho}x{tamanho} com {num_minas} minas")
    print("Digite as coordenadas (linha coluna) para revelar uma célula")
    print("Exemplo: '3 4' para revelar a célula na linha 3, coluna 4")
    print("\n                 GAME ON 🕹️ ")
    
    while not jogo_terminado:
        imprimir_tabuleiro(tabuleiro, visivel)
        
        try:
            entrada = input("Digite as coordenadas (linha coluna): ").split()
            
            if len(entrada) != 2:
                print("Entrada inválida! Digite duas coordenadas separadas por espaço.")
                continue
            
            x, y = map(int, entrada)
            
            if x < 0 or x >= tamanho or y < 0 or y >= tamanho:
                print(f"Coordenadas devem estar entre 0 e {tamanho-1}.")
                continue
            
            # Revela a célula
            if not revelar_celula(tabuleiro, visivel, x, y):
                mostrar_todas_minas(tabuleiro, visivel)
                imprimir_tabuleiro(tabuleiro, visivel)
                print("\n💥BOOMM💥! Você perdeu. Pisou em uma mina. Fim de jogo!")
                break
            
            # Verifica se ganhou
            if verificar_vitoria(tabuleiro, visivel):
                imprimir_tabuleiro(tabuleiro, visivel)
                print("\n😎 Parabéns! Você venceu! Desarmou todas as minas 🎉")
                break
        
        except ValueError:
            print("Entrada inválida! Digite números inteiros para as coordenadas.")


# Menu principal 
def menu_principal():
    vitorias = 0
    
    while True:
        print("\n      404 MINES NOT FOUND 💣🥶")
        print("\n1. Jogar Campo Minado")
        print("2. Sair do programa")
        print("3. Mostrar quantidade de vitórias")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            resultado = jogar_campo_minado()
            if resultado:
                vitorias += 1
                print(f"Vitórias totais: {vitorias}")
        elif opcao == "2":
            print("Obrigado por jogar! Até mais!")
            break
        elif opcao == "3":
            print(f"\nVocê tem {vitorias} vitória(s) até agora!")
        else:
            print("Opção inválida! Por favor, escolha 1, 2 ou 3.")

# Inicia o jogo
if __name__ == "__main__":
    menu_principal()