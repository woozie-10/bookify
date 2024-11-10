from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile", views.my_profile, name="my_profile"),
    path("upload", views.book_upload, name="book_upload"),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/search/', views.book_search, name='book_search'),
    path('books/delete/<int:book_id>', views.book_delete, name='book_delete')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

