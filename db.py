import psycopg2
from psycopg2.extras import RealDictCursor
import templates

def get_db_connection():
    try:
        connection = psycopg2.connect(
            host="dpg-d8q0mshkh4rs73bvtck0-a",
            database="smartport_gateway",
            user="smartport_gateway_user",
            password="ybzlz0DvNf6MVuwlM7grPnTMC36FRLfw",
            port=5432
        )
        return connection
    except Exception as e:
        print(f"Erreur de connexion : {e}")
        return None

def obtenir_dossier(reference_metier):
    connection = get_db_connection()
    if not connection:
        return "<soapenv:Fault><faultstring>Erreur de connexion a la base de donnees</faultstring></soapenv:Fault>"
    
    cursor = None
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        requete = "SELECT id, statut, type_operation FROM dossiers WHERE reference_metier = %s;"
        cursor.execute(requete, (reference_metier,))
        resultat = cursor.fetchone()
        
        if resultat:
            body_content = f"""
            <smart:GetDossierResponse>
               <id>{resultat['id']}</id>
               <statut>{resultat['statut']}</statut>
               <type_operation>{resultat['type_operation']}</type_operation>
            </smart:GetDossierResponse>
            """
            return templates.SOAP_SUCCESS_RESPONSE.format(body_content=body_content)
        else:
            return "<soapenv:Fault><faultstring>Dossier introuvable</faultstring></soapenv:Fault>"
            
    except Exception as e:
        print(f"Erreur SQL : {e}")
        return f"<soapenv:Fault><faultstring>Erreur interne du serveur : {str(e)}</faultstring></soapenv:Fault>"
        
    finally:
        if cursor: cursor.close()
        if connection: connection.close()