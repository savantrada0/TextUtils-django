# from django.http import HttpResponse
# def index(request):
#     return HttpResponse('''<h1> Harry</h1><a href="https://www.codewithharry.com/videos/python-tutorials-for-absolute-beginners-124/">cwh</a>''')
#
# def about(request):
#     return HttpResponse("hello about")

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
 #   return HttpResponse("Home")

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')

    if removepunc == "on":
        puctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in puctuations:
                analyzed= analyzed+char
        params = {'purpose':'Removed Punctuations','analyzed_text': analyzed}
        djtext = analyzed
     #   return render(request,'analyze.html',params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'purpose':'charged to uppercase','analyzed_text':analyzed}
        djtext =analyzed
      #  return render(request,'analyze.html',params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Removed ExtraSpaces','analyzed_text':analyzed}
        djtext = analyzed
      #  return render(request,'analyze.html',params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose':'Removed NewLines',"analyzed_text":analyzed}
        djtext = analyzed
     #   return render(request,'analyze.html',params)

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request,'analyze.html',params)

# def ex1(request):
#     sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
#              '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
#              '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
#              '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
#              ]
#     return HttpResponse((sites))
# def capfirst(request):
#     return HttpResponse("capitalzise first")
#
# def newlineremove(request):
#     return HttpResponse("capitalize first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover")
#
# def charcount(request):
#     return HttpResponse("charcount ")