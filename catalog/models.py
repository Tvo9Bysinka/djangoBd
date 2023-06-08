from django.db import models
from django.urls import reverse #Используется для создания URL-адресов путем изменения шаблонов URL-адресов.
import uuid # Требуется для уникальных экземпляров 

class Facultet(models.Model):
    """Модель, представляющая Факультет."""
    #id = models.IntegerField(primary_key=True,db_index=True, help_text="Уникальный индификатор")
    id = models.AutoField(primary_key=True)
    name_faculteta = models.CharField(max_length=100, help_text="Введите абривиатуру (название) факультета ")
    def get_absolute_url(self):
        """Возвращает URL-адрес для доступа к конкретному ."""
        return reverse('facultet-detail', args=[str(self.id)])    
    def __str__(self):
# чтобы вернуть удобочитаемую строку для каждого объекта. 
# Эта строка используется для представления отдельных записей на сайте администрирования 
# (и в любом другом месте, где вам нужно обратиться к экземпляру модели). 
# Часто это возвращает поле названия или имени из модели.
        return '%s ' % (self.name_faculteta)
    class Meta:
        ordering = ['name_faculteta']


class Napravlenie(models.Model):
    """Модель, представляющая Направление."""
    id = models.AutoField(primary_key=True)
    name_napravlenie = models.CharField(max_length=100, help_text="Введите номер (название) направления ")
    id_facultet = models.ForeignKey('Facultet', on_delete=models.PROTECT, null=False) #PROTECT (Нельзя будет удалить запись указанной таблицы пока он привязан к какой-то таблице)
    def get_absolute_url(self):
        """Возвращает URL-адрес для доступа к конкретному ."""
        return reverse('napravlenie-detail', args=[str(self.id)])    
    def __str__(self):
        return '%s %s' % (self.name_napravlenie,self.id_facultet.name_faculteta)
    class Meta:
        ordering = ['name_napravlenie']


class Group(models.Model):
    """Модель, представляющая Группу."""
    id = models.AutoField(primary_key=True)
    name_group = models.CharField(max_length=50, help_text="Введите номер (название) группы ")
    id_napravlenie = models.ForeignKey('Napravlenie', on_delete=models.PROTECT, null=False)
    def get_absolute_url(self):
        """Возвращает URL-адрес для доступа к конкретному ."""
        return reverse('group-detail', args=[str(self.id)])    
    def __str__(self):
        return '%s (%s)' % (self.name_group,self.id_napravlenie)
    class Meta:
        ordering = ['name_group','-id_napravlenie']

class Studenti(models.Model):
    """Модель, представляющая Студентов. """
    id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100,null=True)
    first_name = models.CharField(max_length=100,null=True)
    middle_name = models.CharField(max_length=100,null=True)
    id_groupa = models.ForeignKey('Group', on_delete=models.PROTECT, null=False)

    def get_absolute_url(self):
        """Возвращает URL-адрес для доступа к конкретному ."""
        return reverse('studenti-detail', args=[str(self.id)])    
    def __str__(self):
        return '%s %s %s [%s]' % (self.last_name,self.first_name,self.middle_name, 
        self.id_groupa)

    class Meta:
        ordering = ['last_name']

###############################################################################################


class Rabotnik(models.Model):
    """Модель, представляющая Работника. """
    id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100,null=True)
    first_name = models.CharField(max_length=100,null=True)
    middle_name=models.CharField(max_length=100,null=True)
    
    def get_absolute_url(self):
        """Возвращает URL-адрес для доступа к конкретному ."""
        return reverse('rabotnik-detail', args=[str(self.id)])    
    def __str__(self):
        return '%s %s %s' % (self.last_name,self.first_name,self.middle_name)
    class Meta:
        ordering = ['last_name']



###############################################################################################
class Forma_kontrol9(models.Model):
    """Модель, представляющая Форму контроля."""
    id = models.AutoField(primary_key=True)
    vid_formi = models.CharField(max_length=50, help_text="Введите вид занятия (Например лекция, практическое занятие, лабараторное) ")
    def get_absolute_url(self):
        """Возвращает URL-адрес для доступа к конкретному ."""
        return reverse('forma_kontrol9-detail', args=[str(self.id)])    
    def __str__(self):
        return '%s ' % (self.vid_formi)

class Predmet(models.Model):
    """Модель, представляющая Предмет. """
    id = models.AutoField(primary_key=True)
    name_predmeta = models.CharField(max_length=70,help_text="Введите название предмета")
    id_forma_kontrol9 = models.ForeignKey('Forma_kontrol9', on_delete=models.PROTECT, null=False) #PROTECT (Вид занятия нельзя будет удалить пока он привязан к какой-то таблице)
    
    def get_absolute_url(self):
        """Возвращает URL-адрес для доступа к конкретному ."""
        return reverse('predmet-detail', args=[str(self.id)])    
    def __str__(self):
        return '%s (%s)' % (self.name_predmeta,self.id_forma_kontrol9.vid_formi)



###############################################################################################
###############################################################################################


class Jurnal(models.Model):
    """Модель, представляющая Предмет. """
    id = models.AutoField(primary_key=True)
    id_rabotnika = models.ForeignKey('Rabotnik', on_delete=models.PROTECT, null=False) #PROTECT (Вид занятия нельзя будет удалить пока он привязан к какой-то таблице)
    id_predmeta = models.ForeignKey('Predmet', on_delete=models.PROTECT, null=False)
    id_studentov = models.ForeignKey('Studenti', on_delete=models.CASCADE, null=False)


    def get_absolute_url(self):
        """Возвращает URL-адрес для доступа к конкретному ."""
        return reverse('jurnal-detail', args=[str(self.id)])    
    def __str__(self):
        return '[%s] %s %s %s  ' % (self.id,
        self.id_rabotnika,self.id_predmeta,self.id_studentov)
    class Meta:
        ordering = ['id_predmeta','id_rabotnika','id_studentov']
        
    
###############################################################################################
class Ficsation(models.Model):
    """Модель, представляющая Фиксацию. """
    id = models.AutoField(primary_key=True)
    id_nomer_zapisi = models.ForeignKey('Jurnal', on_delete=models.CASCADE, null=False) 
    data_propyskov = models.DateField(null=True, blank=True)
    propyski = models.BooleanField (default=True,help_text="Присутсвовал/Отсутсвовал")
    opisanie = models.TextField(max_length=1000,null=True,blank=True, help_text="Описание")


    def get_absolute_url(self):
        """Возвращает URL-адрес для доступа к конкретному ."""
        return reverse('ficsation-detail', args=[str(self.id)])    
    def __str__(self):
        return '[%s] %s %s %s %s   ' % (self.id,self.id_nomer_zapisi,
        self.data_propyskov,self.propyski,self.opisanie)

    class Meta:
        ordering = ['-data_propyskov']