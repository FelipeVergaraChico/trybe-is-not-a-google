from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.Queue = list()

    def __len__(self):
        return len(self.Queue)

    def enqueue(self, value):
        self.Queue.append(value)

    def dequeue(self):
        if len(self.Queue) == 0:
            return None
        return self.Queue.pop(0)

    def search(self, index):
        if 0 > index or index >= len(self.Queue):
            raise IndexError('Índice Inválido ou Inexistente')
        return self.Queue[index]
