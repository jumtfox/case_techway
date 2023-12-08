from django.urls import path
from page_app.views import index, contato, services
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Cadastrar URLs aqui
    path('', index),
    
    path('contato/', contato),

    path('services/', services),
 
]



