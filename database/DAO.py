from database.DB_connect import DBConnect
from model.border import Border
from model.country import Country


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_countries(year):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT c.*
                    FROM contiguity c1, country c 
                    WHERE (c.CCode = c1.state1no OR c.CCode = c1.state2no)
                    AND c1.year <= %s
                    ORDER BY c.StateAbb
                    """
            cursor.execute(query, (year,))

            for row in cursor:
                result.append(Country(**row))

            cursor.close()
            cnx.close()

        return result

    @staticmethod
    def get_edge(idmap, anno):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT c.state1no, c.state2no
                    FROM contiguity c 
                    WHERE c.year <= %s
                    AND conttype = 1
                            """
            cursor.execute(query, (anno,))

            for row in cursor:
                c1= idmap[row['state1no']] # prendo lo stato1 della prima coppia di stati
                c2 = idmap[row['state2no']]
                result.append(Border(c1,c2)) # inserisco nel border i due stati di ogni riga che mi restituisce il db

            cursor.close()
            cnx.close()

        return result

