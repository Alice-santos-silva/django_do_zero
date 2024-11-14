"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.utils.translation import gettext_lazy as _

# Personalização do Django Admin
admin.site.site_header = _("Gerenciamento Brazil Sensations")
admin.site.site_title = _("Título da Aba do Admin")
admin.site.index_title = _("Gerenciamento de fornecedores e clientes.")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
    path('', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
