#XML SCHEMA
"""
->Description of the legaL format of XML document
->Expressed in terms of contraints on the structure and content of document
->often used to specif a "contract between system - "my system will only accept Xml that conforms to this particular
schema

-> if a particular piece of XML meets the specification of the schema 
-> it is said to "validate"

Document type Defintion DTD)

"""

#Many XML Schema Languages 

"""
Document TYpe Definition(DTD)

Satandar Generalized Markup Languajes(ISO 8879:1986 SGML)

XML SCHEMA from W3C(XSD)

XSD es un lenguaje de esquema utilizado para describir la estructura y las restricciones de los contenidos de documentos TIPO XML
de una forma muy precisa 

XS: ELement
xs: sequence 
xs:complex type

"""
import xml.etree.ElementTree as ET
data = '''<person>
    <name>chuck</name>
    <phone type = "intl"<
    +1234324
    </phone>
    <email hide = "yes"/>
    </person>'''
tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

