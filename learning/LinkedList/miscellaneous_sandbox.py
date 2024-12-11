from Node_sandbox import Node
from LinkedList_sandbox import LinkedList
def nth_last_element(ll, n):
    main_ptr = ll.get_head_node()
    ref_ptr = ll.get_head_node()

    # Mueve el puntero de referencia n nodos adelante
    for _ in range(n):
        if ref_ptr is None:
            return None
        ref_ptr = ref_ptr.get_next_node()

    # Mueve ambos punteros hasta que el puntero de referencia llegue al final
    while ref_ptr is not None:
        main_ptr = main_ptr.get_next_node()
        ref_ptr = ref_ptr.get_next_node()

    return main_ptr  # Devuelve el nodo