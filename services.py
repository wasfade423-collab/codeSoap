import xml.etree.ElementTree as ET
from db import get_db_connection
import templates

def handle_get_dossier(xml_body):
    # 1. Extraction des paramètres depuis le XML reçu
    root = ET.fromstring(xml_body)
    # Exemple de recherche de balise (à adapter selon vos structures de requêtes)
    ref_metier = root.find('.//reference_metier').text 
    
    # 2. Appel à la base de données MySQL
    conn = get_db_connection()
    if not conn:
        return "<error>DB_CONNECTION_FAILED</error>"
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM dossiers_fret WHERE reference_metier = %s", (ref_metier,))
    dossier = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    # 3. Génération du contenu XML de la réponse
    if dossier:
        body = f"""<smart:GetDossierResponse>
            <id>{dossier['id']}</id>
            <statut>{dossier['statut']}</statut>
            <type_operation>{dossier['type_operation']}</type_operation>
        </smart:GetDossierResponse>"""
    else:
        body = "<smart:GetDossierResponse><error>Dossier introuvable</error></smart:GetDossierResponse>"
        
    return templates.SOAP_SUCCESS_RESPONSE.format(body_content=body)