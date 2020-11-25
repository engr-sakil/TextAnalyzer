import string

from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request,'index.html')

def analyzedText(request):
    djtext = request.POST.get('text', 'default')
    selecttype = request.POST.get('selecttype', 'off')
    if selecttype == 'punc':
        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuation', 'analyzedText': analyzed}

        return render(request,'analyzedresult.html',params)
    elif selecttype == 'space':
        analyzed = ''
        for char in djtext:
            if char != ' ':
                analyzed = analyzed + char

        params = {'purpose': 'Removed Space', 'analyzedText': analyzed}

        return render(request, 'analyzedresult.html', params)
    elif selecttype == 'newline':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char

        params = {'purpose': 'Removed Newline', 'analyzedText': analyzed}

        return render(request, 'analyzedresult.html', params)
    elif selecttype == 'count':
        analyzed = len(djtext)
        params = {'purpose': 'Charecter Count', 'analyzedText': analyzed}

        return render(request, 'analyzedresult.html', params)
    elif selecttype == 'extra':
        analyzed = string.capwords(djtext)
        params = {'purpose': 'Capitalize the first letter', 'analyzedText': analyzed}

        return render(request, 'analyzedresult.html', params)

    elif selecttype == 'capital':
        analyzed = djtext.upper()
        params = {'purpose': 'Capitalize', 'analyzedText': analyzed}

        return render(request, 'analyzedresult.html', params)

    else:
        return render(request,'Error.html')


