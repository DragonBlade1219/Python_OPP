from collections import deque

def manage_delivery_queue() -> deque:
    # Crea una cola para gestionar entregas de productos.
    
    delivery_deque = deque(["order_1","order_2","order_3"]);
    delivery_deque.append("order_4"); # Agrega al final de la cola.
    delivery_deque.appendleft("order_0"); # Agrega al inicio de la cola.
    print(delivery_deque);
    delivery_deque.pop();
    delivery_deque.popleft();
    
    return delivery_deque;

queue = manage_delivery_queue();
print(queue);
