import connect

def update_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_update = '''
    UPDATE clientes
    SET teléfono_cliente=987654321
    WHERE nombre_cliente = 'Mireia'
    '''
    cursor.execute(sql_update)
    conn.commit()

    cursor.close()
    conn.close()

    return {"Update succesfully"}