from .model import EventModel

class DataRepo:
    def __init__(self, name, model: EventModel, size) -> None:
        self.name = name
        self.model = model
        self.size = size
        pass

    def build(self, repos_datas, polulate_id):
        datas = []
        for i in range(self.size):
            data = self.model.get_event(repos_datas, polulate_id)
            datas.append(data)
        self.datas = datas
        return datas