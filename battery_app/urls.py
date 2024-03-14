from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_file, result_page

urlpatterns = [
    
    path('', upload_file, name='upload_file'),
    path('result/', result_page, name='result_page'),
]
