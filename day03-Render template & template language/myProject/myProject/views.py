from django.shortcuts import render

def homePage(request):
    myDictionary={
        'key': 'value',
        'name': 'Shamim',
        'roll': '101'
    }
    return render(request, 'homePage.html', myDictionary)