from django.shortcuts import render
from .models import Board
from django.http import  HttpResponse

# Create your views here.

def HomePageView(request):
    boards = Board.objects.all()
    #board_names = list()

    """for board in boards:
        board_names.append((board.name))
        http_response = '<br>'.join(board_names)
"""
       # return HttpResponse(http_response)
    return render(request, 'home.html', {'boards': boards})




