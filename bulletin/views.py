from django.shortcuts import render, redirect
# Create your views here.

from .models import Board
from .forms import BaseBulletinBoard

def boardView(request):
    template_name = 'bulletin/bulletin.html'
    board_object = Board.objects.all()
    context = {
        'boardobject':board_object
    }
    return render(request, template_name, context)

def formView(request):
    template_name = 'bulletin/write_page.html' #?

    if request.method == 'POST':
        form = BaseBulletinBoard(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/board/')
    else:
        form = BaseBulletinBoard()
        context = {
            'form':form,
        }
        return render(request, template_name, context)
