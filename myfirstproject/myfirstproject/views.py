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
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    charcount = request.GET.get('charcount','off')
    punctuations = '''.,?!:;'"()[]{}...-–/—\&@%$#*+-=><|^_~'''

    if (removepunc == 'on' and fullcaps == 'on' and newlineremover == 'on'):
        analyzed = ''
        for char in text:
            if char not in punctuations and char != '/n':
                analyzed = analyzed + char.upper()

        params = {'purpose':'Remove Punctuation, Uppercase, NewLine Remover',
                'analyzed_text':analyzed}
        return render(request, 'analyze.html',params)
    
    elif removepunc == 'on':
        analyzed = ''
        print(text)
        print(len(text))
        for char in text:
            if char not in punctuations:
                print(char)
                analyzed = analyzed + char
        print(analyzed)
        params = {'purpose':'Remove Punctuation',
                'analyzed_text':analyzed}
        print(params['analyzed_text'])
        return render(request, 'analyze.html',params)
    
    elif fullcaps =='on':
        analyzed = ''
        for char in text:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to Uppercase','analyzed_text':analyzed}
        return render(request, 'analyze.html',params)
     
    elif newlineremover =='on':
        analyzed = ''
        for char in text:
           if char !="/n":
            analyzed = analyzed + char
        params = {'purpose':'Removed Newlines','analyzed_text':analyzed}
        return render(request, 'analyze.html',params)

    elif extraspaceremover =='on':
        analyzed = ''
        for index,char in enumerate(text):
           if not(text[index] ==" " and text[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Removed Extra space','analyzed_text':analyzed}
        return render(request, 'analyze.html',params)
    
    elif charcount =='on':
        count = 0
        for char in text:
            count += 1
        params = {'purpose':'Character counted','analyzed_text':count}
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