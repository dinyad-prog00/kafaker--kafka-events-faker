import random


class TopicConfig:
    def __init__(self,name,model,nb_threads=1,start_times=[0],intervals=[lambda:random.randint(1, 20)]) -> None:
        self.name=name
        self.model=model
        self.nb_threads=nb_threads
        self.intervals=intervals
        self.start_times=start_times
        

