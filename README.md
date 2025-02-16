# SGE_BLOC2

## Activitat python+postgresql

### Comprovació connexió

Quan executes **print(conn)**, es mostra un objecte de connexió que indica que la base de dades s'ha connectat correctament. A la sortida apareixen les dades de connexió i l'estat **closed: 0**, cosa que significa que la connexió *està activa*. Després, quan crides **conn.close()**, la connexió *es tanca*. Si tornes a imprimir conn, l'objecte continua existint, però ara apareix amb **closed: 1**, indicant que ja no es pot utilitzar per a consultes.

<img src="img/connect(0).png" width="800">

### Creació taules

L’script ha creat a PostgreSQL la taula Clientes amb les columnes donades.
Si entres a pgadmin i busques a la base de dades the_bear, veuràs la taula creada. Si executes SELECT * FROM Clientes; veuràs que la taula existeix però està buida, ja que només s’ha creat l'estructura sense registres.

<img src="img/taules(1).png" width="800">

### Inserció de dades

En executar el segon arxiu **(csv_to_dict.py)**, s’han llegit les dades del fitxer **Clientes.csv** i s’han inserit els 30 primers registres a la taula Clientes de la base de dades **the_bear**.
Si vas a pgadmin, ara es veu la taula plena amb 30 registres, cadascun amb les dades requerides.

<img src="img/(2).png" width="800">

### Creació registre

En executar **main.py**, s’ha afegit un nou client (Roger) a la taula Clientes de la base de dades **the_bear**.

Al pgadmin, es veu que ara hi ha un registre amb les dades que li hem introduit.

<img src="img/(3).png" width="800">

## LISTS

### Veure les dades

En executar **read_registre.py**, la terminal mostra tots els clients de la taula **Clientes** en forma de llista. Això confirma que la consulta SELECT * FROM clientes funciona correctament.

<img src="img/(4).png" width="800">