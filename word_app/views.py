from django.shortcuts import render, redirect 
from django.utils.crypto import get_random_string

def random(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    else:
        request.session['count'] += 1
    request.session['rand_word'] = get_random_string(length=14)
    return render(request, 'random.html')

def submit(request):
    return render(request, 'random.html')

def reset(request):
    request.session.flush()
    return redirect('/')
