from enum import Enum
from collections import deque, Counter

# Enumeración para definir los estados de un pedido
class OrderStatus(Enum):
    PENDING = 1;     # Pedido pendiente de ser procesado
    SHIPPED = 2;     # Pedido enviado
    DELIVERED = 3;   # Pedido entregado
    
# Clase para representar un pedido
class Order:
    def __init__(self, 
                 id: int,
                 description="",
                 status: OrderStatus=OrderStatus.PENDING):
        self.id = id;
        self.description = description;
        self.status = status;

    def __repr__(self):
        return f"Order(id={self.id}, status={self.status}, description={self.description})";

# Clase de gestión de pedidos
class OrderManager:
    def __init__(self):
        self.orders_queue = deque(); # Cola de pedidos pendientes
        self.orders = {};            # Diccionario para almacenar pedidos en función de su ID

    def add_order(self, order_id: int, order_description=""):
        """ Agrega un nuevo pedido con estado PENDING. """
        order = Order(id=order_id, description=order_description);
        self.orders_queue.append(order);  # Agrega el pedido a la cola
        self.orders[order_id] = order;          # Guarda el pedido en el diccionario de pedidos
        print(f"Added: {order}");

    def update_order_status(self, 
                            order_id: int, 
                            new_status: OrderStatus=OrderStatus.PENDING,
                            new_description=""):
        """ Actualiza el estado de un pedido existente. """
        if order_id in self.orders:
            order = self.orders[order_id];
            order.status = new_status;
            order.description = new_description;
            print(f"Updated: {order}");
        else:
            print(f"Order with ID '{order_id}' not found.");

    def list_orders_by_status(self, order_status: OrderStatus):
        """ Lista todos los pedidos con un estado específico. """
        orders_by_status = [order for order in self.orders.values() if order.status == order_status];
        print(f"Orders with status {order_status.name}: {orders_by_status}");

    def get_order_count_by_status(self) -> Counter:
        """ Devuelve el conteo de pedidos en cada estado. """
        status_counter = Counter(order.status for order in self.orders.values());
        return status_counter;
    
"Ejemplo de ejecución..."

order_manager = OrderManager();
order_manager.add_order(order_id=1);
order_manager.add_order(order_id=2, order_description="Pedido Meli 1");
order_manager.add_order(order_id=3, order_description="Pedido Alibaba 1");

order_manager.add_order(order_id=4, order_description="Pedido Amazon 2");
order_manager.add_order(order_id=5, order_description="Pedido Meli 2");
order_manager.add_order(order_id=6, order_description="Pedido Alibaba 2");

order_manager.add_order(order_id=7, order_description="Pedido Amazon 3");
order_manager.add_order(order_id=8, order_description="Pedido Meli 3");
order_manager.add_order(order_id=9, order_description="Pedido Alibaba 3");

print(f"Order registered (Dictionary): {order_manager.orders}");
print(f"Order registered (Queue): {order_manager.orders_queue}");

order_manager.update_order_status(order_id=4, new_status=OrderStatus.SHIPPED, new_description="TEST");
order_manager.update_order_status(order_id=5, new_status=OrderStatus.SHIPPED);
order_manager.update_order_status(order_id=6, new_status=OrderStatus.SHIPPED);

order_manager.update_order_status(order_id=7, new_status=OrderStatus.DELIVERED);
order_manager.update_order_status(order_id=8, new_status=OrderStatus.DELIVERED);
order_manager.update_order_status(order_id=9, new_status=OrderStatus.DELIVERED);

order_manager.list_orders_by_status(OrderStatus.SHIPPED);


