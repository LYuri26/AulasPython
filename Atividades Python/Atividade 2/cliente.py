# cliente.py

class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def atualizar_email(self, novo_email):
        self.email = novo_email

    def atualizar_telefone(self, novo_telefone):
        self.telefone = novo_telefone


# Exemplo de uso
cliente1 = Cliente("João", "joao@email.com", "(11) 9999-9999")
print(f"Cliente: {cliente1.nome}, Email: {
      cliente1.email}, Telefone: {cliente1.telefone}")

# Atualiza o email e o telefone do cliente
cliente1.atualizar_email("joao.novo@email.com")
cliente1.atualizar_telefone("(11) 8888-8888")
print(f"Cliente atualizado: {cliente1.nome}, Email: {
      cliente1.email}, Telefone: {cliente1.telefone}")
