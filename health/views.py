from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .models import Category, Program, Enrollment


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


@require_POST  # Ensures this view only accepts POST requests
def enroll_program(request, id, slug):
    program = get_object_or_404(Program, id=id, slug=slug)

    if not request.user.is_authenticated:
        messages.warning(request, "Please log in to enroll.")
        return redirect('login')

    try:
        # Create enrollment if it doesn't exist
        enrollment, created = Enrollment.objects.get_or_create(
            user=request.user,
            program=program
        )
        if created:
            messages.success(request, "Successfully enrolled in the program!")
        else:
            messages.info(request, "You're already enrolled in this program.")

    except Exception as e:
        messages.error(request, f"Error enrolling: {str(e)}")

    return redirect('health:detail', id=id, slug=slug)




@login_required
def profile(request):
    enrollments = Enrollment.objects.filter(
        user=request.user
    ).select_related(
        'program',
        'program__category'
    ).order_by('-enrolled_at')

    return render(request, 'users/accounts/profile.html', {
        'enrollments': enrollments
    })

