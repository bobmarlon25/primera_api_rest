from django.http import JsonResponse

import json

from .models import Curso

from django.views.decorators.csrf import  csrf_exempt
def index(request):
    context ={
        'status':True,
        'content' :'mi primer api rest con django '
    }
    return  JsonResponse(context)



def cursos(request):
    lista_de_cursos=Curso.objects.all()
    context ={
       'status':True,
        'content' :list(lista_de_cursos.values())
    }
    return  JsonResponse(context)

@csrf_exempt
def post_curso(request):
    json_data=json.loads(request.body)

    titulo=json_data['titulo']
    descripcion=json_data['descripcion']
    imagen=json_data['imagen']

    nuevo_curso=Curso.objects.create(
        titulo=titulo,
        descripcion=descripcion,
        imagen=imagen
    )
    dic_nuevo_curso={
        'id':nuevo_curso.id,
        'titulo':nuevo_curso.titulo,
        'descripcion':nuevo_curso.descripcion
    }
    context={
        'status':True,
        'content':dic_nuevo_curso

    }
    return JsonResponse(context)