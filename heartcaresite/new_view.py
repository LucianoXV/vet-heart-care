from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .forms import PDFUploadForm, NameForm, DataConfirmationForm
import pdfplumber
from docx import Document
from datetime import datetime, date
from .models import Owner, Pet, CardiacData
import os
import pg8000

class UploadPDFView(View):
    def get(self, request):
        form = PDFUploadForm()
        return render(request, 'heartcaresite/upload_pdf.html', {'form': form})

    def post(self, request):
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data['pdf_file']
            # Process the PDF file (e.g., extract data)

            # Extract table data from PDF
            table_data = []
            with pdfplumber.open(pdf_file) as pdf:
                for page in pdf.pages:
                    tables = page.extract_tables()
                    for table in tables:
                        table_data.extend(table)
            request.session['table_data'] = table_data
            return redirect('data_confirmation')
        else:
            return render(request, 'heartcaresite/upload_pdf.html', {'form': form})

class DataConfirmationView(View):
    def get(self, request):
        table_data = request.session.get('table_data', {})
        # Extracting table data...

        form = DataConfirmationForm(initial={
            # Populate form fields...
        })

        return render(request, 'heartcaresite/data_confirmation.html', {'form': form})

    def post(self, request):
        form = DataConfirmationForm(request.POST)
        if form.is_valid():
            # Process and save data...
            return redirect('view_save_doc')
        else:
            # Handle invalid form
            return render(request, 'heartcaresite/data_confirmation.html', {'form': form})

class ViewSaveDocView(View):
    def get(self, request):
        form = DataConfirmationForm(request.GET)
        if form.is_valid():
            file_path = request.session.get('file_path')
            if file_path and os.path.exists(file_path):
                with open(file_path, 'rb') as file:
                    response = HttpResponse(file.read(), content_type='application/octet-stream')
                    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
                    return response
            else:
                return HttpResponse("File not found")
        return HttpResponse("File path is None")

class SuccessPageView(View):
    def get(self, request):
        return render(request, 'heartcaresite/docx_successpage.html')
