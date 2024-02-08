# I have created this file - Niraj
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse('hello Niraj')
# def about(request):
#     return HttpResponse('About me')

def index(request):
    mydict = {'name': 'niraj', 
              'school': 'suryodaya', 
              'address': 'damak-9'}
    return render(request, 'index.html',mydict)
def analyze(request):
    text = request.GET.get('text')
    removepunc = request.GET.get('removepunctuation','off')
    if removepunc == 'on':
        punctuations = '''.,?!:;'"()[]{}...-–/—\&@%$#*+-=><|^_~'''
        print(text,removepunc)
        analyzed = ''
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Remove Punctuation',
                'analyzed_text':analyzed}
        return render(request, 'analyze.html',params)
    else:
        return HttpResponse("Error: Invalid")

def removepunc(request):
    return HttpResponse('remove punc')

# def capfirst(request):
#     return HttpResponse('Captilize first')

# def newlineremove(request):
#     return  HttpResponse('Newline remove')

# def spaceremove(request):
#     return  HttpResponse('space remove')

# def charcount(request):
#     return  HttpResponse('char count')