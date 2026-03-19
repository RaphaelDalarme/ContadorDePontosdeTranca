print("""
====================== Bem-Vindos ao Pontuador de Tranca ======================
""")

maxJogadores = 3 
numJogadores = 0 

while numJogadores < 1 or numJogadores > maxJogadores:
    try:
        numJogadores = int(input(f"Quantos jogadores vão jogar essa partida? (Máximo = 3) jogadores: "))
        if numJogadores < 1 or numJogadores > maxJogadores:
            print(f"ERRO! Escolha um número entre 1 e {maxJogadores}.")
    except ValueError:
        print("Por favor, digite apenas número inteiros.")

participantes = []
contador = 0 

while contador < numJogadores:
    nome = input(f"Digite o nome do jogador {contador + 1}: ")
    participantes.append(nome)
    contador += 1

pontuacao = {}
for nome in participantes:
    pontuacao[nome] = 0 

jogoAtivo = True
while jogoAtivo:
    print("\n--- Nova Rodada ---")

    jogadoresDaRodada = list(participantes)
    for nome in jogadoresDaRodada:
        print(f"\nJogador: {nome} (Pontuação atual: {pontuacao[nome]})")

        try:
            pontosRodada = int(input(f"Quantos pontos {nome} fez nessa rodada? "))
            pontuacao[nome] += pontosRodada
            print(f"Total de {nome}: {pontuacao[nome]} pontos.")
            jogoAtivo = True
        except ValueError:
            print("ERRO! Digite um valor numérico para os pontos.")

    continuar = input("\nDeseja lançar mais uma rodada? (Digite 'sair' para encerrar ou qualquer tecla para continuar): ").lower()

    if continuar == "sair":
        jogoAtivo = False

print("\n" + "X"*30)
print("       RESULTADO FINAL       ")
print("X"*30)

vencedor = max(pontuacao, key=pontuacao.get)
maior_ponto = pontuacao[vencedor]

print("\nPlacar Geral:")
for nome, pontos in pontuacao.items():
    print(f"- {nome}: {pontos} pontos")

print(f"\n🏆 O GRANDE VENCEDOR É: {vencedor} com {maior_ponto} pontos!")
print("===============================================================")

