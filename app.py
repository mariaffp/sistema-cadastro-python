#importa a biblioteca de funções do sistema operacional
import os

#print(os.getcwd())
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    BASE_DIR = os.getcwd()

ARQUIVO = os.path.join(BASE_DIR, 'cadastros.txt')

def menu_interativo():
    lista = []
    while True:
        print('''
            ====MENU====
            1.Cadastrar
            2.Listar
            3.Buscar
            4.Remover
            5.Salvar e Sair
            ''')
        opt = int(input("Escolha a opção: "))

        if opt == 1:
            nome = input("Nome: ")
            idade = input("Idade: ")
            email = input("Email: ")
            cadastrar(lista,nome,idade,email)
            print("Cadastro realizado com sucesso! ")
        elif opt == 2:
            print(listar(lista))
        elif opt == 3:
            nome = input("Digite o nome que deseja buscar ")
            encontrado = buscar(lista,nome)
            if encontrado:
                print("Usuário encontrado: ", encontrado)
            else:
                print("Usuário não encontrado")
        elif opt == 4:
            nome = input("Digite o nome que deseja buscar ")
            removido = remover(lista,nome)
            if removido:
                print("Usuário removido com sucesso")
            else:
                print("Usuário não encontrado")
        elif opt == 5:
            salvar(lista)
            print("Dados salvos, hora de sair")
            break
        else:
            print("Opção inválida")

def cadastrar(lista,nome, idade, email):
    lista.append({"Nome": nome, "Idade": idade, "Email": email})

def listar(lista):
    if not lista:
        return "-----cadastro vazio-----"
    linhas = ""
    for i in lista:
        linhas += (f"\n Nome: {i['Nome']} Idade:{i['Idade']} Email:{i['Email']}")
    return linhas

def buscar(lista,nome_Buscado):
    for busca in lista:
        if busca['Nome'] == nome_Buscado:
            return (f'''\n Nome: {busca['Nome']} Idade: {busca['Idade']} Email: {busca['Email']}''')
    return None

def remover(lista,nome_query):
    for busca in lista:
        if busca['Nome'] == nome_query:
            lista.remove(busca)
            return True
    return False
def salvar(lista,caminho = ARQUIVO):
    with open(caminho,'w', encoding = 'utf-8') as f:
        for usuario in lista:
            f.write((f'''\n
                     Nome: {usuario['Nome']}
                     Idade: {usuario['Idade']}
                     Email: {usuario['Email']}'''))
    return True




def main():
    menu_interativo()

if __name__ == "__main__":
    main()

