import requests
from utils import get_result

wsdl_file = 'http://nlptools.info.uaic.ro/WebPosRo/PosTaggerRoWS?wsdl'
headers = {'content-type': 'text/xml'}

rqe_parse_sentence_text = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webPosRo.uaic/">
   <soapenv:Header/>
   <soapenv:Body>
      <web:parseSentence_TXT>
         <rawSentenceInput>{text}</rawSentenceInput>
      </web:parseSentence_TXT>
   </soapenv:Body>
</soapenv:Envelope>"""

rqe_parse_sentence_xml = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webPosRo.uaic/">
   <soapenv:Header/>
   <soapenv:Body>
      <web:parseSentence_XML>
         <rawSentenceInput>{xml}</rawSentenceInput>
      </web:parseSentence_XML>
   </soapenv:Body>
</soapenv:Envelope>"""

rqe_parse_text_text = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webPosRo.uaic/">
   <soapenv:Header/>
   <soapenv:Body>
      <web:parseText_TXT>
         <rawTextInput>{text}</rawTextInput>
      </web:parseText_TXT>
   </soapenv:Body>
</soapenv:Envelope>"""

rqe_parse_text_xml = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webPosRo.uaic/">
   <soapenv:Header/>
   <soapenv:Body>
      <web:parseText_XML>
         <rawTextInput>{xml}</rawTextInput>
      </web:parseText_XML>
   </soapenv:Body>
</soapenv:Envelope>"""


def parse_sentence_text(text):
    print("Creating request")
    body = rqe_parse_sentence_text.format(text=text)
    print("Request sent to server")
    response = requests.post(wsdl_file, data=body, headers=headers)
    print("Response received")
    return get_result(response)


def parse_sentence_xml(xml):
    print("Creating request")
    body = rqe_parse_sentence_xml.format(xml=xml).encode("utf-8")
    print("Request sent to server")
    response = requests.post(wsdl_file, data=body, headers=headers)
    print("Response received")
    return get_result(response)


def parse_text_text(text):
    print("Creating request")
    body = rqe_parse_text_text.format(text=text).encode("utf-8")
    print("Request sent to server")
    response = requests.post(wsdl_file, data=body, headers=headers)
    print("Response received")
    return get_result(response)


def parse_text_xml(xml):
    print("Creating request")
    body = rqe_parse_text_xml.format(xml=xml).encode("utf-8")
    print("Request sent to server")
    response = requests.post(wsdl_file, data=body, headers=headers)
    print("Response received")
    return get_result(response)
