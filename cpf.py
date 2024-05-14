import sqlite3

conn = sqlite3.connect('cpf_database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS cpfs (
                    id INTEGER PRIMARY KEY,
                    cpf TEXT UNIQUE
                )''')
conn.commit()
def verificar_cpf(cpf):
    cursor.execute('SELECT cpf FROM cpfs WHERE cpf = ?', (cpf,))
    result = cursor.fetchone()
    if result:
        print("CPF já foi digitado anteriormente.")
    else:
        cursor.execute('INSERT INTO cpfs (cpf) VALUES (?)', (cpf,))
        conn.commit()
        print("CPF adicionado com sucesso.")
while True:
    cpf = input("Digite um CPF (ou 'sair' para encerrar): ")
    if cpf.lower() == 'sair':
        break
    else:
        verificar_cpf(cpf)
print("Programa encerrado.")
conn.close()