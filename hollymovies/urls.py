"""
URL configuration for hollymovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from viewer import urls as viewer_urls
from books import urls as books_urls
from accounts import urls as accounts_urls

from viewer.views import home

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    # Includem toate linkurile care incep cu /movies din fisierul
    # aflat in viewer/urls.py
    path('movies/', include(viewer_urls)),
    path('books/', include(books_urls)),

    # Includem link-urile pentru conturi/user views
    path('accounts/', include(accounts_urls, namespace='accounts'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ^ adaugam link-uri pentru fisierele statice
