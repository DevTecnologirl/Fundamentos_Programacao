def imprimir_tabuleiro(tabuleiro):
    print()
    for i in range(3):
        linha = ""
        for j in range(3):
            if tabuleiro[i][j] == "":
                linha += "   "
            else:
                linha += f" {tabuleiro[i][j]} "
            if j < 2:
                linha += "|"
        print(linha)
        if i < 2:
            print("---+---+---")
    print()


def verificar_vitoria(tabuleiro, jogador):
    # Checar linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True
    # Checar colunas
    for j in range(3):
        if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j] == jogador:
            return True
    # Checar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False


def tabuleiro_cheio(tabuleiro):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == "":
                return False
    return True


def jogar():
    placar = {"X": 0, "O": 0, "Empates": 0, "Partidas": 0}

    while True:
        # Criar tabuleiro vazio
        tabuleiro = [["", "", ""], ["", "", ""], ["", "", ""]]
        jogador_atual = "X"
        vencedor = None

        print("\n--- Novo jogo da velha ---")
        imprimir_tabuleiro(tabuleiro)

        while True:
            # Perguntar jogada
            try:
                posicao = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): "))
                if posicao < 1 or posicao > 9:
                    print("Posição inválida! Escolha de 1 a 9.")
                    continue
            except ValueError:
                print("Digite um número válido!")
                continue

            linha = (posicao - 1) // 3
            coluna = (posicao - 1) % 3

            # Verificar se a posição está livre
            if tabuleiro[linha][coluna] != "":
                print("Essa posição já está ocupada! Tente de novo.")
                continue

            # Marcar jogada
            tabuleiro[linha][coluna] = jogador_atual
            imprimir_tabuleiro(tabuleiro)

            # Verificar vitória
            if verificar_vitoria(tabuleiro, jogador_atual):
                print(f"Jogador {jogador_atual} venceu!")
                vencedor = jogador_atual
                break

            # Verificar empate
            if tabuleiro_cheio(tabuleiro):
                print("Empate!")
                break

            # Trocar jogador
            jogador_atual = "O" if jogador_atual == "X" else "X"

        # Atualizar placar
        placar["Partidas"] += 1
        if vencedor:
            placar[vencedor] += 1
        else:
            placar["Empates"] += 1

        # Mostrar placar
        print("\n Placar:")
        print(f"Partidas: {placar['Partidas']}")
        print(f"Vitórias X: {placar['X']}")
        print(f"Vitórias O: {placar['O']}")
        print(f"Empates: {placar['Empates']}")

        # Perguntar se querem jogar novamente
        jogar_novamente = input("\nDesejam jogar novamente? (s/n): ").lower()
        if jogar_novamente != "s":
            print("Obrigado por jogar!")
            break


# Executar o jogo
jogar()
