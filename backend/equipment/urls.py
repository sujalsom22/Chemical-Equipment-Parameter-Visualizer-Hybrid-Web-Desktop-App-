from django.urls import path
from .views import UploadCSV, History, PDFReport

urlpatterns = [
    path("upload/", UploadCSV.as_view()),
    path("history/", History.as_view()),
    path("report/", PDFReport.as_view()),
]
