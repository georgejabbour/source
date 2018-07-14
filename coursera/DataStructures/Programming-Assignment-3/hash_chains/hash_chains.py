# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        ## store all strings in one list
        #self.elems = []
        self.buckets = [[]]*bucket_count #[[],[],[],[],[],[]] a bunch of buckets that hold strings

    def _hash_func(self, s): #PolyHash from lecture
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def add(self, string):
        """
        add("hello")
        buckets[helloHash]=['hello']
        add("world") # assume for simplicity it has the same hash
        buckets[worldHash]=['hello']+['world'] = ['hello','world']

        """
        stringHash = self._hash_func(string)
        bucket = self.buckets[stringHash]
        if string not in bucket:
            self.buckets[stringHash] = [string] + bucket

    def delete(self, string):
        stringHash = self._hash_func(string)
        bucket = self.buckets[stringHash]
        for buck in range(len(bucket)): #deletes first instance of the string
            if string==bucket[buck]:
                bucket.pop(buck)
                break #stops after deleting one instance

    def find(self, string):
        stringHash = self._hash_func(string) #find where the string would have gone
        if string in self.buckets[stringHash]: #if it actually is there...
            return "yes" #...then say so
        return "no" #otherwise say no

    def check(self, hashh):
        return self.buckets[hashh] #return whatever is in that hash, which is default of []

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain): #this prints out the chain with the hash 'chain'
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        qt=query.type
        if qt == 'check':
            print(' '.join(proc.check(query.ind)))
        elif qt == 'find':
            print(proc.find(query.s))
        elif qt == 'add':
            proc.add(query.s)
        elif qt =='del':
            proc.delete(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
