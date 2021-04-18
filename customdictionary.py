class TagCloud:
    def __init__(self):  ## __init__ is constructor.
        self.__tags = {}  # __ is treated like private

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0)+1

    def __getitem__(self, tag):  # __getitem__ is used so that you can access the element using square brackets as in Line 25
        return self.__tags.get(tag.lower(), 0) 

    def __setitem__(self, tag, count):
        self.__tags[tag.lower] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("Python")
print(cloud["PYTHON"])
