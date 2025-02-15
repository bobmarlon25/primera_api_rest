from django.urls import path

from . import views

urlpatterns = [
    path('',views.Index.as_view() ),
    path('tarea',views.TareaView.as_view()),
    path('tarea/<int:pk>',views.TareaDetailView.as_view())
]

