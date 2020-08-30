# I have created this file -junaid

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')



def about(request):
    return HttpResponse("This is about section")


def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')

    if removepunc == "on":
        # analyzed= djtext
        punctuations ='''['(-[\]{}()*+?.,\\^$|#\/]/g,"\\$&");'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
    
        params = {'purpose':'Remove punctuation','analyzed_text': analyzed }
        return render (request,'analyze.html',params)
    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

            params = {'purpose':'Capitalized text','analyzed_text': analyzed }
        return render (request,'analyze.html',params)
    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" :
                analyzed = analyzed + char

            params = {'purpose':'New Line Removed','analyzed_text': analyzed }
        return render (request,'analyze.html',params)

    else:
        return HttpResponse('<h1>Error 404 Not Found </h1> <a href="/">Home</a>' )