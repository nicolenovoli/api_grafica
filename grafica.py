import json

# carregar usuários do arquivo
def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except:
        return []

# salvar usuários no arquivo
def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

# "banco de dados" simples (lista)
users = load_users()


# função para cadastrar usuário
def registro_usuario(nome, email, telefone, endereco):
    # verificar se já existe
    for user in users:
        if user["email"] == email:
            print("❌ Email já cadastrado!")
            return

    new_user = {
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "endereco": endereco
    }

    users.append(new_user)
    save_users(users)  # <== salvando no arquivo
    print("✅ Usuário cadastrado com sucesso!")
    
    
"""
registro_usuario("João", "joao@email.com", 44999999999, "Rua A, 123")
registro_usuario("Maria", "maria@email.com", 44888888888, "Rua B, 456")

# tentando cadastrar repetido
registro_usuario("João 2", "joao@email.com", 44777777777, "Rua C, 789")

print("\n📋 Lista de usuários:")
print(users)
"""

