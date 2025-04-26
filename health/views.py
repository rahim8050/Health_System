from django.shortcuts import render, get_object_or_404
from .models import Category, Program

def program_list(request,category_slug=None):
    category = None
    programs = Program.objects.filter(available=True)
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        programs = programs.filter(category=category)

    return render(request, 'program/programs/programs.html',{
        'category': category,
        'products': programs,
        'categories': categories,
    })


# views.py
from django.shortcuts import get_object_or_404


def program_list_by_category(request, category_slug):
    categories = Category.objects.all()
    current_category = None
    programs = Program.objects.filter(available=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        programs = programs.filter(category=current_category)

    return render(request, 'program/programs/programs.html', {
        'categories': categories,
        'programs': programs,
        'current_category': current_category
    })

def program_detail(request, id, slug):
    program = Program.objects.get(id=id, slug=slug)
    return render(request, 'program/programs/program_detail.html', {
        'program': program
    })

def index(request):
    return render(request,'base.html')