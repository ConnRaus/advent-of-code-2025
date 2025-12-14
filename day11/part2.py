from collections import defaultdict
from functools import lru_cache

with open("input.txt") as f:
    lines = [x.strip().split(' ') for x in f.readlines()]

graph = defaultdict(tuple)
for line in lines:
    fromNode, toNodes = line[0].replace(':', ''), line[1:]
    graph[fromNode] = tuple(toNodes)
    # ^ typechecker might hate this, its fine

# im not even sure why i had graph as an input to the
# function in part 1. just memoize with lru_cache 
@lru_cache
def count_paths(node, target):
    if node == target: return 1
    return sum(count_paths(next, target) for next in graph[node])

# looking for two paths, multiply individual parts to get total paths: 
# svr -> dac -> fft -> out 
svr_dac = count_paths('svr', 'dac')
dac_fft = count_paths('dac', 'fft')
fft_out = count_paths('fft', 'out')
path1_paths = svr_dac * dac_fft * fft_out

# svr-> fft -> dac -> out
svr_fft = count_paths('svr', 'fft')
fft_dac = count_paths('fft', 'dac')
dac_out = count_paths('dac', 'out')
path2_paths = svr_fft * fft_dac * dac_out

print(path1_paths + path2_paths)
