from urllib import request, response
from xmlrpc.client import ResponseError
from django.forms import model_to_dict
from django.shortcuts import render
from .models import Jurnal, Rabotnik, Facultet, Group, Napravlenie, Forma_kontrol9,Predmet, Studenti
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import viewsets,generics
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import action

from catalog import serializers
# Create your views here.

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_facultet=Facultet.objects.all().count
    num_napravlenie=Napravlenie.objects.all().count
    num_group=Group.objects.all().count
    
    num_rabotnik=Rabotnik.objects.all().count

    num_predmet=Predmet.objects.all().count
    num_forma_kontrol9=Forma_kontrol9.objects.all().count

    num_studenti=Studenti.objects.all().count

    num_jurnal=Jurnal.objects.all().count

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_facultet':num_facultet,'num_napravlenie':num_napravlenie,'num_group':num_group,
        'num_rabotnik':num_rabotnik,
        'num_predmet':num_predmet,'num_forma_kontrol9':num_forma_kontrol9,
        'num_studenti':num_studenti,
        'num_jurnal':num_jurnal},
    )

#Отображение списков
from django.views import generic
####################################################################################

class FacultetListView(generic.ListView):
    model = Facultet
    #paginate_by = 10
class FacultetDetailView(generic.DetailView):
    model = Facultet

class FacultetCreate(CreateView):
    model = Facultet
    fields = '__all__'
    #success_url = reverse_lazy('facultets')

class FacultetUpdate(UpdateView):
    model = Facultet
    fields = '__all__'
    success_url = reverse_lazy('facultets')

class FacultetDelete(DeleteView):
    model = Facultet
    success_url = reverse_lazy('facultets')



###API

class FacultetViewSet(viewsets.ModelViewSet):
    queryset=Facultet.objects.all()
    serializer_class=FacultetSerializer

#Подробно расписанный метод добавления удаления изменения просмотра
# class FacultetAPIList(generics.ListCreateAPIView):
#     queryset=Facultet.objects.all()
#     serializer_class=FacultetSerializer

# class FacultetAPIUpdate(generics.UpdateAPIView):
#     queryset=Facultet.objects.all()
#     serializer_class = FacultetSerializer

# class FacultetAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Facultet.objects.all()
#     serializer_class=FacultetSerializer


################################################################################

class NapravlenieListView(generic.ListView):
    model = Napravlenie
    #paginate_by = 10
class NapravlenieDetailView(generic.DetailView):
    model = Napravlenie

class NapravlenieCreate(CreateView):
    model = Napravlenie
    fields = '__all__'

class NapravlenieUpdate(UpdateView):
    model = Napravlenie
    fields = '__all__'
    success_url = reverse_lazy('napravlenies')

class NapravlenieDelete(DeleteView):
    model = Napravlenie
    success_url = reverse_lazy('napravlenies')
    
###API

class NapravlenieViewSet(viewsets.ModelViewSet):
    queryset=Napravlenie.objects.all()
    serializer_class=NapravlenieSerializer
################################################################################

class GroupListView(generic.ListView):
    model = Group
    paginate_by = 5
class GroupDetailView(generic.DetailView):
    model = Group

class GroupCreate(CreateView):
    model = Group
    fields = '__all__'

class GroupUpdate(UpdateView):
    model = Group
    fields = '__all__'
    success_url = reverse_lazy('groups')

class GroupDelete(DeleteView):
    model = Group
    success_url = reverse_lazy('groups')

###API

