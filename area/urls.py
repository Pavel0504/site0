from django.urls import path
from . import views


app_name = 'area'

urlpatterns = [
    path('', views.index, name='index'),
    path('/add', views.add, name='add'),
    path('/<int:id>/edit', views.edit, name='edit'),
    path('/<int:id>/delete', views.delete, name='delete'),
    path('/<int:id>/filial_data', views.filial_data, name='filial_data'),
    path('/<int:id>/grp_data', views.grp_data, name='grp_data'),
    path('/<int:id>/plot_data', views.plot_data, name='plot_data'),
    # path('/<int:id>/plot_data', views.plot_data, name='plot_data'),
]
