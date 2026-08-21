#Modulo de Gerenciamennto de Evento

#Lista de memória
listaEventos=[]


#Formato de cada evento: Dicionario
#     "id": int,             # identificador único do evento
#     "nome": str,           # nome do evento
#     "data": str,           # formato AAAA-MM-DD
#     "local": str,          # local onde ocorre o evento
#     "categoria": str,      # "Tecnologia", "IA", "Cultura Tecnologica"
#     "participado": bool    # retornar: true se o participante for constante
# }

    def validarEvento(evento):
        try:
            datetime.strptime(evento, '%d/%m/%Y')
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
