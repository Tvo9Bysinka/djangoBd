from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^facultets/$', views.FacultetListView.as_view(), name='facultets'),
    url(r'^facultet/(?P<pk>\d+)$', views.FacultetDetailView.as_view(), name='facultet-detail'),
    
    url(r'^napravlenies/$', views.NapravlenieListView.as_view(), name='napravlenies'),
    url(r'^napravlenie/(?P<pk>\d+)$', views.NapravlenieDetailView.as_view(), name='napravlenie-detail'),

    url(r'^groups/$', views.GroupListView.as_view(), name='groups'),
    url(r'^group/(?P<pk>\d+)$', views.GroupDetailView.as_view(), name='group-detail'),

    url(r'^predmets/$', views.PredmetListView.as_view(), name='predmets'),
    url(r'^predmet/(?P<pk>\d+)$', views.PredmetDetailView.as_view(), name='predmet-detail'),

    url(r'^forma_kontrol9s/$', views.Forma_kontrol9ListView.as_view(), name='forma_kontrol9s'),
    url(r'^forma_kontrol9/(?P<pk>\d+)$', views.Forma_kontrol9DetailView.as_view(), name='forma_kontrol9-detail'),

    url(r'^jurnals/$', views.JurnalListView.as_view(), name='jurnals'),
    url(r'^jurnal/(?P<pk>\d+)$', views.JurnalDetailView.as_view(), name='jurnal-detail'),

    url(r'^ficsations/$', views.FicsationListView.as_view(), name='ficsations'),
    url(r'^ficsation/(?P<pk>\d+)$', views.FicsationDetailView.as_view(), name='ficsation-detail'),

    url(r'^rabotniks/$', views.RabotnikListView.as_view(), name='rabotniks'),
    url(r'^rabotnik/(?P<pk>\d+)$', views.RabotnikDetailView.as_view(), name='rabotnik-detail'),

    url(r'^studentis/$', views.StudentiListView.as_view(), name='studentis'),
    url(r'^studenti/(?P<pk>\d+)$', views.StudentiDetailView.as_view(), name='studenti-detail'),
]


urlpatterns += [
    url(r'^facultet/create/$', views.FacultetCreate.as_view(), name='facultet_create'),
    url(r'^facultet/(?P<pk>\d+)/update/$', views.FacultetUpdate.as_view(), name='facultet_update'),
    url(r'^facultet/(?P<pk>\d+)/delete/$', views.FacultetDelete.as_view(), name='facultet_delete'),

    url(r'^napravlenie/create/$', views.NapravlenieCreate.as_view(), name='napravlenie_create'),
    url(r'^napravlenie/(?P<pk>\d+)/update/$', views.NapravlenieUpdate.as_view(), name='napravlenie_update'),
    url(r'^napravlenie/(?P<pk>\d+)/delete/$', views.NapravlenieDelete.as_view(), name='napravlenie_delete'),

    url(r'^group/create/$', views.GroupCreate.as_view(), name='group_create'),
    url(r'^group/(?P<pk>\d+)/update/$', views.GroupUpdate.as_view(), name='group_update'),
    url(r'^group/(?P<pk>\d+)/delete/$', views.GroupDelete.as_view(), name='group_delete'),

    url(r'^predmet/create/$', views.PredmetCreate.as_view(), name='predmet_create'),
    url(r'^predmet/(?P<pk>\d+)/update/$', views.PredmetUpdate.as_view(), name='predmet_update'),
    url(r'^predmet/(?P<pk>\d+)/delete/$', views.PredmetDelete.as_view(), name='predmet_delete'),

    url(r'^forma_kontrol9/create/$', views.Forma_kontrol9Create.as_view(), name='forma_kontrol9_create'),
    url(r'^forma_kontrol9/(?P<pk>\d+)/update/$', views.Forma_kontrol9Update.as_view(), name='forma_kontrol9_update'),
    url(r'^forma_kontrol9/(?P<pk>\d+)/delete/$', views.Forma_kontrol9Delete.as_view(), name='forma_kontrol9_delete'),

    url(r'^jurnal/create/$', views.JurnalCreate.as_view(), name='jurnal_create'),
    url(r'^jurnal/(?P<pk>\d+)/update/$', views.JurnalUpdate.as_view(), name='jurnal_update'),
    url(r'^jurnal/(?P<pk>\d+)/delete/$', views.JurnalDelete.as_view(), name='jurnal_delete'),

    url(r'^ficsation/create/$', views.FicsationCreate.as_view(), name='ficsation_create'),
    url(r'^ficsation/(?P<pk>\d+)/update/$', views.FicsationUpdate.as_view(), name='ficsation_update'),
    url(r'^ficsation/(?P<pk>\d+)/delete/$', views.FicsationDelete.as_view(), name='ficsation_delete'),


    url(r'^rabotnik/create/$', views.RabotnikCreate.as_view(), name='rabotnik_create'),
    url(r'^rabotnik/(?P<pk>\d+)/update/$', views.RabotnikUpdate.as_view(), name='rabotnik_update'),
    url(r'^rabotnik/(?P<pk>\d+)/delete/$', views.RabotnikDelete.as_view(), name='rabotnik_delete'),

    url(r'^studenti/create/$', views.StudentiCreate.as_view(), name='studenti_create'),
    url(r'^studenti/(?P<pk>\d+)/update/$', views.StudentiUpdate.as_view(), name='studenti_update'),
    url(r'^studenti/(?P<pk>\d+)/delete/$', views.StudentiDelete.as_view(), name='studenti_delete'),
]
