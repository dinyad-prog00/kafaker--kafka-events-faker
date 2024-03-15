from datetime import datetime
from typing import Dict, Sequence
from faker import Faker

class ModelBase:
    def get_event(self):
        return self._get()
    def _get(self) -> Dict | Sequence[Dict]:
        return {}

class EventModel(ModelBase):
    def __init__(self, schema, generator=None, faker_local:str | Sequence[str] | Dict[str, int | float] | None = None) -> None:
        super().__init__()
        self.schema = schema
        self.generator=generator
        self.fake = Faker(faker_local)
        pass
        
    def get_event(self):
        if self.generator != None:
            event= self.generator()
        else:
            event = self._get()
        event['event_time'] = datetime.now().isoformat(timespec='milliseconds')
        return event
    
    def _get(self):
        event = {}

        for key, value in self.schema.items():
            if callable(value):
                event[key]=value()
            elif isinstance(value,ModelBase):
                event[key]= value.get_event()
            else:
                event[key]=None
        
        return event
    
class ArrayModel(ModelBase):
    def __init__(self,model:EventModel,size:int) -> None:
        super().__init__()
        self.model = model
        self.size = size
    
    def _get(self) -> Dict | Sequence[Dict]:
        if(callable(self.size)):
            nb=self.size()
        else:
            nb= self.size
        return [self.model.get_event() for i in range(nb)]
        
