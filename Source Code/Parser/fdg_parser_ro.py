import requests
from utils import get_result

wsdl_file = 'http://nlptools.info.uaic.ro/WebFdgRo/FdgParserRoWS?wsdl'
headers = {'content-type': 'text/xml'}

rqt_parse_pos_tagged_text = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webFdgRo.uaic/">
   <soapenv:Header/>
   <soapenv:Body>
      <web:parsePosTaggedXML>
         <posTaggedXML>{xml}</posTaggedXML>
      </web:parsePosTaggedXML>
   </soapenv:Body>
</soapenv:Envelope>"""

rqt_parse_text = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webFdgRo.uaic/">
   <soapenv:Header/>
   <soapenv:Body>
      <web:parseText>
         <txt>{text}</txt>
      </web:parseText>
   </soapenv:Body>
</soapenv:Envelope>"""


def parse_pos_tagget_text(text):
    print("Creating request")
    body = rqt_parse_pos_tagged_text.format(xml=text)
    print("Request sent to server")
    response = requests.post(wsdl_file, data=body, headers=headers)
    print("Response received")
    return get_result(response)


def parse_text(text):
    print("Creating request")
    body = rqt_parse_text.format(text=text)
    print("Request sent to server")
    response = requests.post(wsdl_file, data=body, headers=headers)
    print("Response received")
    return get_result(response)
