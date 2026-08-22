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

   categoria = input("Digite a categoria: ")

eventos = filtrarEventosPorCategoria(listaEventos, categoria)

if not eventos:
    print("Nenhum evento encontrado nessa categoria.")
else:
    visualizarEventos(eventos)

def marcarEventoAtendido(listaEventos, id):
    for evento in listaEventos:
        if evento["id"] == id:
            evento["participado"] = True
            print("Evento marcado como participado.")
            return True

    print("Evento não encontrado.")
    return False