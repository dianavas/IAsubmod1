import requests

wsdl_file = 'http://nlptools.info.uaic.ro/UAIC.AnaphoraResolution/AnaphoraResolutionWS?wsdl'

request_envelope = """<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://resolution.anaphora.uaic/">
  <SOAP-ENV:Body>
    <ns1:solveLinks>
      <text>{text}</text>
      <language>{language}</language>
    </ns1:solveLinks>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>"""


def solve_anaphora_resolution(text, language):
    languages_supported = ['ro']
    if language not in languages_supported:
        message = "Language \"%(language)s\" is not supported." % {"language": language}
        raise Exception(message)
    print("Creating request")
    headers = {'content-type': 'text/xml'}
    body = request_envelope.format(text=text, language=language)
    print("Request sent to server")
    response = requests.post(wsdl_file, data=body, headers=headers)
    print("Response received")
    result = str(response.content).split("<return>")[1].split("</return>")[0]
    if result == "":
        result = "No result from server :("
    return result
