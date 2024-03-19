import random
import os

class JogoDaVelha:
    VITORIA_COMBINACOES = [
        ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],  # Horizontais
        ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],  # Verticais
        ['1', '5', '9'], ['3', '5', '7']  # Diagonais
    ]
    VAZIO = ' '

    def __init__(self):
        print("Bem vindo ao jogo da velha!")
        self.nome_jogador_1 = input("Nome do Jogador 1: ")
        self.simbolo_jogador_1 = 'X'
        self.nome_jogador_2 = input("Nome do Jogador 2: ")
        self.simbolo_jogador_2 = 'O'

        jogador_inicial = random.choice([self.nome_jogador_1, self.nome_jogador_2])  # Para Escolher aleatoriamente quem começa
        self.turno = jogador_inicial
        print(f"{self.turno} ({'X' if self.turno == self.nome_jogador_1 else 'O'}) começa.")

        self.tabuleiro = {str(i): self.VAZIO for i in range(1, 10)}

    def exibir_tabuleiro(self):
        print(f" {self.tabuleiro['1']} │ {self.tabuleiro['2']} │ {self.tabuleiro['3']} ")
        print("───┼───┼───")
        print(f" {self.tabuleiro['4']} │ {self.tabuleiro['5']} │ {self.tabuleiro['6']} ")
        print("───┼───┼───")
        print(f" {self.tabuleiro['7']} │ {self.tabuleiro['8']} │ {self.tabuleiro['9']} ")

    def verificar_ganhador(self):
        for combinacao in self.VITORIA_COMBINACOES:
            if self.tabuleiro[combinacao[0]] == self.tabuleiro[combinacao[1]] == self.tabuleiro[combinacao[2]] != self.VAZIO:
                return self.tabuleiro[combinacao[0]]

        if self.VAZIO not in self.tabuleiro.values():
            return "empate"

        return None

    def jogar(self):
        while True:
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

            self.exibir_tabuleiro()
            print(f"{self.turno} - escolha sua jogada entre 1-9:")
            jogada = input("Jogada: ")

            if self.tabuleiro.get(jogada) == self.VAZIO:
                self.tabuleiro[jogada] = self.simbolo_jogador_1 if self.turno == self.nome_jogador_1 else self.simbolo_jogador_2
                ganhador = self.verificar_ganhador()

                if ganhador:
                    if ganhador == "empate":
                        print("EMPATE!!!")
                    else:
                        print(f"{self.turno} ({self.simbolo_jogador_1 if self.turno == self.nome_jogador_1 else self.simbolo_jogador_2}) é o vencedor!!!")
                    break
                else:
                    self.turno = self.nome_jogador_1 if self.turno == self.nome_jogador_2 else self.nome_jogador_2
            else:
                print(f"Jogada inválida, {jogada} já foi realizada ou não é uma posição válida.")

        self.exibir_tabuleiro()


jogo = JogoDaVelha()
jogo.jogar()