def displayMenu():
    print("\n=== Planejador de Eventos do Campus ===")
    print("1. Adicionar Evento")
    print("2. Ver Todos os Eventos")
    print("3. Filtrar por Categoria")
    print("4. Marcar Evento como Participado")
    print("5. Gerar Relatório")
    print("6. Sair")

def getEscolhaDoUsuario():
    while True:
        try:
            escolha = int(input("Escolha uma opção: "))
            return escolha
        except ValueError:
            print("Digite apenas um número.")
            