from PyQt5 import QtWidgets, QtGui, QtCore
from idga import Ui_MainWindow  # importing our generated file

import sys
import json
import difflib

data = json.load(open("dictionary.json"))


class Idga(QtWidgets.QMainWindow):
    def __init__(self):
        super(Idga, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.start_search.clicked.connect(self.search_button_clicked)
        self.ui.results_list.itemSelectionChanged.connect(self.result_list_changed)
        self.ui.exit_button.clicked.connect(self.exit_button_clicked)
        self.ui.search_text.returnPressed.connect(self.search_button_clicked)

    def result_list_changed(self):
        selected_items = self.ui.results_list.selectedItems()
        if len(selected_items) > 0:
            item = self.ui.results_list.selectedItems()[0].text()
            text = '\n\n'.join(data[item])
            self.ui.result_textbox.setText(text)

    def search_button_clicked(self):
        self.ui.results_list.clear()
        self.ui.result_textbox.clear()
        search = self.ui.search_text.text()
        results = [key for key in data.keys()
                   if difflib.SequenceMatcher(None, search.lower(), key.lower()).ratio() >= 0.9]

        if len(results) > 0:
            self.ui.results_list.setEnabled(True)
            for result in results:
                self.ui.results_list.addItem(result)
        else:
            self.ui.results_list.setEnabled(False)
            self.ui.results_list.addItem('nothing found')

    def exit_button_clicked(self):
        QtCore.QCoreApplication.instance().quit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = Idga()
    application.show()
    sys.exit(app.exec())
