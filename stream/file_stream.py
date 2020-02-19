from stream import Stream


class FileStream(Stream):
    def __init__(self, filename):
        super(FileStream, self).__init__()
        self.first = True
        self.tupleCounter = 0
        self.startTime = 0
        self.endTime = 0 
        self.stream_file = open(filename)
        self.num_facts = {}

    def get_fact(self):
        line_list = self.stream_file.readline().split()
        if (len(line_list) > 1):
            predicate = line_list[0]
            groundings = line_list[1:]
            return predicate, groundings
        return None 

    def read_timeline(self):
        line_list = self.stream_file.readline().split()
        if (len(line_list) == 2):
            self.startTime = int(line_list[0])
            self.endTime = int(line_list[1])
            self.timeLine = {
                "startTime": self.startTime,
                "endTime"  : self.endTime 
            }

    def getNumberOfTuplesAt(self, t):
        return self.num_facts[t]

    def getTimeLine(self):
        if self.first:
            self.read_timeline() # skiping first line which contains info
            self.first = False
        return self.timeLine

    def hasTimePoint(self, t):
        if self.first:
            self.read_timeline() # skiping first line which contains info
            self.first = False
        return t >= self.startTime and t <= self.endTime 

    def get(self, t):
        result = dict() 
        if self.first:
            self.read_timeline() # skiping first line which contains info
            self.first = False
        has_fact = True
        facts_read = 0
        while has_fact:
            row = [t, self.timeLine["endTime"], self.tupleCounter, None]
            fact = self.get_fact()
            if fact is not None:
                predicate, constant_list = fact;
                row.extend(constant_list)
                if predicate not in result:
                    result[predicate] = set()
                result[predicate].add(tuple(row))
                facts_read += 1
            else:
                has_fact = False
        self.num_facts[t] = facts_read
        return result 
