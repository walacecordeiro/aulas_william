usuarios = {'walace':'ativo', 'denis':'inativo', 'marcos':'ativo', 'marcelo':'inativo'}

# Neste caso o loop itera pela cópia e deleta na coleção original.
for user, status in usuarios.copy().items():
    if status == 'inativo':
        del usuarios[user]

print(usuarios)

# Neste caso é criada uma nova coleção, o loop itera diretamente nos itens da coleção, depois adiciona com base na condição os itens a nova coleção.
usuarios_ativos = {}
for user, status in usuarios.items():
    if status == 'ativo':
        usuarios_ativos[user] = status

print(usuarios_ativos)