# python3

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        # use a list or a deque (to access last element) finish_time
        # store in finish_time the times when the computer will 
        #   finish processing the packets
        self.finish_time = []

    def Process(self, request):
        

        if len(self.finish_time)==0: # if finish_time is empty when a new packet arrives, start processing immediately
            self.finish_time.append(request.arrival_time + request.process_time)
            return Response(False,request.arrival_time)
        # when a new packet arrives, first pop from the front of finish_time
        #   all the packets which are already processed by the time the new packet arrives
        while self.finish_time and self.finish_time[0] <= request.arrival_time:
            self.finish_time.pop(0)

        if len(self.finish_time)==0: #check again if we've popped it
            self.finish_time.append(request.arrival_time + request.process_time)
            return Response(False,request.arrival_time)
        
        if len(self.finish_time)<self.size: #if the buffer is not full
            self.finish_time.append(self.finish_time[-1] + request.process_time)
            return Response(False, self.finish_time[-2])
        else: #if the buffer is full
            return Response(True,-1)

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buf):
    responses = []
    for request in requests:
        responses.append(buf.Process(request))
    return responses

def PrintResponses(responses):
    # output the processing start time for each packet instead of processing finish time
    # or -1 if it was dropped
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count) # requests with arrival_times and process_times read from input

    # process requests with arrival_times and process_times in a buffer of size buf
    # and store the finish times of each request in finish_times
    buf = Buffer(size)
    responses = ProcessRequests(requests, buf) 

    PrintResponses(responses)
