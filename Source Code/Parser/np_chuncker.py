import requests
from utils import get_result

wsdl_file = 'http://nlptools.info.uaic.ro/WebNpChunkerRo/NpChunkerRoWS?wsdl'
headers = {'content-type': 'text/xml'}

rqe_chunck_tagget_text = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webNpChunkerRo.uaic/">
   <soapenv:Header/>
   <soapenv:Body>
      <web:chunkTaggedText>
         <taggedXml>{xml}</taggedXml>
      </web:chunkTaggedText>
   </soapenv:Body>
</soapenv:Envelope>"""

rqe_chunck_text = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webNpChunkerRo.uaic/">
   <soapenv:Header/>
   <soapenv:Body>
      <web:chunkText>
         <inputText>{text}</inputText>
      </web:chunkText>
   </soapenv:Body>
</soapenv:Envelope>"""


def chunck_tagget_text(xml):
    print("Creating request")
    body = rqe_chunck_tagget_text.format(xml=xml).encode("utf-8")
    print("Request sent to server")
    response = requests.post(wsdl_file, data=body, headers=headers)
    print("Response received")
    return get_result(response)


def chunck_text(text):
    print("Creating request")
    body = rqe_chunck_text.format(text=text).encode("utf-8")
    print("Request sent to server")
    response = requests.post(wsdl_file, data=body, headers=headers)
    print("Response received")
    return get_result(response)
