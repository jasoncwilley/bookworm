from django.shortcuts import render

from .models import Bookcase

def bookcase_list(request):
    bookcases = Bookcase.objects.prefetch_related('bookshelf_set').all()

    context = {
        "bookcases": bookcases,
    }
    return render(request, "bookcases/bookcase_list.html", context)