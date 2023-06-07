from django.contrib import admin
from .models import *


# Register your models here.


class FilialAdmin(admin.ModelAdmin):
    pass

class CompanyAdmin(admin.ModelAdmin):
    pass

class GrrProjectAdmin(admin.ModelAdmin):
    pass

class ProjTypeAdmin(admin.ModelAdmin):
    pass

class PhaseAdmin(admin.ModelAdmin):
    pass

class LicAdmin(admin.ModelAdmin):
    pass

class PlotAdmin(admin.ModelAdmin):
    pass

class MonthAdmin(admin.ModelAdmin):
    pass

class MesureUnitAdmin(admin.ModelAdmin):
    pass

class WorkTypeAdmin(admin.ModelAdmin):
    pass

class MainFormAdmin(admin.ModelAdmin):
    pass

admin.site.register(Filial, FilialAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(GrrProject, GrrProjectAdmin)
admin.site.register(ProjType, ProjTypeAdmin)
admin.site.register(Phase, PhaseAdmin)
admin.site.register(Lic, LicAdmin)
admin.site.register(Plot, PlotAdmin)
admin.site.register(Month, MonthAdmin)
admin.site.register(MesureUnit, MesureUnitAdmin)
admin.site.register(WorkType, WorkTypeAdmin)
admin.site.register(MainForm, MainFormAdmin)
