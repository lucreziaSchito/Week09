from database.DB_connect import DBConnect
from model.film import Film

class Dao:
    @staticmethod
    def get_all_film():
        """Query di esempio, non utilizzata dalle funzionalità dell'esercizio."""
        cnx = DBConnect.get_connection()
        try:
            cursor = cnx.cursor(dictionary=True)
            try:
                cursor.execute('''SELECT id, titolo, genere, serata,
                                         numero_voti, somma_voti
                                  FROM film ORDER BY id''')

                result = []
                for r in cursor:
                    film = Film(r['id'], r['titolo'], r['genere'], r['serata'], r['numero_voti'], float(r['somma_voti']))
                    result.append(film)
                return result

            finally:
                cursor.close()
        finally:
            cnx.close()

if __name__ == '__main__':
    dao = Dao()
    print(dao.get_all_film()) # per controllare che la connessione avvenga