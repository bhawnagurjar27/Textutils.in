# I have created this file

from django.http import HttpResponse
from django.shortcuts import render        # For templates

#Templates

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')      #method in django to get the text      #replace GET with POST
    #djtext = request.GET.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    #print(djtext)
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
    #analyzed = djtext
        params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    # Analyze the text
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': "Change to Uppercase", 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char


        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        #return render(request, 'analyze.html', params)
    if(removepunc != "on" and fullcaps != "on" and extraspaceremover != "on" and newlineremover != "on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)



