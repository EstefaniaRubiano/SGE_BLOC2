import connect

def read_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_read = "SELECT * FROM clientes"

    cursor.execute(sql_read)
    conn.commit()

    results = cursor.fetchall()

    #Obtenir resultats
    print(results)
    print(results[4])
    print(results[4][3])

print(read_reg())


