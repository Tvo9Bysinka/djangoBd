"""DjangoBD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include, re_path

from catalog.views import *
from rest_framework import routers
urlpatterns = [
    path('admin/', admin.site.urls),
]

#Авторизация
urlpatterns += [
    path('api/v1/drf-auth/',include('rest_framework.urls')), #http://127.0.0.1:8000/api/v1/drf-auth/login/(logout)
    
]
#Токен
urlpatterns += [
    path('api/v1/auth/',include('djoser.urls')), 
    re_path(r'^auth/',include('djoser.urls.authtoken')),
]
# class MyCustomRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(url=r'^{prefix}$',
#                       mapping={'get': 'list'},
#                       name='{basename}-list',
#                       detail=False,
#                       initkwargs={'suffix': 'List'}),
#         routers.Route(url=r'^{prefix}/{lookup}$',
#                       mapping={'get': 'retrieve'},
#                       name='{basename}-detail',
#                       detail=True,
#                       initkwargs={'suffix': 'Detail'})
#     ]
# router = MyCustomRouter() - роутер где будет находить страницу без последнего слешла  http://127.0.0.1:8000/api/v1/facultet (работает как SimpleRouter)

router=routers.DefaultRouter() # - #http://127.0.0.1:8000/api/v1/ есть путь (показывает куда идти) router=routers.SimpleRouter() - нет пути

router.register(r'facultet',FacultetViewSet)
urlpatterns += [path('api/v1/',include(router.urls)),]
router.register(r'napravlenie',NapravlenieViewSet)
urlpatterns += [path('api/v1/',include(router.urls)), ]
router.register(r'group',GroupViewSet)
urlpatterns += [path('api/v1/',include(router.urls)),]
router.register(r'studenti',StudentiViewSet)
urlpatterns += [path('api/v1/',include(router.urls)), ]
router.register(r'jurnal',JurnalViewSet)
urlpatterns += [path('api/v1/',include(router.urls)), ]
router.register(r'ficsation',FicsationViewSet)
urlpatterns += [path('api/v1/',include(router.urls)), ]
router.register(r'rabotnik',RabotnikViewSet)
urlpatterns += [path('api/v1/',include(router.urls)), ]
router.register(r'forma_kontrol9',Forma_kontrol9ViewSet)
urlpatterns += [path('api/v1/',include(router.urls)), ]
router.register(r'predmet',PredmetViewSet)
urlpatterns += [path('api/v1/',include(router.urls)), ]




# Используйте include() чтобы добавлять URL из каталога приложения
from django.urls import include
urlpatterns += [
     path('catalog/', include('catalog.urls')),
]

# Добавьте URL соотношения, чтобы перенаправить запросы с корневого URL, на URL приложения
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

# Используйте static() чтобы добавить соотношения для статических файлов
# Только на период разработки
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
