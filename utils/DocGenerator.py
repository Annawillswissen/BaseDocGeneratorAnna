import os
from docxcompose.composer import Composer
from docx import Document
from utils.replaceContent import setTextToContentControl

from docx import Document
from docx.oxml import OxmlElement




# import win32com.client as win32

# def update_toc(filepath):
#     try:
#         word = win32.Dispatch("Word.Application")
#         word.Visible = False  # Word-Fenster nicht anzeigen
#         doc = word.Documents.Open(filepath)
#         doc.TablesOfContents(1).Update()
#         doc.Close(SaveChanges=True)
#         word.Quit()
#     except Exception as e:
#         print(f"Ein Fehler ist aufgetreten: {e}")

# # Pfad zum Word-Dokument
# filepath = 'path/to/your/document.docx'
# update_toc(filepath)




def generate_document(params):

    # drösle dictionary auf und speicher in lokale variablen
    base_path = params['path_doc_pool']
    cob_typ = params['typ']
    cob_hardware = params['hardware']
    cob_interlock_length = params['interlock_length']
    cob_safety = params['safety']
    cob_harting = params['harting']
    filepath = params['save_filepath']
    fn_number = params['fn_number']
    project_name = params['project_name']
    customer = params['customer']
    firstname = params['firstname']
    lastname = params['lastname']
    email = params['email']
    phone = params['phone']
    
    # erzeuge Pfad für Anlagentyp
    path = os.path.join(base_path, cob_typ)

    # erzeuge Basis Dokument
    basedoc = Document(os.path.join(path, "1_head", "head.docx"))

    # restliche Dokumente zum zusammenführen
    snippet_list = []

    # Hardware
    if cob_hardware == "hardwired":
        snippet_list.append(os.path.join(path, "2_hardware", cob_hardware, cob_hardware + ".docx"))
    else:
        snippet_list.append(os.path.join(path, "2_hardware", cob_hardware, cob_hardware + "_" + cob_interlock_length + ".docx"))
    
    # 24-poliger Ja/Nein
    if cob_harting == "Ja":
        snippet_list.append(os.path.join(path, "2_hardware", "optional_24pol", "optional_24pol.docx"))
    
    # Safety Signals
    if cob_safety == "24-pol":
        snippet_list.append(os.path.join(path, "3_safety_signals", "safety_24pol", "safety_24pol.docx"))

    elif cob_safety == "Profisafe":
        snippet_list.append(os.path.join(path, "3_safety_signals", "profisafe.docx"))

    # Standard Signals
    snippet_list.append(os.path.join(path, "4_standard_signals", "signals.docx"))

    # End 
    snippet_list.append(os.path.join(path, "5_end", "end.docx"))

    # erzeuge Composer Objekt
    composer = Composer(basedoc)

    # erzeuge Seitenumbruch nach erster Seite
    basedoc.add_page_break()

    # füge alle restlichen snippets hinzu
    for i, snippet in enumerate(snippet_list):
        tmp_object = Document(snippet)
        
        # Bei letztem Snippet keinen Pagebreak mehr
        if i < len(snippet_list)-1:
            tmp_object.add_page_break()

        composer.append(tmp_object)
    

    # Felder manipulieren vor dem Speichern
    setTextToContentControl(composer.doc, "Projektname", project_name)
    setTextToContentControl(composer.doc, "Auftragsnummer", fn_number)
    setTextToContentControl(composer.doc, "Kunde", customer)
    setTextToContentControl(composer.doc, "Kontakt", firstname + " " + lastname + " (LVT)")
    setTextToContentControl(composer.doc, "Mail", email)
    setTextToContentControl(composer.doc, "Telefon", phone)

    # Dokument speichern
    #update_table_of_contents(composer.doc)
    composer.save(filepath)