class GroupViewSet(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class=GroupSerializer
################################################################################
class PredmetListView(generic.ListView):
    model = Predmet
class PredmetDetailView(generic.DetailView):
    model = Predmet

class PredmetCreate(CreateView):
    model = Predmet
    fields = '__all__'

class PredmetUpdate(UpdateView):
    model = Predmet
    fields = '__all__'
    success_url = reverse_lazy('predmets')

class PredmetDelete(DeleteView):
    model = Predmet
    success_url = reverse_lazy('predmets')

###API
class PredmetViewSet(viewsets.ModelViewSet):
    queryset=Predmet.objects.all()
    serializer_class=PredmetSerializer
################################################################################
class Forma_kontrol9ListView(generic.ListView):
    model = Forma_kontrol9
class Forma_kontrol9DetailView(generic.DetailView):
    model = Forma_kontrol9

class Forma_kontrol9Create(CreateView):
    model = Forma_kontrol9
    fields = '__all__'

class Forma_kontrol9Update(UpdateView):
    model = Forma_kontrol9
    fields = '__all__'
    success_url = reverse_lazy('forma_kontrol9s')

class Forma_kontrol9Delete(DeleteView):
    model = Forma_kontrol9
    success_url = reverse_lazy('forma_kontrol9s')

###API

class Forma_kontrol9ViewSet(viewsets.ModelViewSet):
    queryset=Forma_kontrol9.objects.all()
    serializer_class=Forma_kontrol9Serializer
################################################################################
class JurnalListView(generic.ListView):
    model = Jurnal
    paginate_by = 10
class JurnalDetailView(generic.DetailView):
    model = Jurnal

class JurnalCreate(CreateView):
    model = Jurnal
    fields = '__all__'

class JurnalUpdate(UpdateView):
    model = Jurnal
    fields = '__all__'
    success_url = reverse_lazy('jurnals')

class JurnalDelete(DeleteView):
    model = Jurnal
    success_url = reverse_lazy('jurnals')

###API

class JurnalViewSet(viewsets.ModelViewSet):
    queryset=Jurnal.objects.all()
    serializer_class=JurnalSerializer
################################################################################


class FicsationListView(generic.ListView):
    model = Ficsation
    paginate_by = 10
class FicsationDetailView(generic.DetailView):
    model = Ficsation

class FicsationCreate(CreateView):
    model = Ficsation
    fields = '__all__'

class FicsationUpdate(UpdateView):
    model = Ficsation
    fields = '__all__'
    success_url = reverse_lazy('ficsations')

class FicsationDelete(DeleteView):
    model = Ficsation
    success_url = reverse_lazy('ficsations')

###API

class FicsationViewSet(viewsets.ModelViewSet):
    queryset=Ficsation.objects.all()
    serializer_class=FicsationSerializer
################################################################################

    
class RabotnikListView(generic.ListView):
    model = Rabotnik
    paginate_by = 10
class RabotnikDetailView(generic.DetailView):
    model = Rabotnik

class RabotnikCreate(CreateView):
    model = Rabotnik
    fields = '__all__'

class RabotnikUpdate(UpdateView):
    model = Rabotnik
    fields = '__all__'
    success_url = reverse_lazy('rabotniks')

class RabotnikDelete(DeleteView):
    model = Rabotnik
    success_url = reverse_lazy('rabotniks')


###API

class RabotnikViewSet(viewsets.ModelViewSet):
    queryset=Rabotnik.objects.all()
    serializer_class=RabotnikSerializer
################################################################################
class StudentiListView(generic.ListView):
    model = Studenti
    paginate_by = 10
class StudentiDetailView(generic.DetailView):
    model = Studenti

class StudentiCreate(CreateView):
    model = Studenti
    fields = '__all__'

class StudentiUpdate(UpdateView):
    model = Studenti
    fields = '__all__'
    success_url = reverse_lazy('studentis')

class StudentiDelete(DeleteView):
    model = Studenti
    success_url = reverse_lazy('studentis')


###API

class StudentiViewSet(viewsets.ModelViewSet):
    queryset=Studenti.objects.all()
    serializer_class=StudentiSerializer
################################################################################

# from django.contrib.auth.mixins import LoginRequiredMixin

# class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
#     """
#     Generic class-based view listing books on loan to current user.
#     """
#     model = Facultet
#     template_name ='catalog/facultet_list.html'
#     paginate_by = 10
