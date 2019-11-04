from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import BookARI
from . import ari

def index(request):
    status = request.GET.get('status', 0)
    status = int(status)
    context = {
        'book_aris': BookARI.objects.order_by('ari'),
        'status': status
    }
    return render(request, 'ariapp/index.html', context)


def delete_book(request, book_id):
    book = BookARI.objects.get(id=book_id)
    book.delete()
    return HttpResponseRedirect(reverse('ariapp:index'))


def calculate_ari(request):
    # print(request.POST)
    status = 0
    try:
        url = request.POST['url']
        url = url.strip()
        if BookARI.objects.filter(url=url).count() == 0:
        
            ad = ari.ari_from_url(url)
            
            book_ari = BookARI(title=ad['title'],
                                author=ad['author'],
                                url=ad['url'],
                                n_characters=ad['n_characters'],
                                n_words=ad['n_words'],
                                n_sentences=ad['n_sentences'],
                                ari=ad['ari'],
                                age_range=ad['age_range'],
                                grade_level=ad['grade_level'])
            book_ari.save()
        else:
            status = 1
    except:
        status = 2

    
    return HttpResponseRedirect(reverse('ariapp:index')+'?status=' + str(status))