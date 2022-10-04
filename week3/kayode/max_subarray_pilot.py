import itertools


def max_subarray(arr):
    # list to hold the subarrays
    subarrays = []
    # list to hold the sums of the subarrays
    subarray_sums = []
    # list to hold the maximum sum
    max_sum = []
    # loop through the array
    for i in range(len(arr)):
        # loop through the array again
        for j in range(len(arr)):
            # slice the array
            subarray = arr[i:j+1]
            # append the subarray to the subarrays list
            subarrays.append(subarray)
    # loop through the subarrays list
    for subarray in subarrays:
        # calculate the sum of the subarray
        if len(subarray) != 0:
            subarray_sum = sum(subarray)
            # append the sum to the subarray_sums list
            subarray_sums.append(subarray_sum)
    # loop through the subarray_sums list
    # for subarray_sum in subarray_sums:
        # append the maximum sum to the max_sum list
    max_sum.append(max(subarray_sums))
    # return the maximum sum
    return max(max_sum)


def max_subarray2(arr):
    # list to hold the subarrays
    subarrays = []
    # list to hold the sums of the subarrays
    subarray_sums = []
    # loop through the array
    for i, j in itertools.product(range(len(arr)), range(len(arr))):
        # slice the array
        subarray = arr[i:j+1]
        # append the subarray to the subarrays list
        subarrays.append(subarray)
    # loop through the subarrays list
    subarray_sums.extend(sum(subarray) for subarray in subarrays if len(subarray) != 0)

    max_sum = [max(subarray_sums)]
    # return the maximum sum
    return max(max_sum)

if __name__ == '__main__':
    print(max_subarray([-4, -5, -6]))
    print(max_subarray2([-4, -5, -6]))