# upload_file.py
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
import os

#delete previosly uploaded files.
def delete_uploaded_files(document_path):
    for filename in os.listdir(document_path):
        file_path = os.path.join(document_path, filename)
        os.remove(file_path)


def upload_files(request):
    if request.method == 'POST':
        request_file = request.FILES.get('document')

        fs = FileSystemStorage()
        uploaded = False

        if request_file:
            if request_file.name.endswith(('.jpg', '.jpeg', '.png')):
                fs.save(request_file.name, request_file)
                uploaded = True

                filename = request_file.name
                filepath = os.path.join('./media')

            return filename, filepath