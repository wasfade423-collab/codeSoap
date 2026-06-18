SOAP_SUCCESS_RESPONSE = """<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:smart="http://smartport.lacotonou.bj/">
   <soapenv:Header/>
   <soapenv:Body>
      {body_content}
   </soapenv:Body>
</soapenv:Envelope>"""

WSDL_CONTENT = """<?xml version="1.0" encoding="UTF-8"?>
<wsdl:definitions name="SmartPortSoap"
    targetNamespace="http://smartport.lacotonou.bj/"
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
    xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
    xmlns:tns="http://smartport.lacotonou.bj/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">

    <wsdl:types>
        <xsd:schema targetNamespace="http://smartport.lacotonou.bj/">
            <xsd:element name="GetDossierRequest">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element name="reference_metier" type="xsd:string"/>
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="GetDossierResponse">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element name="id" type="xsd:int"/>
                        <xsd:element name="statut" type="xsd:string"/>
                        <xsd:element name="type_operation" type="xsd:string"/>
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>

            <xsd:element name="CreateDossierRequest">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element name="reference_metier" type="xsd:string"/>
                        <xsd:element name="statut" type="xsd:string"/>
                        <xsd:element name="type_operation" type="xsd:string"/>
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="CreateDossierResponse">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element name="success" type="xsd:boolean"/>
                        <xsd:element name="message" type="xsd:string"/>
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
        </xsd:schema>
    </wsdl:types>

    <wsdl:message name="GetDossierRequestMessage"><wsdl:part name="parameters" element="tns:GetDossierRequest"/></wsdl:message>
    <wsdl:message name="GetDossierResponseMessage"><wsdl:part name="parameters" element="tns:GetDossierResponse"/></wsdl:message>
    <wsdl:message name="CreateDossierRequestMessage"><wsdl:part name="parameters" element="tns:CreateDossierRequest"/></wsdl:message>
    <wsdl:message name="CreateDossierResponseMessage"><wsdl:part name="parameters" element="tns:CreateDossierResponse"/></wsdl:message>

    <wsdl:portType name="SmartPortPortType">
        <wsdl:operation name="GetDossier">
            <wsdl:input message="tns:GetDossierRequestMessage"/>
            <wsdl:output message="tns:GetDossierResponseMessage"/>
        </wsdl:operation>
        <wsdl:operation name="CreateDossier">
            <wsdl:input message="tns:CreateDossierRequestMessage"/>
            <wsdl:output message="tns:CreateDossierResponseMessage"/>
        </wsdl:operation>
    </wsdl:portType>

    <wsdl:binding name="SmartPortSoapBinding" type="tns:SmartPortPortType">
        <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
        <wsdl:operation name="GetDossier">
            <soap:operation soapAction="GetDossier"/>
            <wsdl:input><soap:body use="literal"/></wsdl:input>
            <wsdl:output><soap:body use="literal"/></wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="CreateDossier">
            <soap:operation soapAction="CreateDossier"/>
            <wsdl:input><soap:body use="literal"/></wsdl:input>
            <wsdl:output><soap:body use="literal"/></wsdl:output>
        </wsdl:operation>
    </wsdl:binding>

    <wsdl:service name="SmartPortSoapService">
        <wsdl:port name="SmartPortSoapPort" binding="tns:SmartPortSoapBinding">
            <soap:address location="https://smartport-soap-api.onrender.com/"/>
        </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
"""