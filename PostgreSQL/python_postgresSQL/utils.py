import psycopg2
from time import sleep

def conectar():
    """
    Função para conectar ao servidor
    """
    try:
        conn = psycopg2.connect(
            database='python_postgreSQL',
            host='localhost',
            user='postgres',
            password='postgres'
        )
        return conn
    except psycopg2.Error as erro:
        print(f'Erro na conexão ao PostgreSQL Server:{erro}')



def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """

    if conn: #se existir uma conecxão,
        conn.close() #desconecta pra mim


def listar():
    """
    Função para listar os produtos
    """
    conn = conectar()
    cursor = conn.cursor() #criando um cursor para trabalhar com as Query
    cursor.execute('select * from produtos') #usando o cursor para executar a consulta
    produtos = cursor.fetchall()  #transformando tudo em lista

    if len(produtos) > 0: #verificando se nossa lista tem dados ou seja, se ela é maior que 0.
        print('Listando produtos... ')
        print(20 * '-')
        for produto in produtos:
            print(f'ID: {produto[0]}')
            print(f'Produto: {produto[1]}')
            print(f'Preço: {produto[2]}')
            print(f'Estoque: {produto[3]}')
            print(20 * '-')
    else:
        print('Não existem produtos cadastrados.')
    desconectar(conn) #usando a função desconectar


def inserir():
    """
    Função para inserir um produto
    """  
    conn = conectar()
    cursor = conn.cursor()

    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))
    estoque = int(input('Informe a quantidade em estoque: '))

    cursor.execute(f"INSERT INTO produtos (nome, preco, estoque) VALUES ('{nome}',{preco}, {estoque})")
    conn.commit() #gravando as alterações no banco de dados.

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi inserido com sucesso.')
    else:
        print('Não foi possivel inserir o produto.')
    desconectar(conn)


def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o código do produto: '))
    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))
    estoque = int(input('Informe a quantidade em estoque: '))

    cursor.execute(f"UPDATE produtos SET nome='{nome}', preco={preco}, estoque={estoque} WHERE id={codigo}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi atualizado com sucesso.')
    else:
        print('Erro ao atualizar o produto.')
    desconectar(conn)




def deletar():
    """
    Função para deletar um produto
    """
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o código do produto: '))

    cursor.execute(f'DELETE FROM produtos WHERE id={codigo}')
    conn.commit()

    if cursor.rowcount == 1:
        print('Produto excluído com sucesso.')
    else:
        print(f'Erro ao exluir o produto com id {codigo}')
    desconectar(conn)




def menu():
    """
    Função para gerar o menu inicial
    """
    while True:
        sleep(2)
        print('=========Gerenciamento de Produtos==============')
        print('Selecione uma opção: ')
        print('1 - Listar produtos.')
        print('2 - Inserir produtos.')
        print('3 - Atualizar produto.')
        print('4 - Deletar produto.')
        print('5 - Sair do programa.')
        opcao = int(input('Digite uma opção: '))
        if opcao in [1, 2, 3, 4, 5]:
            if opcao == 1:
                listar()
            elif opcao == 2:
                inserir()
            elif opcao == 3:
                atualizar()
            elif opcao == 4:
                deletar()
            elif opcao == 5:
                print(f'Saindo do programa ...')
                sleep(1)
                break
            else:
                print('Opção inválida')
        else:
            print('Opção inválida')

