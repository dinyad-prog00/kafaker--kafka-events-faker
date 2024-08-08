from kafaker.data import DataRepo
from kafaker.faker import KafkaEventsFaker
from kafaker.topic import TopicConfif
from kafaker.template import customer, store, product, supplier, order, employee
import random

class KafkaOrderEvents(KafkaEventsFaker):
    def __init__(self, topic_name="orders", bootstrap_servers='localhost:9092', nb_threads=3, start_times=[0, 2, 21], intervals=[5, 7, lambda: random.randint(1, 20)], console=True, polulate_id=False):
        super().__init__(
            topics=[
                TopicConfif(topic_name, order,
                            nb_threads=3,
                            start_times=[0, 2, 21],
                            intervals=[5, 7, lambda: random.randint(1, 20)])
            ],
            repositoies=[
                DataRepo("customers", customer, 300),
                DataRepo("employees", employee, 20),
                DataRepo("stores", store, 50),
                DataRepo("suppliers", supplier, 50),
                DataRepo("products", product, 200)
            ],
            bootstrap_servers=bootstrap_servers,
            console=console,
            polulate_id=polulate_id
        )
