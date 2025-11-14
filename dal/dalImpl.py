import pymssql
from modele.pingouins import Pingouin

SERVER = 'localhost'
USER = 'SA'
PWD = 'pa$$word'
BDD = 'PINGOUINS'

GET_ALL = "SELECT * FROM Pingouins"
DELETE_PINGOUIN = "DELETE FROM Pingouins WHERE id_pingouin=%d"
MODIF_PINGOUIN = "UPDATE Pingouins SET espece=%s, ile=%s, longueur_bec=%d, profondeur_bec=%d, longueur_nageoire=%d, poids=%d, sex=%s, annee_naissance=%d WHERE id_pingouin=%d"
GET_PINGOUIN = "SELECT * from Pingouins Where id_pingouin=%d"


def get_all_pingouins():
    cnx = pymssql.connect(SERVER, USER, PWD, BDD)
    cursor = cnx.cursor(as_dict=True)
    cursor.execute(GET_ALL)
    pingouins = []
    for row in cursor:
        pingouins.append(Pingouin(row['id_pingouin'], row['espece'], row['ile'], row['longueur_bec'],
                                  row['profondeur_bec'], row['longueur_nageoire'], row['poids'],
                                  row['sex'], row['annee_naissance']))
    cnx.close()
    return pingouins


def delete_pingouin(id):
    cnx = pymssql.connect(SERVER, USER, PWD, BDD)
    cursor = cnx.cursor()
    cursor.execute(DELETE_PINGOUIN, (id,))
    cnx.commit()
    cnx.close()


def update_pingouin(pingouin):
    cnx = pymssql.connect(SERVER, USER, PWD, BDD)
    cursor = cnx.cursor()
    cursor.execute(MODIF_PINGOUIN, (
        pingouin.espece, pingouin.ile, pingouin.longueur_bec, pingouin.profondeur_bec,
        pingouin.longueur_nageoire, pingouin.poids, pingouin.sexe, pingouin.annee_naissance, pingouin.id))
    cnx.commit()
    cnx.close()


def get_pingouin(id):
    cnx = pymssql.connect(SERVER, USER, PWD, BDD)
    cursor = cnx.cursor(as_dict=True)
    cursor.execute(GET_PINGOUIN, (id,))
    row = cursor.fetchone()
    cnx.close()
    return Pingouin(row['id_pingouin'], row['espece'], row['ile'], row['longueur_bec'],
                    row['profondeur_bec'], row['longueur_nageoire'], row['poids'],
                    row['sex'], row['annee_naissance'])
