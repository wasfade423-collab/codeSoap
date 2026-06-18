import psycopg2
import os

def get_db_connection():
    try:
        # Utilise l'External Connection String de Render que nous avons configuré
        connection = psycopg2.connect(
            host="dpg-d8q0mshkh4rs73bvtck0-a.ohio-postgres.render.com",
            database="smartport_gateway",
            user="smartport_gateway_user",
            password="ybzlz0DvNf6MVuwlM7grPnTMC36FRLfw",
            port=5432
        )
        return connection
    except Exception as e:
        print(f"Erreur de connexion à la base de données : {e}")
        return None