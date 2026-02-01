import requests
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
import sys

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Desktop App")
        btn = QPushButton("Upload CSV", self)
        btn.clicked.connect(self.upload)

    def upload(self):
        file, _ = QFileDialog.getOpenFileName()
        r = requests.post(
            "http://127.0.0.1:8000/api/upload/",
            files={"file": open(file, "rb")},
            auth=("admin", "password"),
        )
        dist = r.json()["type_distribution"]
        plt.bar(dist.keys(), dist.values())
        plt.show()

app = QApplication(sys.argv)
w = App()
w.show()
sys.exit(app.exec_())
