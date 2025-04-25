from django.shortcuts import render, get_object_or_404

from health.models import Program, Category


# Create your views here.
def index(request):
    return render(request,'base.html')
def program_list(request,category_slug=None):
    category = None
    programs = Program.objects.filter(available=True)
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        programs = programs.filter(category=category)

    return render(request, 'program/programs/programs.html',{
        'category': category,
        'programs': programs,
        'categories': categories,
    })