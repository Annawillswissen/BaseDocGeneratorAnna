import sys, os, docx, time
from docxcompose.composer import Composer
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from UI.Mainwindow.Mainwindow import Ui_MainWindow  # Pfad entsprechend anpassen
from DocGenerator import generate_document

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Management zwischen den combo boxen
        self.ui.cob_typ.currentIndexChanged.connect(self.cob_management)

        # Navigation Buttons
        self.ui.pb_Schnittstellen.clicked.connect(lambda: self.switch_widget(0))          #_test.clicked.connect(self.on_pb_test_clicked)
        self.ui.pb_SoO.clicked.connect(lambda: self.switch_widget(1))
        self.ui.pb_spare.clicked.connect(lambda: self.switch_widget(2))

        # start generating documents
        self.ui.pb_start.clicked.connect(self.generator)



    def cob_management(self):
        # Hole aktuell ausgewählten Anlagentyp
        current_text = self.ui.cob_typ.currentText()

        # Logik zur Steuerung der Sichtbarkeit der Einträge in Hardware Combo Box
        if current_text == "phs":
            # Wenn "phs" ausgewählt ist, blendet "hardwired" aus
            index = self.ui.cob_hardware.findText("hardwired")
            self.ui.cob_hardware.removeItem(index)
        else:
            # Stelle sicher, dass "Item B" vorhanden ist, wenn nicht "Option 1" gewählt ist
            if self.ui.cob_hardware.findText("hardwired") == -1:
                self.ui.cob_hardware.addItem("hardwired")


    def switch_widget(self,index):
        self.ui.sw_nav_bar.setCurrentIndex(index)

    
    def generator(self):

        # lösche Dialogfeld
        self.ui.lb_error.setText("")
        
        # hole Dateipfad, wo gespeichert werden soll
        filepath, _ = QFileDialog.getSaveFileName(
            self,
            "Dokument speichern unter",
            "Z:/vm_austausch/SS_Tool/",
            "Word Dokument (*.docx)",
        )

        # Überprüfe, ob ein Dateipfad ausgewählt wurde
        if filepath:
            try:
                generate_document(
                    "Z:/vm_austausch/SS_Tool/vorlagenpool",
                    self.ui.cob_typ.currentText(),
                    self.ui.cob_hardware.currentText(),
                    self.ui.cob_interlock_length.currentText(),
                    self.ui.cb_24_pins.isChecked(),
                    filepath
                )
                self.ui.lb_error.setText("Dokument erfolgreich gespeichert.")  # Erfolgsmeldung
            except PermissionError as e:
                self.ui.lb_error.setText(f"Fehler: Zugriff verweigert - {str(e)}")  # Zeigt den Fehler an
            except Exception as e:
                self.ui.lb_error.setText(f"Ein unbekannter Fehler ist aufgetreten: {str(e)}")  # Fängt andere mögliche Fehler
        else:
            self.ui.lb_error.setText("Kein Dateipfad ausgewählt.")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
