from django.shortcuts import render
from django.http import HttpResponse



def writing(request):
    return render(request, 'writing/writing.html')





def PDF_Request(request):
    file = open('writing/CatsSongbook.pdf', "r+b")
    file.seek(0)
    pdf = file.read()
    file.close()
    return HttpResponse(pdf, 'static/writing/CatsSongbook.pdf')
