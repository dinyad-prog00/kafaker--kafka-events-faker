from kafaker.faker import KafkaEventsFaker
from kafaker.topic import TopicConfig

from kafaker.template import mytest
kafkaf = KafkaEventsFaker(topics=[TopicConfig("mytest",mytest)])
kafkaf.start()