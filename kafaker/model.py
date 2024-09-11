from datetime import datetime
import random
import inspect
from typing import Dict, Sequence
from faker import Faker


class ModelBase:
    def get_event(self, repos_datas=None, polulate_id=False):
        return self._get(repos_datas, polulate_id)

    def _get(self, repos_datas=None, polulate_id=False) -> Dict | Sequence[Dict]:
        return {}


class EventModel(ModelBase):
    def __init__(self, schema, generator=None, faker_local: str | Sequence[str] | Dict[str, int | float] | None = None) -> None:
        super().__init__()
        self.schema = schema
        self.generator = generator
        self.fake = Faker(faker_local)
        pass

    def get_event(self, repos_datas=None, polulate_id=False):
        if self.generator != None:
            event = self.generator()
        else:
            event = self._get(repos_datas, polulate_id)
        # event['event_time'] = datetime.now().isoformat(timespec='milliseconds')
        return event

    def _get(self, repos_datas=None, polulate_id=False):
        event = {}

        for key, value in self.schema.items():     
            if isinstance(value, ModelBase):
                event[key] = value.get_event(repos_datas, polulate_id)
                
            elif callable(value):
                params = []
                for name in inspect.signature(value).parameters:
                    if name.startswith("__"):
                        params.append(event[name[2:]])    
                event[key] = value(*params)
            else:
                event[key] = None

        return event


class ArrayModel(ModelBase):
    def __init__(self, model: EventModel, size: int) -> None:
        super().__init__()
        self.model = model
        self.size = size

    def _get(self, repos_datas=None, polulate_id=False) -> Dict | Sequence[Dict]:
        if (callable(self.size)):
            nb = self.size()
        else:
            nb = self.size
        return [self.model.get_event(repos_datas, polulate_id) for _ in range(nb)]


class FromRepo(ModelBase):
    def __init__(self, repo_name) -> None:
        self.repo_name = repo_name

    def get_event(self, repos_datas=None, polulate_id=False):
        return self._get(repos_datas, polulate_id)

    def _get(self, repos_datas=None, polulate_id=False) -> Dict | Sequence[Dict]:
        if repos_datas == None:
            return None
        else:
            return random.choice(repos_datas[self.repo_name], polulate_id)


class IdRepo(ModelBase):
    def __init__(self, repo_name) -> None:
        self.repo_name = repo_name

    def get_event(self, repos_datas=None, polulate_id=False):
        return self._get(repos_datas, polulate_id)

    def _get(self, repos_datas=None, polulate_id=False) -> Dict | Sequence[Dict]:
        if repos_datas == None:
            return None
        else:
            evt = random.choice(repos_datas[self.repo_name])
            if evt != None:
                return evt if polulate_id else evt['id']
