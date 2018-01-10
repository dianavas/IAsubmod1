import requests
from utils import get_result, validate_language
from xml.dom import minidom

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
    body = rqt_solve_links.format(text=text, language=language).encode("utf-8")
    print("Request sent to server")
    response = requests.post(wsdl_file, data=body, headers=headers)
    print("Response received")
    return get_result(response)


def solve_links_xml(xml, language="ro"):
    validate_language(language)
    print("Creating request")
    body = rqt_solve_links_xml.format(xml=xml, language=language).encode("utf-8")
    print("Request sent to server")
    response = requests.post(wsdl_file, data=body, headers=headers)
    print("Response received")
    return get_result(response)


def match(pronoun, noun):
    if noun.attributes["POS"].value != "NOUN":
        return False
    if not noun.hasAttribute("Gender") or not pronoun.hasAttribute("Gender"):
        return False
    if not noun.hasAttribute("Number") or not pronoun.hasAttribute("Number"):
        return False
    if pronoun.attributes["Gender"].value != noun.attributes["Gender"].value:
        return False
    if pronoun.attributes["Number"].value != noun.attributes["Number"].value:
        return False
    return True


def solve_links_manual(xml):
    xmldoc = minidom.parseString(xml)
    sentences = xmldoc.getElementsByTagName("S")
    search_list = []
    for s in sentences:
        words = s.getElementsByTagName("W")
        for w in words:
            if w.hasAttribute("POS") and (w.attributes["POS"].value == "NOUN" or w.attributes["POS"].value == "PRONOUN"):
                search_list.append(w)
    anaphoras = []

    for i in range(0, len(search_list)):
        if (search_list[i].attributes["POS"].value == "PRONOUN"):
            for j in reversed(range(0, i)):
                if match(search_list[i], search_list[j]):
                    anaphoras.append((search_list[i].attributes["id"].value, search_list[j].attributes["LEMMA"].value))
                    search_list[i].setAttribute("ANAPHORA", search_list[j].attributes["LEMMA"].value)
                    break

    for a in anaphoras:
        data = "id=\"" + a[0] + "\""
        xml = xml[:xml.index(data) + len(data)] + " ANAPHORA=\"" + a[1] + "\"" + xml[xml.index(data) + len(
            data):]

    return xml
