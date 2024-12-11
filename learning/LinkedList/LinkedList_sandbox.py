# LinkedList_sandbox.py
from Node import Node

class LinkedList:
    def __init__(self, value=None):
        """Inicializa la lista enlazada con un nodo cabeza."""
        self.head_node = Node(value)

    def get_head_node(self):
        """Devuelve el nodo cabeza de la lista enlazada."""
        return self.head_node

    def insert_beginning(self, new_value):
        """Inserta un nuevo nodo al comienzo de la lista."""
        new_node = Node(new_value)  # Crea un nuevo nodo con el valor proporcionado
        new_node.set_next_node(self.head_node)  # Enlaza el nuevo nodo al nodo cabeza actual
        self.head_node = new_node  # Actualiza el nodo cabeza para que sea el nuevo nodo

    def stringify_list(self):
        """Devuelve una representación de cadena de todos los valores en la lista."""
        string_list = ""  # Variable para almacenar los valores de los nodos
        current_node = self.head_node  # Comienza desde el nodo cabeza

        while current_node is not None:  # Recorre hasta que no haya más nodos
            if current_node.get_value() is not None:  # Verifica que el valor no sea None
                string_list += str(current_node.get_value()) + "\n"  # Concatenar valor y salto de línea
            current_node = current_node.get_next_node()  # Avanza al siguiente nodo

        return string_list  # Devuelve la representación de cadena de la lista

    def remove_node(self, value_to_remove):
        """Elimina el primer nodo que contenga el valor especificado."""
        current_node = self.head_node  # Comienza desde el nodo cabeza

        # Caso especial: Si el nodo cabeza es el que se debe eliminar
        if current_node is not None and current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()  # Actualiza el nodo cabeza
            return  # Nodo eliminado, salir del método

        # Recorre la lista buscando el valor a eliminar
        while current_node is not None:
            next_node = current_node.get_next_node()  # Obtiene el siguiente nodo
            if next_node is not None and next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())  # Elimina el nodo
                return  # Nodo eliminado, salir del método
            current_node = next_node  # Avanza al siguiente nodo