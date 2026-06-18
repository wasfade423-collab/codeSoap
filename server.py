import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import services
import templates

PORT = int(os.environ.get('PORT', 8000))

class SOAPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/?wsdl':
            self.send_response(200)
            # On indique bien au navigateur que c'est du XML
            self.send_header('Content-Type', 'application/xml; charset=utf-8')
            self.end_headers()
            
            # .strip() supprime les espaces et sauts de ligne invisibles au début et à la fin
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

        if "GetDossier" in post_data or "GetDossier" in soap_action:
            response_xml = services.handle_get_dossier(post_data)
        else:
            response_xml = templates.SOAP_SUCCESS_RESPONSE.format(body_content="<error>Unknown Action</error>")

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