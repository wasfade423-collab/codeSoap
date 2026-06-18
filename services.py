import xml.etree.ElementTree as ET
import db

def handle_get_dossier(xml_request):
    try:
        root = ET.fromstring(xml_request)
        reference_metier = root.find('.//reference_metier').text if root.find('.//reference_metier') is not None else ''
        
        if not reference_metier:
            return "<soapenv:Fault><faultstring>Reference metier manquante dans la requete</faultstring></soapenv:Fault>"
            
        return db.obtenir_dossier(reference_metier)
        
    except Exception as e:
        print(f"Erreur services : {e}")
        return f"<soapenv:Fault><faultstring>Erreur de traitement XML : {str(e)}</faultstring></soapenv:Fault>"