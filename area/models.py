import json

import django.contrib.auth.forms
from django.conf import settings
from django.db import models
import datetime
# Create your models here.


class Filial(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class GrrProject(models.Model):
    name = models.CharField(max_length=30)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProjType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Phase(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Lic(models.Model):
    gos_num = models.CharField(max_length=20)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.gos_num


class Plot(models.Model):
    name = models.CharField(max_length=100)
    grp = models.ForeignKey(GrrProject, on_delete=models.CASCADE)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    lic = models.ForeignKey(Lic, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Month(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class MesureUnit(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class WorkType(models.Model):
    name = models.CharField(max_length=255)
    measure_unit = models.ForeignKey(MesureUnit, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.measure_unit})"

    class Meta:
        ordering = ['name']


class MainForm(models.Model):
    filial = models.ForeignKey(Filial, on_delete=models.RESTRICT, verbose_name="Филиал")
    company = models.ForeignKey(Company, on_delete=models.RESTRICT, verbose_name="Компания")
    grp = models.ForeignKey(GrrProject, on_delete=models.RESTRICT, verbose_name="ГР проект")
    proj_type = models.ForeignKey(ProjType, on_delete=models.RESTRICT, verbose_name="Тип проекта")
    plot = models.ForeignKey(Plot, on_delete=models.RESTRICT, verbose_name="Участок работ")
    phase = models.ForeignKey(Phase, on_delete=models.RESTRICT, verbose_name="Фаза работ на участке")
    lic = models.ForeignKey(Lic, on_delete=models.RESTRICT, null=True, blank=True, verbose_name="Лицензия")
    month = models.ForeignKey(Month, on_delete=models.RESTRICT, verbose_name="Месяц")
    work_type = models.ForeignKey(WorkType, on_delete=models.RESTRICT, verbose_name="Вид работ")
    measure_unit = models.ForeignKey(MesureUnit, on_delete=models.RESTRICT, verbose_name="Единица измерения")
    fact = models.BooleanField(verbose_name="Является ли параметр фактическим")
    value = models.FloatField(verbose_name="Значение")
    time_create = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, blank=True, null=True)
    # user_update = models.


class CompanyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Company):
            return o.__dict__
        return json.JSONEncoder.default(self, o)
