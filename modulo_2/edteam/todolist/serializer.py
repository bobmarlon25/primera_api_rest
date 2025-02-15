from rest_framework import serializers

from .models import Tarea


class TareaSerializer(serializers.ModelSerializer): # el ModelSerializer nos ayuda a cear la clase con el mismo modelo 
    class Meta:    
        model=Tarea     # escojemos cual es el modelo 
        fields='__all__'    # y escohgemos los campos  ,en este caso todos 

     # se utiliza para moldear o maquillar un modulo podemos enviar informacion  y pedir informacon sin modificar el modulo 
    def to_representation(self, instance):
        representation= super().to_representation(instance)
        if instance.estado == 1:
            estado="pendiente"
        elif instance.estado== "2":
            estado ="terminado"
        return representation


