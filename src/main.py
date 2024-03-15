import random
from faker import Faker
from event_model import EventModel,ArrayModel
from KafkaEventsFaker import KafkaEventsFaker
from topic_config import TopicConfif

fake = Faker("fr_FR")

schema = {
    'id': fake.uuid4,
    'shop': fake.company, 
    'address': fake.address,
    'pizza' : ArrayModel(EventModel({
        'name':fake.word,
        'summary': fake.catch_phrase,
        'price': lambda: round(random.uniform(1, 1000), 2)}) ,
        lambda: random.randint(1,5))
    }

def gen():
    return {'name':"Dinyad YD", 'age' : 2}

model = EventModel(schema,generator=gen)
kafka_ef = KafkaEventsFaker(topics=[
    TopicConfif("clients",model, nb_threads= 3,start_times=[0,2,21],intervals= [5,7,lambda: random.randint(1,20)]),
])
kafka_ef.start()