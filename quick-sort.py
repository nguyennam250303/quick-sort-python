# quick-sort-python
def quicksort(a):

    if len(a) < 2:

        return a

    k = a[0]

    l = [i for i in a[1:] if i <= k]

    r = [i for i in a[1:] if i > k]

    return quicksort(l) + [k] + quicksort(r)
