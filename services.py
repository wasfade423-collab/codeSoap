# Exemple dans ton fichier de gestion des services
from psycopg2.extras import RealDictCursor
import db # Ton module de connexion

def extraire_dossier(reference_metier):
    conn = db.get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    
    # Exécution de la requête sur PostgreSQL
    cursor.execute("SELECT id, statut, type_operation FROM dossiers_fret WHERE reference_metier = %s", (reference_metier,))
    dossier = cursor.fetchone()
    
    cursor.close()
    conn.close()
    return dossier