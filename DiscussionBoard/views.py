from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Topic , Post
from django.http import  HttpResponse
from django.contrib.auth.models import User


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


def boards_topics(request, pk):
	board = get_object_or_404(Board, pk = pk)

	return render(request, 'topics.html', {'board':board})


