import psycopg2
import os

def get_db_connection():
    try:
        connection = psycopg2.connect(
            # Utilise l'hôte interne fourni par Render (vérifie-le sur ton dashboard)
            host="dpg-d8q0mshkh4rs73bvtck0-a", 
            database="smartport_gateway",
            user="smartport_gateway_user",
            password="ybzlz0DvNf6MVuwlM7grPnTMC36FRLfw",
            port=5432
        )
        return connection
    except Exception as e:
        print(f"Erreur de connexion à la base de données : {e}")
        return None