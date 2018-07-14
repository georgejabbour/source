# python3

#takes a lot of memory but gets the job done..
class Phonebook:
    def __init__(self):
        self.entries = [None] * 10000000

    def add(self, name, number):
        self.entries[number]=name

    def delete(self,number):
        if self.entries[number] != None:
            self.entries[number]=None

    def find(self,number):
        if self.entries[number]==None:
            return "not found"

        return self.entries[number]

def read_queries():
    n = int(input())
    return [Phonebook(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    """Helper function which reads queries from standard input,
    runs phonebook manager and sends the results to standard output.
    """
    for query in queries:
        q = query.split()
        todo = q[0]
        num = int(q[1])
        if todo == "add":
            phonebook.add(q[2],num)
        elif todo == "find":
            print(phonebook.find(num))
        elif todo == "del":
            phonebook.delete(num)


if __name__ == '__main__':
    phonebook = Phonebook()
    qNum = int(input())
    qs = [input() for i in range(qNum)]

    process_queries(qs)

