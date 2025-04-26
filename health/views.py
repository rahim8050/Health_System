from django.shortcuts import render, get_object_or_404
from .models import Category, Program


def program_list(request):
    categories = Category.objects.prefetch_related('programs')
    return render(request, 'program/programs/programs.html', {
        'categories': categories
    })

def program_detail(request, id, slug):
    program = get_object_or_404(Program, id=id, slug=slug)
    return render(request, 'program/programs/program_detail.html', {
        'program': program
    })
def index(request):
    return render(request,'base.html')