import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from UI.Mainwindow.Mainwindow import Ui_MainWindow
from utils.DocGenerator import generate_document

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Management zwischen den combo boxen
        self.ui.cob_typ.currentIndexChanged.connect(self.cob_typ_management)
        self.ui.cob_safety.currentIndexChanged.connect(self.cob_safety_management)
        self.ui.cob_hardware.currentIndexChanged.connect(self.cob_hw_management)

        # Navigation Buttons
        self.ui.pb_Schnittstellen.clicked.connect(lambda: self.switch_widget(0))
        self.ui.pb_SoO.clicked.connect(lambda: self.switch_widget(1))
        self.ui.pb_spare.clicked.connect(lambda: self.switch_widget(2))

        # start generating documents
        self.ui.pb_start.clicked.connect(self.generator)



    def cob_typ_management(self):
        # Hole aktuell ausgewählten Anlagentyp
        current_text = self.ui.cob_typ.currentText()

        # Logik zur Steuerung der Sichtbarkeit der Einträge in Hardware Combo Box
        if current_text == "phs":
            # Wenn "phs" ausgewählt ist, blendet "hardwired" aus
            index = self.ui.cob_hardware.findText("hardwired")
            self.ui.cob_hardware.removeItem(index)
        else:
            # Stelle sicher, dass item vorhanden ist, wenn nicht "Option 1" gewählt ist
            if self.ui.cob_hardware.findText("hardwired") == -1:
                self.ui.cob_hardware.addItem("hardwired")

    def cob_safety_management(self):
        # Hole aktuell ausgewählte safety variante
        current_text = self.ui.cob_safety.currentText()

        # Logik zur Steuerung der Sichtbarkeit der Einträge bezüglich 24-pol. Stecker
        if current_text == "24-pol":
            # Wenn safety 24-pol ausgewählt ist, blende Harting "Nein" aus
            index = self.ui.cob_harting.findText("Nein")
            self.ui.cob_harting.removeItem(index)
        else:
            # Stelle sicher, dass item vorhanden ist, wenn nicht safety "Profisafe" gewählt ist
            if self.ui.cob_harting.findText("Nein") == -1:
                self.ui.cob_harting.addItem("Nein")

                # wähle "Nein" vor
                index = self.ui.cob_harting.findText("Nein")
                self.ui.cob_harting.setCurrentIndex(index)


    def cob_hw_management(self):
        # Hole aktuell ausgewählten Anlagentyp
        current_text = self.ui.cob_hardware.currentText()

        # wenn hardware == profibus, blende Profisafe aus
        if current_text == "profibus" or current_text == "hardwired":
            # Wenn "profibus" ausgewählt ist, blende "Profisafe" aus
            index = self.ui.cob_safety.findText("Profisafe")
            self.ui.cob_safety.removeItem(index)

        elif current_text == "profinet":
            # füge Profisafe hinzu wenn Profinet angewählt ist
            if self.ui.cob_safety.findText("Profisafe") == -1:
                self.ui.cob_safety.addItem("Profisafe")

        if current_text == "hardwired":
            self.ui.lb_interlock_length.setHidden(True)
            self.ui.cob_interlock_length.setHidden(True)
        else:
            self.ui.lb_interlock_length.setHidden(False)
            self.ui.cob_interlock_length.setHidden(False)

            

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
                    self.ui.cob_safety.currentText(),
                    self.ui.cob_harting.currentText(),
                    filepath,
                    self.ui.le_fn_number.text(),
                    self.ui.le_project_name.text(),
                    self.ui.le_customer.text(),
                    self.ui.le_firstname.text(),
                    self.ui.le_lastname.text(),
                    self.ui.le_email.text(),
                    self.ui.le_phone.text()

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
