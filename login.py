import time
import os
from cryptography.fernet import Fernet
import sqlite3
import subprocess

#criptografia
arquivo_chave = 'chave.key'
if os.path.exists(arquivo_chave):
    with open(arquivo_chave, 'rb') as arquivo:
        chave = arquivo.read()
else:
    chave = Fernet.generate_key()
    with open(arquivo_chave, 'wb') as arquivo:
        arquivo.write(chave)
crypto = Fernet(chave)

#banco de usuários
banco_de_dados = sqlite3.connect("0usuarios.db")
cursor = banco_de_dados.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    senha TEXT NOT NULL
)
""")
banco_de_dados.commit()

#classe usuário
class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = crypto.encrypt(senha.encode())
    def __str__(self):
        return f"Usuario: {self.nome}"f", Senha: {self.senha}"
    def __repr__(self):
        return self.__str__()

#registra o usuário no banco de dados
def salvar_usuario(nome, senha):
    cursor.execute(
        "INSERT INTO usuarios (nome, senha) VALUES (?, ?)",
        (nome, senha)
    )
    banco_de_dados.commit()

#inicia o aplicativo
def inicio():
    os.system('cls')
    print('1-fazer login')
    print('2-criar conta')
    resposta = input('Escolha: ')
    if resposta == "1":
        fazer_login()
    elif resposta == "2":
        criar_conta()

#opção de fazer o login
def fazer_login():
    while True:
        os.system('cls')
        nome = input("Usuário: ")
        senha = input("Senha: ")
        cursor.execute(
            'SELECT senha FROM usuarios WHERE nome = ?',
            (nome,)
        )
        resultado = cursor.fetchone()
        if resultado:
            senha_banco = resultado[0]
            senha_original = crypto.decrypt(
                senha_banco
            ).decode()
            if senha_original == senha:
                print('Login Realizado')
                global novo_usuario
                novo_usuario = Usuario(nome, senha)
                print(f"Bem-vindo de volta, {nome}!")
                global historico
                historico = sqlite3.connect(f"{novo_usuario.nome}.db")
                global Cursor
                Cursor = historico.cursor()
                Cursor.execute("""
                CREATE TABLE IF NOT EXISTS musicas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    artista TEXT NOT NULL,
                    album TEXT NOT NULL,
                    duracao TEXT NOT NULL,
                    genero TEXT NOT NULL,
                    ano INTEGER NOT NULL
                )
                """)
                historico.commit()
                time.sleep(3)
                break
                time.sleep(3) 
                break
            else:
                print('senha incorreta')
                time.sleep(3)
                continue
        else:
            print('Usuário inexistente')
            time.sleep(3)
            continue

#opção de criar uma conta
def criar_conta():
    while True:
        os.system('cls')
        nome = input('Crie um nome de usuário: ')
        cursor.execute(
        "SELECT nome FROM usuarios WHERE nome = ?",
        (nome,)
        )
        resultado = cursor.fetchone()
        if resultado:
            print("Usuário já existe")
            time.sleep(3)
            continue
        senha = input('Crie uma senha: ')
        if len(senha) < 8:
            print('A senha deve ter no mínimo 8 caracteres')
            time.sleep(3)
            continue
        elif senha == nome:
            print('Crie uma senha forte')
            time.sleep(3)
            continue
        else:
            global novo_usuario
            novo_usuario = Usuario(nome, senha)
            salvar_usuario(
                novo_usuario.nome,
                novo_usuario.senha
            )
            print("Conta criada com sucesso!")
            global historico
            historico = sqlite3.connect(f"{novo_usuario.nome}.db")
            global Cursor
            Cursor = historico.cursor()
            Cursor.execute("""
            CREATE TABLE IF NOT EXISTS musicas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                você TEXT NOT NULL,
                monkey TEXT NOT NULL
            )
            """)
            historico.commit()
            time.sleep(3)
            break

inicio()