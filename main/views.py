from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Post
from .forms import PostForm
import base64

def board_list(request):
    boards = Board.objects.all()
    return render(request, "main/board_list.html", {"boards": boards})

def board_detail(request, slug):
    board = get_object_or_404(Board, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.board = board
            post.ip_address = request.META.get("REMOTE_ADDR")
            image = form.cleaned_data.get("image")
            if image:
                post.image_data = image.read()
                post.image_mime = image.content_type
            post.save()
            return redirect("board_detail", slug=slug)
    else:
        form = PostForm()

    posts = board.posts.filter(parent__isnull=True).order_by("-created_at")
    return render(request, "main/board_detail.html", {
        "board": board,
        "posts": posts,
        "form": form,
    })
