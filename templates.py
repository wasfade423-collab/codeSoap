# Modèle de réponse SOAP générique en cas de succès
SOAP_SUCCESS_RESPONSE = """<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:smart="http://smartport.lacotonou.bj/">
   <soapenv:Header/>
   <soapenv:Body>
      {body_content}
   </soapenv:Body>
</soapenv:Envelope>"""

# Fichier WSDL minimal à renvoyer si l'utilisateur fait un GET sur l'URL
WSDL_CONTENT = """<?xml version="1.0" encoding="UTF-8"?>
<wsdl:definitions name="SmartPortSoap" ...>
   </wsdl:definitions>
"""