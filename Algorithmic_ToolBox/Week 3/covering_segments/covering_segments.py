# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    seg_text = segments
    points = []
    inx = segments[0][1]
    a = 0

    for i, j in segments:
        if inx < i:
            points.append(inx)
            inx = j
        if inx > i and inx > j:
            inx = j
        # print(i, j, inx)

    points.append(inx)

    return(points)

if __name__ == '__main__':
    k = sys.stdin.read()
    n, *data = map(int, k.split())
    segments = sorted(list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2]))))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
