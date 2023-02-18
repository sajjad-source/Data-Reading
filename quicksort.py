def compare_func(a, b): #compare func
    if a <= b:
        return True
    else:
        return False


def swap(the_list, i, j): #swap helper func to swap to values
    the_list[i], the_list[j] = the_list[j], the_list[i]


def partition(the_list, compareFunc, p, r): #partition func
    i = p - 1 #i is behind p
    j = p #j is = p
    pivot = the_list[r] #pivot is the value at index r
    while j < r: #while j < r
        if compareFunc(the_list[j], pivot): #if the value at index j is smaller or equal to the pivot
            i += 1 #increase i
            swap(the_list, i, j) #swap the value at index j with index val at index i

        j += 1 #increment j

    swap(the_list, i + 1, j) #when loop reached the end (i.e j is r), swap the value of the pivot in front of i

    return i + 1 #return the index at which the pivot is at


def quicksort(the_list, compareFunc, p, r): #quicksort func
    if p < r: #if p < r
        q = partition(the_list, compareFunc, p, r) #assign q to partition func call
        quicksort(the_list, compareFunc, p, q - 1) #recursively call quicksort with partition from p to q - 1
        quicksort(the_list, compareFunc, q + 1, r) #recursively call quicksort with partition from q + 1 to r




def sort(the_list, compareFunc): #sorting func
    quicksort(the_list, compareFunc, p=0, r=len(the_list) - 1) #call quicksort from p=0 to end of the list




