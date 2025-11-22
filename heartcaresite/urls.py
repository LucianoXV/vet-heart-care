from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
    path('data_confirmation/', views.data_confirmation, name='data_confirmation'),
    path('name/', views.get_name, name='name'),
    path('view_save_doc/', views.view_save_doc, name='view_save_doc'),
    path('voltar/', views.voltar_action, name='voltar_action'),
    path('success/', views.success_page, name='success_page'),
]