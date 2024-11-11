from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import BookForm, ReviewForm
from .models import Book



def index(request):
    return render(request, "bookify/index.html")

@login_required
def my_profile(request):
    user_books = Book.objects.filter(uploader=request.user)
    username = request.user.username
    return render(request, "bookify/my_profile.html", {
        'user_books': user_books,
        'username': username,
    })

@login_required
def book_upload(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.uploader = request.user
            messages.success(request, "The book uploaded successfully!")
            book.save()
            return redirect('book_detail', book_id=book.id)
        else:
            messages.error(request, "Upload failed. Please correct the errors below.")
    else:
        form = BookForm()
    return render(request, 'bookify/book_upload.html', {'form': form})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.creator = request.user
                review.book = book
                review.save()
                messages.success(request, "The review was added successfully!")
                return redirect('book_detail', book_id=book_id)
            else:
                messages.error(request, "Review failed. Please correct the errors below.")
        else:
            messages.error(request, "You need to be logged in to add a review.")
            return redirect('user_login')
    else:
        form = ReviewForm()
    
    return render(request, "bookify/book_detail.html", {'book': book, 'form': form})
            
    

def book_search(request):
    query = request.GET.get('q', None)
    if query:
        books = Book.objects.filter(name__icontains=query) | Book.objects.filter(author__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'bookify/book_search.html', {'books': books})
 
@login_required    
def book_delete(request, book_id):
    if request.method == 'POST':
        Book.objects.filter(id=book_id).delete()
        messages.success(request, "The book has been deleted successfully!")
        return redirect('my_profile')
    return redirect('my_profile')
 
