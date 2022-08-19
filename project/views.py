import base64
import os
from django.shortcuts import render
from django.core.files.base import ContentFile
from .face_rec import FaceRec
from PIL import Image
import base64
import secrets
import io


# Create your views here.
def index(request):
    return render(request, "project/index.html", {})


def cam(request):
    if request.method == 'POST':
        # initialising face recognition object
        faceRec = FaceRec()

        # reading the dataurl and converting into an image
        data = str(request.POST.get('img'))
        _format, _dataurl = data.split(';base64,')
        _filename, _extension = secrets.token_hex(20), _format.split('/')[-1]
        file = ContentFile(base64.b64decode(_dataurl),
                           name=f"{_filename}.{_extension}")
        image = Image.open(file)
        image_io = io.BytesIO()
        image.save(image_io, format=_extension)

        # generating the content of the new image
        file = ContentFile(image_io.getvalue(),
                           name=f"{_filename}.{_extension}")
        # saving the file on system
        filename = faceRec.unknown_dir+"\\"+_filename+"."+_extension

        fout = open(filename, 'wb+')
        for chunk in file.chunks():
            fout.write(chunk)
            fout.close()

        # recognising the face in image
        print(faceRec.recongnizeImg(filename))

        # deleting file after processing
        os.remove(filename)
        return render(request, "project/webCam.html", {
            "success": False,
            "message": ""
        })

    return render(request, "project/webCam.html")
