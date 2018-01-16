# Uses python3
import sys

def get_optimal_value(capacity,weights,values):
    value = 0
    valuePerWeight = sorted([[values/weights,weights] for values,weights in zip(values,weights) ],reverse=True)

    while capacity >0 and valuePerWeight:
        maxi = 0
        idx = None
        for i,item in enumerate(valuePerWeight):        
            if item[1]>0 and item[0]>maxi:
                maxi = item[0]
                idx = i
                
        if idx is None:
            return 0
        
        w = valuePerWeight[idx][1]
        v_per = valuePerWeight[idx][0]
    
        if w >= capacity:
            value += v_per*capacity
            capacity = 0
            return value
    
        else:
            value += v_per*w
            capacity -= w
    
        valuePerWeight.pop(idx)

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
    
### Try to make changes
