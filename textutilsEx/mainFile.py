from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def analyze(request):
    user_text = request.POST.get('text', 'default')
    rem_punc = request.POST.get('removepunc', 'off')
    ch_case = request.POST.get('change_case', '')
    new_line = request.POST.get('removenewline', 'off')
    space_rem = request.POST.get('extraspaceremove', 'off')
    analyzed = ""
    purposes = ''
    if rem_punc == 'on':
        punctuations = '''!"'#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
        purposes += "Punctuations Removed, "
        for character in user_text:
            if character not in punctuations:
                analyzed = analyzed + character
        analyzed = analyzed.capitalize()
    else:
        analyzed = user_text

    if space_rem == 'on':
        temp = ''
        purposes += "Extra Spaces Removed, "
        for ind, t in enumerate(analyzed):
            try:
                if not (analyzed[ind] == " " and analyzed[ind+1] == " "):
                    temp = temp+t
            except:
                pass
        analyzed = temp

    if new_line == 'on':
        purposes += "New Lines Removed, "
        def func(value):
            return ' '.join(value.splitlines())
        analyzed = func(analyzed)

    if ch_case == 'Upper':
        purposes += "Changed Case, "
        analyzed = analyzed.upper()
    elif ch_case == 'Lower':
        purposes += "Changed Case, "
        analyzed = analyzed.lower()

    count_words = 0
    for i in range(len(analyzed)):
        try:
            if analyzed[i] == " " and analyzed[i+1] != " ":
                count_words += 1
        except:
            pass

    count_words += 1
    dict1 = {'purpose': purposes, 'analyzed_text': analyzed,
             "no_of_words": count_words}
    return render(request, 'analyze.html', dict1)
