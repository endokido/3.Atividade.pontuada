import os
import time
from dataclasses import dataclass

# Definição da Classe
@dataclass
class Reserva:
    numero_aviao: int
    nome_passageiro: str

    def exibir_reserva(self):
        print(f"Avião: {self.numero_aviao}")
        print(f"Passageiro: {self.nome_passageiro}")


# Vetores 
vetor_avioes = [None] * 4
vetor_assentos = [0] * 4

lista_reservas = []
MAX_RESERVAS = 20 


# Funções Auxiliares
def limpar_tela():
    os.system("cls")


def pausar():
    input("\nPressione Enter para continuar...")


# Programa Principal
def main():
    while True:
        limpar_tela()
        print("==========================================")
        print("    SISTEMA DE GESTÃO - SWEET FLIGHT")
        print("==========================================")
        print("1. Registrar números dos aviões")
        print("2. Registrar quantitativo de assentos")
        print("3. Reservar passagem aérea")
        print("4. Realizar consulta por avião")
        print("5. Realizar consulta por passageiro")
        print("6. Sair")
        print("------------------------------------------")

        opcao = input("Escolha uma opção: ")

        match opcao:

            # Opção 1 
            case "1":
                print("\n--- Registro de Aviões ---")
                for i in range(4):
                    while True:
                        try:
                            num = int(input(f"Digite o número do avião {i + 1}: "))
                            vetor_avioes[i] = num
                            break
                        except ValueError:
                            print("Por favor, digite um número válido.")
                print("\nAviões registrados com sucesso!")
                pausar()

            # Opção 2
            case "2":
                print("\n--- Registro de Assentos ---")

                if vetor_avioes[0] is None:
                    print("Atenção: Cadastre os aviões (Opção 1) antes de definir os assentos.")
                else:
                    for i in range(4):
                        while True:
                            try:
                                qtd = int(input(f"Quantos assentos para o avião {vetor_avioes[i]}? "))
                                if qtd >= 0:
                                    vetor_assentos[i] = qtd
                                    break
                                else:
                                    print("A quantidade não pode ser negativa.")
                            except ValueError:
                                print("Digite um número inteiro válido.")

                    print("\nAssentos registrados com sucesso!")

                pausar()

            # Opção 3 — Reservar várias pessoas
            case "3":
                print("\n--- Reserva de Passagens ---")

                if len(lista_reservas) >= MAX_RESERVAS:
                    print("Limite máximo de 10 reservas atingido!")
                    pausar()
                    continue

                if vetor_avioes[0] is None:
                    print("Nenhum avião cadastrado.")
                    pausar()
                    continue

                try:
                    aviao_input = int(input("Informe o número do avião: "))

                    indice_aviao = -1
                    for i in range(4):
                        if vetor_avioes[i] == aviao_input:
                            indice_aviao = i
                            break

                    if indice_aviao == -1:
                        print("Este avião não existe!")
                        pausar()
                        continue

                    # Pergunta quantas pessoas deseja reservar
                    quantidade = int(input("Quantas pessoas deseja reservar? "))

                    # Verificações de limites
                    if quantidade <= 0:
                        print("A quantidade deve ser maior que zero.")
                        pausar()
                        continue

                    if quantidade > vetor_assentos[indice_aviao]:
                        print("Não há assentos suficientes para esse avião!")
                        pausar()
                        continue

                    if len(lista_reservas) + quantidade > MAX_RESERVAS:
                        print("Essa quantidade ultrapassa o limite máximo de 10 reservas.")
                        pausar()
                        continue

                    # Realiza as reservas múltiplas
                    for i in range(quantidade):
                        nome = input(f"Nome do passageiro {i + 1}: ")
                        nova_reserva = Reserva(aviao_input, nome)
                        lista_reservas.append(nova_reserva)

                    vetor_assentos[indice_aviao] -= quantidade
                    print("\nReservas realizadas com sucesso!")

                except ValueError:
                    print("Entrada inválida.")

                pausar()

            # Opção 4 
            case "4":
                print("\n--- Consulta por Avião ---")

                try:
                    aviao_input = int(input("Informe o número do avião: "))

                    if aviao_input not in vetor_avioes:
                        print("Este avião não existe!")
                    else:
                        encontrou = False
                        print(f"\nLista de passageiros do avião {aviao_input}:")
                        for reserva in lista_reservas:
                            if reserva.numero_aviao == aviao_input:
                                print(f"- {reserva.nome_passageiro}")
                                encontrou = True

                        if not encontrou:
                            print("Nenhuma reserva encontrada para este avião.")
                except ValueError:
                    print("Entrada inválida.")

                pausar()

            # Opção 5 
            case "5":
                print("\n--- Consulta por Passageiro ---")
                nome_input = input("Informe o nome do passageiro: ")

                encontrou = False
                print(f"\nReservas encontradas para {nome_input}:")
                for reserva in lista_reservas:
                    if reserva.nome_passageiro.lower() == nome_input.lower():
                        print(f"- Avião Nº {reserva.numero_aviao}")
                        encontrou = True

                if not encontrou:
                    print("Nenhuma reserva encontrada para este passageiro.")

                pausar()

            # Opção 6 
            case "6":
                print("\nEncerrando o sistema Sweet Flight")
                break

            # Inválida 
            case _:
                print("\nOpção inválida!")
                time.sleep(1)


if __name__ == "__main__":
    main()
