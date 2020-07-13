def dir_reduc(arr):
    for n in range(len(arr)):
        if arr[n] == 'NORTH' and arr[n+1] == 'SOUTH':
            arr.remove(arr[n] and arr[n+1])



a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dir_reduc(a))