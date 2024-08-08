from datetime import datetime
from typing import Sequence
from kafka import KafkaProducer
from faker import Faker
import json
import time
import threading
from threading import Thread
from .data import DataRepo
from .topic import TopicConfif


class KafkaEventsFaker:
    def __init__(self, topics=Sequence[TopicConfif], repositoies=Sequence[DataRepo], bootstrap_servers='localhost:9092', console=True, polulate_id=False):
        self.topics = topics
        self.repositories = repositoies
        self.console = console
        self.polulate_id = polulate_id
        if not console:
            self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def _generate_events(self, topic, model):
        event = model.get_event(self.repos_datas, self.polulate_id)
        event['event_time'] = datetime.now().isoformat(timespec='milliseconds')
        if self.console:
            print(json.dumps(event, indent=2))
        else:
            self.producer.send(topic, value=event)
            self.producer.flush()

    def _generate_events_threaded(self, topic, model, start_time, interval, tag):
        time.sleep(start_time)
        while True:
            if self.console:
                print("\n{} ======================================\n".format(tag))
            else:
                print("{} : Sent +++".format(tag))
            self._generate_events(topic, model)
            time.sleep(interval)

    def _create_thread(self, topic, model, start_time, interval, tag):
        itvl = self._get_value_fct(interval)
        thread = threading.Thread(target=self._generate_events_threaded, args=(
            topic, model, start_time, itvl, tag))
        thread.start()
        return thread

    def start(self):
        self._build_repos()
        print("Kafka events faker is started....")
        threads = []

        for config in self.topics:
            for i in range(config.nb_threads):
                th = self._create_thread(
                    config.name, config.model, config.start_times[i], config.intervals[i], "{}-{}".format(config.name, i+1))
                threads.append(th)

        for thread in threads:
            thread.join()

    def _get_value_fct(self, value):
        if (callable(value)):
            return value()
        else:
            return value

    def _build_repos(self):
        repos_datas = {}
        for repo in self.repositories:
            d = repo.build(repos_datas,self.polulate_id)
            repos_datas[repo.name] = d
        self.repos_datas = repos_datas
    def add_topic(self,topic: TopicConfif):
        self.topics.append(topic)
