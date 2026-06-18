import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import xml.etree.ElementTree as ET
import services
import templates
import db

PORT = int(os.environ.get('PORT', 8000))

class SOAPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or '?wsdl' in self.path:
            self.send_response(200)
            self.send_header('Content-Type', 'application/xml; charset=utf-8')
            self.end_headers()
            clean_wsdl = templates.WSDL_CONTENT.strip()
            self.wfile.write(clean_wsdl.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Non trouve")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        soap_action = self.headers.get('SOAPAction', '')

        try:
            if "GetDossier" in post_data or "GetDossier" in soap_action:
                response_xml = services.handle_get_dossier(post_data)
            elif "CreateDossier" in post_data or "CreateDossier" in soap_action:
                root = ET.fromstring(post_data)
                ref = root.find('.//reference_metier').text if root.find('.//reference_metier') is not None else ''
                stat = root.find('.//statut').text if root.find('.//statut') is not None else ''
                op = root.find('.//type_operation').text if root.find('.//type_operation') is not None else ''
                
                response_xml = db.creer_dossier(ref, stat, op)
            else:
                response_xml = templates.SOAP_SUCCESS_RESPONSE.format(body_content="<error>Unknown Action</error>")
        except Exception as e:
            print(f"Erreur d execution : {e}")
            response_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
   <soapenv:Body>
      <soapenv:Fault>
         <faultcode>soapenv:Server</faultcode>
         <faultstring>Erreur interne lors du traitement de la requete.</faultstring>
         <detail>
            <exception>{str(e)}</exception>
         </detail>
      </soapenv:Fault>
   </soapenv:Body>
</soapenv:Envelope>"""

        self.send_response(200)
        self.send_header("Content-Type", "text/xml; charset=utf-8")
        self.end_headers()
        self.wfile.write(response_xml.encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', PORT), SOAPHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()