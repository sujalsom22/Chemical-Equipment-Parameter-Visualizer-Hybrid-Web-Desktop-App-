from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Dataset
from .utils import analyze_csv
from reportlab.pdfgen import canvas
from django.http import FileResponse

class UploadCSV(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file = request.FILES["file"]
        summary = analyze_csv(file)

        if Dataset.objects.count() >= 5:
            Dataset.objects.first().delete()

        Dataset.objects.create(
            filename=file.name,
            summary=summary
        )

        return Response(summary)


class History(APIView):
    def get(self, request):
        return Response(list(Dataset.objects.values()))


class PDFReport(APIView):
    def get(self, request):
        dataset = Dataset.objects.last()
        c = canvas.Canvas("report.pdf")

        y = 800
        for k, v in dataset.summary.items():
            c.drawString(50, y, f"{k}: {v}")
            y -= 20

        c.save()
        return FileResponse(open("report.pdf", "rb"), as_attachment=True)
