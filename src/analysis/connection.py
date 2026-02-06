import mysql.connector
import pandas as pd

def get_db_data(query):
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '1234', 
        'database': 'classicmodels',
        'port': 3306
    }
    conn = mysql.connector.connect(**db_config)
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Ce bloc s'exécute uniquement quand tu lances ce fichier directement
if __name__ == "__main__":
    # Test the connection
    data = get_db_data("SELECT 1")
    if data is not None:
        print("Successfully connected to the classicmodels database!")
    else:
        print("Connection failed.")