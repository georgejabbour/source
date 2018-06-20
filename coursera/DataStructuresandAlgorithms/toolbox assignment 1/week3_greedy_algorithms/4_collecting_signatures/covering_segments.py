# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    length = len(segments)
    while len(segments)>1:
        if segments[0].end-segments[1].start >=0:
            del segments[1]
        else:
            points.append(segments[0].end)
            del segments[0]
    points.append(segments[0].end)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    segments = sorted(segments, key=lambda s: s.end)
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
