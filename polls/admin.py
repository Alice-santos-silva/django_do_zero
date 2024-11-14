from django.contrib import admin

# Register your models here.

from polls.models import Question

@admin.register(Question)
class Question(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'nome', 'descricao', 'telefone', 'email', 'pub_date') # lista de quais campos eu quero que apareça
    search_fields = ('descricao', 'tipo',)
    list_filter = ('pub_date',)
    