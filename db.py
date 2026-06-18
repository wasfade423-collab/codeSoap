import psycopg2
from psycopg2.extras import RealDictCursor
import templates

def obtenir_dossier(reference_metier):
    connection = None
    cursor = None
    try:
        # 1. Connexion via le réseau privé de Render
        connection = psycopg2.connect(
            host="dpg-d8q0mshkh4rs73bvtck0-a",  # Ton hôte interne Render
            database="smartport_gateway",
            user="smartport_gateway_user",
            password="ybzlz0DvNf6MVuwlM7grPnTMC36FRLfw",
            port=5432
        )
        
        # RealDictCursor permet de récupérer les résultats sous forme de dictionnaire (ex: ligne['statut'])
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        
        # 2. Ta requête SQL pour chercher le dossier
        requete = "SELECT id, statut, type_operation FROM dossiers WHERE reference_metier = %s;"
        cursor.execute(requete, (reference_metier,))
        resultat = cursor.fetchone()
        
        if resultat:
            # 3. On construit le contenu XML de la réponse avec les vraies données de la DB
            body_content = f"""
            <smart:GetDossierResponse>
               <id>{resultat['id']}</id>
               <statut>{resultat['statut']}</statut>
               <type_operation>{resultat['type_operation']}</type_operation>
            </smart:GetDossierResponse>
            """
            # On insère ce body dans le template générique de succès
            return templates.SOAP_SUCCESS_RESPONSE.format(body_content=body_content)
        else:
            # Gestion si le dossier n'existe pas
            return "<soapenv:Fault><faultstring>Dossier introuvable</faultstring></soapenv:Fault>"
            
    except Exception as e:
        print(f"Erreur DB : {e}")
        return "<soapenv:Fault><faultstring>Erreur interne du serveur</faultstring></soapenv:Fault>"
        
    finally:
        # Toujours fermer le curseur et la connexion
        if cursor: cursor.close()
        if connection: connection.close()