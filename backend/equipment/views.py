from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from .models import Dataset
from .utils import analyze_csv
from reportlab.pdfgen import canvas
from django.http import FileResponse


class CsrfExemptSessionAuthentication(BaseAuthentication):
    def authenticate(self, request):
        return None


class UploadCSV(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = []

    def post(self, request):
        if "file" not in request.FILES:
            return Response({"error": "No file uploaded"}, status=400)

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
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = []

    def get(self, request):
        return Response(list(Dataset.objects.values()))


class PDFReport(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = []

    def get(self, request):
        dataset = Dataset.objects.last()
        if not dataset:
            return Response({"error": "No data available"}, status=400)

        c = canvas.Canvas("report.pdf")
        y = 800
        for k, v in dataset.summary.items():
            c.drawString(50, y, f"{k}: {v}")
            y -= 20
        c.save()

        return FileResponse(open("report.pdf", "rb"), as_attachment=True)
