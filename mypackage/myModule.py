def top_n(items,n):
    """Return the top n items in an array in Desc order.
    Args:
        Items(array):list or an array like object with
        n (int): Number of items to return
    Return:
        array: top n items in desc order"""
    for i in range(n):
        for j in range (len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    # getting the last two items
    top_n=items[-n:]
    #return in desc order
    return top_n[::-1]
                