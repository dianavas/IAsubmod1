import requests
from utils import get_result, validate_language

wsdl_file = 'http://nlptools.info.uaic.ro/UAIC.AnaphoraResolution/AnaphoraResolutionWS?wsdl'
headers = {'content-type': 'text/xml'}

rqt_solve_links = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:res="http://resolution.anaphora.uaic/">
   <soapenv:Header/>
   <soapenv:Body>
      <res:solveLinks>
         <text>{text}</text>
         <language>{language}</language>
      </res:solveLinks>
   </soapenv:Body>
</soapenv:Envelope>"""

rqt_solve_links_xml = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:res="http://resolution.anaphora.uaic/">
   <soapenv:Header/>
   <soapenv:Body>
      <res:solveLinks_XML>
         <xml>{xml}</xml>
         <language>{language}</language>
      </res:solveLinks_XML>
   </soapenv:Body>
</soapenv:Envelope>"""


def solve_links(text, language="ro"):
    validate_language(language)
    print("Creating request")
    body = rqt_solve_links.format(text=text, language=language)
    print("Request sent to server")
    response = requests.post(wsdl_file, data=body, headers=headers)
    print("Response received")
    return get_result(response)


def solve_links_xml(xml, language="ro"):
    validate_language(language)
    print("Creating request")
    body = rqt_solve_links_xml.format(xml=xml, language=language)
    print("Request sent to server")
    response = requests.post(wsdl_file, data=body, headers=headers)
    print("Response received")
    return get_result(response)
