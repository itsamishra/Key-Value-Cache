import time

# Class representing single data point (key-value)
class Data:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        self.last_update_timestamp = time.time()

    def set_last_update_timestamp(self, new_timestamp):
        self.last_update_timestamp = new_timestamp


# Cache holding
class Cache:
    def __init__(self):
        self.cacheDict = dict()

    def add_data(self, key: str, data: Data):
        self.cacheDict[key] = data

    def remove_data(self, key: str):
        pass

    def update_data(self, key: str, data: Data):
        pass
