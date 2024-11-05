# habilitar a rota do signupform para caregar a view de accounts e renderizar o template signup_form
from django.urls import path
from accounts.views import AccountCreateView  

urlpatterns = [
    path(
        'accounts/signup', # esse nome pode mudar no futuro, se eu quiser 
        AccountCreateView.as_view(),
        name="signup" # nome interno que não muda
    ),
]
