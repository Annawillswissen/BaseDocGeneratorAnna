import os
from docxcompose.composer import Composer
from docx import Document

def generate_document(base_path, cob_typ, cob_hardware, cob_interlock_length, cb_24_pins, filepath):
    # erzeuge Pfad für Anlagentyp
    path = os.path.join(base_path, cob_typ)

    # erzeuge Basis Dokument
    basedoc = Document(os.path.join(path, "1_head", "head.docx"))

    # restliche Dokumente zum zusammenführen
    snippet_list = []

    # Hardware
    snippet_list.append(os.path.join(path, "2_hardware", cob_hardware, cob_hardware + "_" + cob_interlock_length + ".docx"))
    
    # Wenn Option 24-poliger Stecker, füge Seite ein
    if cb_24_pins:
        snippet_list.append(os.path.join(path, "2_hardware", "optional_24pol", "optional_24pol.docx"))
    
    # Safety Signals
    if cb_24_pins:
        snippet_list.append(os.path.join(path, "3_safety_signals", "safety_24pol", "safety_24pol.docx"))
    else:
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
    
    # Dokument speichern              
    composer.save(filepath)
