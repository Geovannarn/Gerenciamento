from datetime import datetime

# Módulo de Gerenciamento de Eventos
# Estudante A

listaEventos = []

def validarData(dataStr):
    try:
        datetime.strptime(dataStr, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def adicionarEvento(listaEventos, nome, data, local, categoria):
    if not nome.strip() or not local.strip() or not categoria.strip():
        print("Erro: nome, local e categoria não podem estar vazios.")
        return False

    if not validarData(data):
        print("Erro: data inválida. Use o formato AAAA-MM-DD.")
        return False

    novoId = max((evento["id"] for evento in listaEventos), default=0) +1

    novoEvento = {
        "id": novoId,
        "nome": nome,
        "data": data,
        "local": local,
        "categoria": categoria,
        "participado": False
    }

    listaEventos.append(novoEvento)
    print(f"Evento '{nome}' (id {novoId}) adicionado com sucesso!")
    return True


def listarEventos(listaEventos):
    if not listaEventos:
        print("Nenhum evento cadastrado.")
        return

    for evento in listaEventos:
        status = "Participou" if evento["participado"] else "Não participou"
        print(f"[{evento['id']}] {evento['nome']} | {evento['data']} | {evento['local']} | {evento['categoria']} | {status}")


def procurarEventoPorNome(listaEventos, nome):
    encontrados = [
        evento for evento in listaEventos
        if nome.lower() in evento["nome"].lower()
    ]

    if not encontrados:
        print(f"Nenhum evento encontrado com o nome '{nome}'.")
    else:
        print(f"\n--- Resultados da busca por '{nome}' ---")
        for evento in encontrados:
            status = "Participou" if evento["participado"] else "Não participou"
            print(f"[{evento['id']}] {evento['nome']} | {evento['data']} | {evento['local']} | {evento['categoria']} | {status}")

    return encontrados
def deletarEvento(listaEventos, id_evento):
    for evento in listaEventos:
        if evento["id"] == id_evento:
            listaEventos.remove(evento)
            print(f"Evento '{evento['nome']}' (id {id_evento}) removido com sucesso.")
            return True

    print(f"Erro: nenhum evento encontrado com id {id_evento}.")
    return False


if __name__ == "__main__":
    adicionarEvento(listaEventos, "Semana de Tecnologia", "2025-11-10", "Auditório Central", "Tecnologia")
    adicionarEvento(listaEventos, "Feira de Cultura", "2025-12-01", "Ginásio", "Cultura")
    adicionarEvento(listaEventos, "", "2025-11-10", "Auditório Central", "Tecnologia")   # TEM QUE FALHAR  (nome vazio)
    adicionarEvento(listaEventos, "Evento Teste", "10/11/2025", "Local X", "Cultura")    # TEM QUE FALHAR   (data errada)

    print("\n--- Lista de Eventos ---")
    listarEventos(listaEventos)

    print("\n--- Busca por Nome ---")
    procurarEventoPorNome(listaEventos, "tecnologia")

    print("\n--- Busca por Categoria ---")
    procurarEventoPorCategoria(listaEventos, "Tecnologia")

    print("\n--- Deletar por id ---")
    deletarEvento(listaEventos, id_eventos=1)


    print("\n--- Deletar por nome ---")
    deletarEvento(listaEventos, nome="Segurança Quântica" )

    print("\n--- Lista Após Remoção ---")
    listarEventos(listaEventos)