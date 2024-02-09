# I have created this file - Niraj
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    mydict = {'name': 'niraj', 
              'school': 'suryodaya', 
              'address': 'damak-9'}
    return render(request, 'index.html',mydict)

def analyze(request):
    text = request.POST.get('text')
    removepunc = request.POST.get('removepunctuation','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    punctuations = '''.,?!:;'"()[]{}...-–/—\&@%$#*+-=><|^_~'''
    purpose = ''
    if removepunc == 'on':
        analyzed = ''
        print(text)
        print(len(text))
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        text = analyzed
        purpose += 'Remove punctuations'

    if fullcaps =='on':
        analyzed = ''
        for char in text:
            analyzed = analyzed + char.upper()
        text = analyzed
        purpose +='| Changed to Uppercase'

    if newlineremover =='on':
        analyzed = ''
        for char in text:
           if char !="\n" and char != '\r':
                analyzed = analyzed + char
           else:
               char = ' ' 
               analyzed = analyzed + char
        text = analyzed
        purpose +='| New Line Removed'

    if extraspaceremover =='on':
        analyzed = ''
        for index,char in enumerate(text):
           if not(text[index] ==" " and text[index+1] == " "):
                analyzed = analyzed + char
        text = analyzed
        purpose += "| Removed Extra Space"
    
    if charcount =='on':
        count = 0
        for char in text:
            count += 1
        params = {'purpose':'Character counted','analyzed_text':count}
        text = analyzed
        purpose +='| Character counted'

    if charcount =='off' and extraspaceremover == 'off' and removepunc=='off' and fullcaps == 'off' and newlineremover == 'off':
        return HttpResponse('ERROR')
    
    params = {'purpose':purpose, 'analyzed_text':analyzed}
    return render(request, 'analyze.html',params)

def removepunc(request):
    return HttpResponse('remove punc')
