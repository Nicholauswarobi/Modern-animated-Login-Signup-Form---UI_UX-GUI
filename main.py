########################################################################
## IMPORTS
########################################################################
import sys

########################################################################
# IMPORT GUI FILE
from src.ui_login_interface import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
########################################################################
# IMPORT QAppSettings
from Custom_Widgets.QAppSettings import QAppSettings


########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        # Use this to specify your json file(s) path/name
        loadJsonStyle(self, self.ui, jsonFiles = {"json-styles\login_styles.json"
            }) 
        ########################################################################
        # Apply them style, genarate icons
        QAppSettings.updateAppSettings(self)
        
        ########################################################################

        self.show()


########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
