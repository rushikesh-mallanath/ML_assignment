from django.shortcuts import render

from .blue_text import extract_blue_text
from .text_extract import text_extract
from .upload_file import upload_files
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_200_OK
from django.views.decorators.csrf import csrf_exempt

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
print('PATH IS ::', BASE_DIR)


class ExtractImage(APIView):
    @csrf_exempt
    def post(self,request):
        
        #upload input image, using below function
        filename, filepath = upload_files(request)
        print(fr'File uploaded named : {filename}')
        print(fr'File uploaded path : {filepath}')

        try:
            output_path = BASE_DIR
            #get blue text and mask it, using below function
            result = extract_blue_text(filepath, output_path)

            #get extracted text from this function
            text = text_extract(result)
        except Exception as e:
            print('error is ::', e)

        return Response(text, status=HTTP_200_OK)
