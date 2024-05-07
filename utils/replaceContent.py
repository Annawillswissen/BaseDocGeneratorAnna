from docx import Document
from docx.oxml.ns import qn

def setTextToContentControl(doc, tagname, texttoset):
    """
    Diese Funktion setzt den Text für ein Inhaltssteuerelement basierend auf seinem Alias.
    Alle Textelemente innerhalb des Steuerelements werden durch 'texttoset' ersetzt.
    """
    # Access the underlying xml element of the document
    for element in doc.element.xpath(".//w:sdt"):
        alias = element.find('.//w:alias', namespaces={'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'})
        if alias is not None and alias.get(qn('w:val')) == tagname:
            content_elements = element.findall('.//w:t', namespaces={'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'})
            if content_elements:
                # Setze den Text des ersten Elements und lösche den Text der restlichen Elemente
                content_elements[0].text = texttoset
                for content in content_elements[1:]:
                    content.text = ''
                return True  # Bei erfolgreichem Update
    return False  # Wenn kein passendes Inhaltssteuerelement gefunden wird
