from datetime import datetime

# Módulo de Gerenciamento de Eventos
# Estudante A

listaEventos = []

# Formato de cada evento (dicionário):
# {
#     "id": int,             # identificador único do evento
#     "nome": str,           # nome do evento
#     "data": str,           # formato AAAA-MM-DD
#     "local": str,          # local onde ocorre o evento
#     "categoria": str,      # ex: "Tecnologia", "IA", "Cultura Tecnologica"
#     "participado": bool    # true se o participante confirmou presença
# }


def validarData(dataStr):
    try:
        datetime.strptime(dataStr, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def adicionarEvento(listaEventos, nome, data, local, categoria):
    if not nome or not local or not categoria:
        print("Erro: nome, local e categoria não podem estar vazios.")
        return False

    if not validarData(data):
        print("Erro: data inválida. Use o formato AAAA-MM-DD.")
        return False

    novoId = len(listaEventos) + 1

    novoEvento = {
        "id": novoId,
        "nome": nome,
        "data": data,
        "local": local,
        "categoria": categoria,
        "participado": False
    }

    listaEventos.append(novoEvento)
    print(f"Evento '{nome}' adicionado com sucesso!")
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
