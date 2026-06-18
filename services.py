import xml.etree.ElementTree as ET
from psycopg2.extras import RealDictCursor
import db  # Ton module de connexion (db.py)
import templates

def handle_get_dossier(xml_body):
    # Extraction de la référence métier depuis le XML reçu
    root = ET.fromstring(xml_body)
    ref_metier = root.find('.//reference_metier').text 
    
    conn = db.get_db_connection()
    if not conn:
        return "<error>DB_CONNECTION_FAILED</error>"
    
    # Utilisation du RealDictCursor pour PostgreSQL
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT id, statut, type_operation FROM dossiers_fret WHERE reference_metier = %s", (ref_metier,))
    dossier = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if dossier:
        body = f"""<smart:GetDossierResponse>
            <id>{dossier['id']}</id>
            <statut>{dossier['statut']}</statut>
            <type_operation>{dossier['type_operation']}</type_operation>
        </smart:GetDossierResponse>"""
    else:
        body = "<smart:GetDossierResponse><error>Dossier introuvable</error></smart:GetDossierResponse>"
        
    return templates.SOAP_SUCCESS_RESPONSE.format(body_content=body)