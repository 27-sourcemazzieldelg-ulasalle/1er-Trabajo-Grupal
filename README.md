# 1er-Trabajo-Grupal
es para que subamos la tarea dejada en clases
https://colab.research.google.com/drive/1qLbKcyy9puymKd8wZkrkDyiPLlnFbfVP?usp=sharing#scrollTo=ZUHRaBcyOwB_
cola
# Creo una cola llamada proyecto que contiene los pasos del mismo
proyecto = Cola()
# Agregar las tareas a la cola paraa la completacion de mi proyecto
proyecto.encolar("Planificación")
proyecto.encolar("Diseño")
proyecto.encolar("Desarrollo")
proyecto.encolar("Pruebas")
proyecto.encolar("Entrega")
print("Estado inicial de la cola:")
while not proyecto.esta_vacia():
    print(proyecto.desencolar())

# Agregar una nueva tarea y mostrarla
proyecto.encolar("Mantenimiento")
print("Nueva tarea agregada:", proyecto.ver_primero())
1 ejemplos de fila
tareas = ["Comprar pan", "Desayunar","Lavar los platos", "Estudiar Python"]

# Elimine la primera tarea(no olvidar que empezamos desde 0- se uso el metodo pop)
tareas.pop(0)

# Use el append para agregar un elemento al final de la lista
tareas.append("Preparar el almuerzo")

# Imprimo todas las tareas menos la primera que borre y se va a imprimir la tarea agregada.
print(tareas)
2 ejemplos de fila
tareas = ["Comprar pan", "Desayunar","Lavar los platos", "Estudiar Python"]

# Elimine la primera tarea(no olvidar que empezamos desde 0- se uso el metodo pop)
tareas.pop(0)

# Use el append para agregar un elemento al final de la lista
tareas.append("Preparar el almuerzo")

# Imprimo todas las tareas menos la primera que borre y se va a imprimir la tarea agregada.
print(tareas)
