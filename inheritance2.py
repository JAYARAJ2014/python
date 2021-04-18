##Reasonable example of inheritance. 

class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__():
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True
        print("File opened")

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False
        print("File closed")


class FileStream(Stream):
    def read(self):
        print("Reading... data from file")


class NetworkStream(Stream):
    def read(self):
        print("Reading... data from network")


