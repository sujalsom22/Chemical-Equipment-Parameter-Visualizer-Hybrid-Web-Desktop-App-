# Chemical Equipment Parameter Visualizer  
Hybrid Web + Desktop Application

---

## 📌 Project Overview
The Chemical Equipment Parameter Visualizer is a hybrid application designed to analyze and visualize parameters of chemical equipment. Users can upload a CSV file containing equipment details, and the system generates summary statistics and visual insights. A single Django REST backend is shared by both a React-based web application and a PyQt5-based desktop application.

---

## 🧱 System Architecture

React Web App        PyQt5 Desktop App  
        |                     |  
        |------ REST API -----|  
                    |  
            Django REST Backend  
                    |  
              Pandas Analytics  
                    |  
              SQLite Database  

---

## 🛠️ Tech Stack

### Backend
- Python
- Django
- Django REST Framework
- Pandas
- SQLite
- Gunicorn

### Frontend (Web)
- React.js
- Chart.js
- HTML / CSS / JavaScript

### Frontend (Desktop)
- PyQt5
- Matplotlib
- Requests

---

## ✨ Features
- CSV upload for chemical equipment data
- Automatic data parsing and validation
- Summary statistics (averages, counts)
- Equipment type distribution analysis
- Interactive web charts using Chart.js
- Desktop visualizations using Matplotlib
- Storage of last 5 uploaded datasets
- PDF report generation
- Shared backend for web and desktop clients

---

## 🚀 Running the Project Locally
### Backend Setup
cd backend
pip install -r requirements.txt
python manage.py runserver


### Backend runs at:

http://127.0.0.1:8000

### Web Frontend (React)
cd web-frontend
npm install
npm start


### Web app runs at:

http://localhost:3000

### Desktop Application (PyQt5)
cd desktop-app
python app.py

## 🌐 Deployment

Backend deployed on Render using Gunicorn

Web frontend deployed on Netlify

Desktop application runs locally and consumes the same deployed backend APIs

### 🔗 API Endpoints

POST /api/upload/
Upload CSV file and receive summary statistics

GET /api/history/
Retrieve history of last 5 uploaded datasets

GET /api/report/
Download PDF summary report

## 🏁 Conclusion

This project demonstrates full-stack development using Django REST Framework, data analytics with Pandas, and multi-platform frontend integration. It highlights clean architecture, reusable backend logic, and effective data visualization across web and desktop platforms.