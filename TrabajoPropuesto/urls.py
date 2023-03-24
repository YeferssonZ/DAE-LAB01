from django.urls import path

from . import views



urlpatterns = [
    # ex: localhost:8080/app/
    path('', views.index, name='index'),
    # ex: localhost:8080/app/sumar/18/19
    path('sumar/<int:num1>/<int:num2>', views.suma),
    # ex: localhost:8080/app/restar/18/19
    path('restar/<int:num1>/<int:num2>', views.resta),
    # ex: localhost:8080/app/multiplicar/18/19
    path('multiplicar/<int:num1>/<int:num2>', views.multiplicacion),
    # ex: localhost:8080/app/dividir/18/19
    path('dividir/<int:num1>/<int:num2>', views.division)
    ]