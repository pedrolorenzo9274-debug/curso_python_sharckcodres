[A senha secreta.py](https://github.com/user-attachments/files/26631818/A.senha.secreta.py)
senha = "0000"
tentativa = input("Insira sua senha (Máximo de 3 tentativas): ")
numero_de_tentativas = 1

while tentativa != senha:
    print("Senha errada.")
    tentativa = input("Insira sua senha: ")
    numero_de_tentativas += 1
    if numero_de_tentativas > 2 and tentativa != senha:
        print("Tentativas demais,bloqueado")
        break

if tentativa == senha:
    print("Você acertou a senha")
