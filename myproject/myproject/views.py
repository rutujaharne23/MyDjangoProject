# I have created this file - Rutuja
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("hello Rutuja")
#     # return HttpResponse("<h1>Rutuja</h1>") We can add HTML code inside HttpResponse
#
# def about(request):
#     return HttpResponse("About Page")

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home")

def aboutus(request):
    return HttpResponse("<h1>About us</h1>")

def contactus(request):
    return HttpResponse("<h1>Contact us</h1>")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    # Check which checkbox is on
    if removepunc == "on":
        analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = { 'purpose': 'Removed Punctuation', 'analyzed_text': analyzed }
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Space Removed', 'analyzed_text': analyzed}
        # djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and spaceremover != "on"):
        return HttpResponse("Error! Please select any operation and try again.")

    return render(request, 'analyze.html', params)
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("new line remove")
#
# def spaceremove(request):
#     return HttpResponse("space remove")
#
# def charcount(request):
#     return HttpResponse("char count")