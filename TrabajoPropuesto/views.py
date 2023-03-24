from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("BIENVENIDO")

def suma(request,num1,num2):
    var1 = int(num1)
    var2 = int(num2)
    # result = "La suma 18 + 19 es: %s" % (var1+var2)
    result = "La suma del número es: %s" % (var1+var2)
    return HttpResponse(result)

def resta(request,num1,num2):
    var1 = int(num1)
    var2 = int(num2)
    # result = "La resta 18 - 19 es: %s" % (var1-var2)
    result = "La resta del número es: %s" % (var1-var2)
    return HttpResponse(result)

def multiplicacion(request,num1,num2):
    var1 = int(num1)
    var2 = int(num2)
    # result = "La multliplicación 18 * 19 es: %s" % (var1*var2)
    result = "La multliplicación del número es: %s" % (var1*var2)
    return HttpResponse(result)

def division(request,num1,num2):
    var1 = int(num1)
    var2 = int(num2)
    # result = "La división 18 / 19 es: %s" % (var1/var2)
    result = "La división del número es: %s" % (var1/var2)
    return HttpResponse(result)