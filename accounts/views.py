from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password # criptografia
from django.contrib import messages

from django.contrib.auth import get_user_model # o django decide qual é o modelo
User = get_user_model()

from accounts.forms import AccountSignupForm # classe que eu criei

# view baseada em classe

class AccountCreateView(CreateView):
    model = User
    template_name = 'registration/signup_form.html'
    form_class = AccountSignupForm
    success_url = reverse_lazy('login') # o nome login já é um nome de rota interno, do proprio django
    success_message = 'Usuário criado com sucesso!'
    
    # parte necessária por conta do campo de senha
    def form_valid(self, form):
        form.instance.password = make_password(form.instance.password)
        messages.success(self.request, self.success_message)
        
        return super(AccountCreateView, self).form_valid(form)
    
    