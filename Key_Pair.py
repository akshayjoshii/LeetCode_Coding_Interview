def key_pair(arr, k):
    counter = 0
    check = set()
    for num in arr:
        if num in check:
            counter += 1
        check.add(k - num)
    if counter >= 1:
        return ("Key pairs found: {}".format(counter))
    else:
        return "No Key Pairs found"

print(key_pair([10, 15, 2, 5, 3, 4, 1], 7))
