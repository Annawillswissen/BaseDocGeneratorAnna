import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from UI.Mainwindow.Mainwindow import Ui_MainWindow  # Pfad entsprechend anpassen

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Verbinde den Button-Klick mit der on_pb_test_clicked Funktion
        self.ui.pb_Schnittstellen.clicked.connect(self.switch_to_Interlocks)          #_test.clicked.connect(self.on_pb_test_clicked)
        self.ui.pb_SoO.clicked.connect(self.switch_to_SoO)
        self.ui.pb_spare.clicked.connect(self.switch_to_spare)






    def switch_to_Interlocks(self):
        self.ui.sw_test.setCurrentIndex(0)

    def switch_to_SoO(self):
        self.ui.sw_test.setCurrentIndex(1)

    def switch_to_spare(self):
        self.ui.sw_test.setCurrentIndex(2)
        
        










if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
