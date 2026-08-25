from Evento import listaEventos, adicionarEvento


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

            if 1 <= escolha <= 6:
                return escolha

            print("Escolha uma opção entre 1 e 6.")

        except ValueError:
            print("Digite apenas um número.")


def visualizarEventos(listaEventos):
    if not listaEventos:
        print("Nenhum evento cadastrado.")
        return

    print("\n=== EVENTOS ===")

    for evento in listaEventos:
        status = "Participado" if evento["participado"] else "Não participado"

        print(f"\nID: {evento['id']}")
        print(f"Nome: {evento['nome']}")
        print(f"Data: {evento['data']}")
        print(f"Local: {evento['local']}")
        print(f"Categoria: {evento['categoria']}")
        print(f"Status: {status}")


def filtrarEventosPorCategoria(listaEventos, categoria):
    eventosFiltrados = []

    for evento in listaEventos:
        if evento["categoria"].lower() == categoria.lower():
            eventosFiltrados.append(evento)

    return eventosFiltrados


def marcarEventoAtendido(listaEventos, id):
    for evento in listaEventos:
        if evento["id"] == id:
            evento["participado"] = True
            print("Evento marcado como participado.")
            return True

    print("Evento não encontrado.")
    return False


def gerarRelatorio(listaEventos):
    totalEventos = len(listaEventos)

    print("\n=== RELATÓRIO ===")
    print(f"Total de eventos: {totalEventos}")

    if totalEventos == 0:
        print("Nenhum evento cadastrado.")
        return

    categorias = {}

    for evento in listaEventos:
        categoria = evento["categoria"]

        if categoria in categorias:
            categorias[categoria] += 1
        else:
            categorias[categoria] = 1

    print("\nEventos por categoria:")

    for categoria, quantidade in categorias.items():
        print(f"{categoria}: {quantidade}")

    totalParticipados = 0

    for evento in listaEventos:
        if evento["participado"]:
            totalParticipados += 1

    percentual = (totalParticipados / totalEventos) * 100

    print(f"\nEventos participados: {totalParticipados}")
    print(f"Percentual participado: {percentual:.2f}%")


while True:
    displayMenu()

    escolha = getEscolhaDoUsuario()

    if escolha == 1:
        print("\n=== ADICIONAR EVENTO ===")

        nome = input("Nome: ")
        data = input("Data (AAAA-MM-DD): ")
        local = input("Local: ")
        categoria = input("Categoria: ")

        adicionarEvento(
            listaEventos,
            nome,
            data,
            local,
            categoria
        )

    elif escolha == 2:
        visualizarEventos(listaEventos)

    elif escolha == 3:
        categoria = input("Digite a categoria: ")

        eventos = filtrarEventosPorCategoria(
            listaEventos,
            categoria
        )

        if not eventos:
            print("Nenhum evento encontrado nessa categoria.")
        else:
            visualizarEventos(eventos)

    elif escolha == 4:
        try:
            idEvento = int(input("Digite o ID do evento: "))
            marcarEventoAtendido(listaEventos, idEvento)

        except ValueError:
            print("Digite um ID válido.")

    elif escolha == 5:
        gerarRelatorio(listaEventos)

    elif escolha == 6:
        print("Programa encerrado.")
        break