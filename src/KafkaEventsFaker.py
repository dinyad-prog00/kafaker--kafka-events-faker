from typing import Sequence
from kafka import KafkaProducer
from faker import Faker
import json
import time
import threading

from event_model import EventModel
from topic_config import TopicConfif

class KafkaEventsFaker:
    def __init__(self, topics= Sequence[TopicConfif] ,bootstrap_servers='localhost:9092'):
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        self.topics=topics
        

    def _generate_events(self, topic,model):
        self.producer.send(topic, value=model.get_event())
        self.producer.flush()

    def _generate_events_threaded(self,topic,model,start_time,interval,tag):
        time.sleep(start_time)
        while True:
            self._generate_events(topic,model)
            print("{} : Sent +++".format(tag))
            time.sleep(interval)
            
    
    def _create_thread(self,topic,model,start_time,interval,tag):
        itvl = self._get_value_fct(interval)
        thread = threading.Thread(target=self._generate_events_threaded,args=(topic,model,start_time,itvl,tag))
        thread.start()
        return thread
        
    def start(self):
         print("Kafka events faker is started....")
         threads=[]

         for config in self.topics:
             for i in range(config.nb_threads):
                 th = self._create_thread(config.name,config.model,config.start_times[i],config.intervals[i],"{}-{}".format(config.name,i+1))
                 threads.append(th)
                 
         for thread in threads:
            thread.join()
             


    def _get_value_fct(self,value):
        if(callable(value)):
            return value()
        else:
            return value


