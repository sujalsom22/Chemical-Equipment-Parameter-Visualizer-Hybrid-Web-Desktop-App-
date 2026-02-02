import sys
import requests
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QFileDialog,
    QLabel,
    QVBoxLayout,
    QMessageBox
)

BACKEND_URL = "http://127.0.0.1:8000/api/upload/"

class ChemicalEquipmentApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Visualizer (Desktop)")
        self.setGeometry(300, 200, 400, 200)

        self.label = QLabel("Upload a CSV file to visualize data")
        self.button = QPushButton("Upload CSV")
        self.button.clicked.connect(self.upload_csv)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def upload_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select CSV File", "", "CSV Files (*.csv)"
        )

        if not file_path:
            return

        try:
            with open(file_path, "rb") as f:
                response = requests.post(
                    BACKEND_URL,
                    files={"file": f},
                    timeout=30
                )

            if response.status_code != 200:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"Upload failed (status {response.status_code})"
                )
                return

            summary = response.json()
            self.show_charts(summary)

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def show_charts(self, summary):
        # Chart 1: Equipment Type Distribution
        plt.figure(figsize=(8, 5))
        plt.bar(
            summary["type_distribution"].keys(),
            summary["type_distribution"].values()
        )
        plt.title("Equipment Type Distribution")
        plt.xlabel("Equipment Type")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.show()

        # Chart 2: Average Flowrate by Type
        plt.figure(figsize=(8, 5))
        plt.bar(
            summary["avg_flowrate_by_type"].keys(),
            summary["avg_flowrate_by_type"].values()
        )
        plt.title("Average Flowrate by Equipment Type")
        plt.xlabel("Equipment Type")
        plt.ylabel("Flowrate")
        plt.tight_layout()
        plt.show()

        # Chart 3: Average Pressure by Type
        plt.figure(figsize=(8, 5))
        plt.plot(
            list(summary["avg_pressure_by_type"].keys()),
            list(summary["avg_pressure_by_type"].values()),
            marker="o"
        )
        plt.title("Average Pressure by Equipment Type")
        plt.xlabel("Equipment Type")
        plt.ylabel("Pressure")
        plt.tight_layout()
        plt.show()

        # Chart 4: Average Temperature by Type
        plt.figure(figsize=(8, 5))
        plt.plot(
            list(summary["avg_temperature_by_type"].keys()),
            list(summary["avg_temperature_by_type"].values()),
            marker="o"
        )
        plt.title("Average Temperature by Equipment Type")
        plt.xlabel("Equipment Type")
        plt.ylabel("Temperature")
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChemicalEquipmentApp()
    window.show()
    sys.exit(app.exec_())
