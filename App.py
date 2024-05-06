import sys, os, docx
from docxcompose.composer import Composer
from PySide6.QtWidgets import QApplication, QMainWindow
from UI.Mainwindow.Mainwindow import Ui_MainWindow  # Pfad entsprechend anpassen

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Navigation Buttons
        self.ui.pb_Schnittstellen.clicked.connect(lambda: self.switch_widget(0))          #_test.clicked.connect(self.on_pb_test_clicked)
        self.ui.pb_SoO.clicked.connect(lambda: self.switch_widget(1))
        self.ui.pb_spare.clicked.connect(lambda: self.switch_widget(2))

        # start generating documents
        self.ui.pb_start.clicked.connect(self.generator)






    def switch_widget(self,index):
        self.ui.sw_nav_bar.setCurrentIndex(index)

    
    def generator(self):

        # Basispfad zu den Vorlagen
        base_path = "Z:/vm_austausch/SS_Tool/vorlagenpool"
        
        # erzeuge Pfad für Anlagentyp
        path = os.path.join(base_path, self.ui.cob_typ.currentData)

        # erzeuge Basis Dokument
        basedoc = docx.Document(os.path.join(path, "1_head", "head.docx"))

        # restliche Dokumente zum zusammenführen
        snippet_list = []

        # Hardware
        snippet_list.append(os.path.join(path, "2_hardware", self.ui.cob_hardware.currentData, self.ui.cob_hardware.currentData + "_" + self.ui.cob_interlock_length.currentData + ".docx"))
        
        # Wenn Option 24-poliger Stecker, füge Seite ein
        if self.ui.cb_24_pins.isChecked == True:
            snippet_list.append(os.path.join(path, "2_hardware", "optional_24pol", "optional_24pol.docx"))
        
        # Safety Signals
        if self.ui.cb_24_pins.isChecked == True:
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
            tmp_object = docx.Document(snippet)
            
            # Bei letztem Snippet keinen Pagebreak mehr
            if i < len(snippet_list)-1:
                tmp_object.add_page_break()

            composer.append(tmp_object)
            
            
        # neues Dokument speichern
        
        composer.save('Z:/vm_austausch/merged_document.docx')









if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
