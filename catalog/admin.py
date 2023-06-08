from django.contrib import admin
from .models import Jurnal, Rabotnik, Facultet, Group, Napravlenie, Forma_kontrol9,Predmet, Studenti,Ficsation

#admin.site.register(Facultet)
#admin.site.register(Group)
#admin.site.register(Napravlenie)
#admin.site.register(Studenti)


class StudentiInline(admin.TabularInline):
    model = Studenti

class NapravlenieInline(admin.TabularInline):
    model = Napravlenie

class GroupInline(admin.TabularInline):
    model = Group

class PredmetInline(admin.TabularInline):
    model = Predmet

class RabotnikInline(admin.TabularInline):
    model = Rabotnik

@admin.register(Facultet)
class FacultetAdmin(admin.ModelAdmin):
    list_display = ('name_faculteta','id')
    fields = ['name_faculteta']
    inlines = [NapravlenieInline]

@admin.register(Napravlenie)
class NapravlenieAdmin(admin.ModelAdmin):
    list_display = ('name_napravlenie','id_facultet','id')#Что мы будем видеть
    fields = ['name_napravlenie','id_facultet'] #Что отображается при добавлении редактировании
    inlines = [GroupInline]

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name_group','id_napravlenie','id')
    fields = ['name_group','id_napravlenie']
    inlines = [StudentiInline] #Чтобы можно было добавлять/(изменять) прям в добавлении/редактировании модели




class StudentiAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name','middle_name','id','id_groupa') 
    fields = ['first_name', 'last_name','middle_name','id_groupa']
   
admin.site.register(Studenti, StudentiAdmin)
    





@admin.register(Forma_kontrol9)
class Forma_kontrol9Admin(admin.ModelAdmin):
    list_display = ('vid_formi','id')
    fields = ['vid_formi']
    inlines = [PredmetInline]

@admin.register(Predmet)
class PredmetAdmin(admin.ModelAdmin):
    list_display = ('name_predmeta','id','id_forma_kontrol9')
    fields = ['name_predmeta','id_forma_kontrol9']


@admin.register(Rabotnik)
class RabotnikpAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','middle_name','id')
    fields = ['last_name','first_name','middle_name'] 


# Register your models here.
@admin.register(Jurnal)
class JurnalAdmin(admin.ModelAdmin):
    list_filter = ('id_predmeta','id_rabotnika','id_studentov')
    list_display = ('id','id_predmeta','id_rabotnika', 'id_studentov')
    fields = ['id_predmeta','id_rabotnika', 'id_studentov'] 
   



@admin.register(Ficsation)
class FicsationAdmin(admin.ModelAdmin):
    list_filter = ('data_propyskov', 'propyski')
    list_display = ('id_nomer_zapisi','data_propyskov', 'propyski','opisanie','id')
    fields = ['id_nomer_zapisi','data_propyskov', 'propyski','opisanie'] 