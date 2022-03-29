### Given an array (or string), the task is to reverse the array/string.
###Input  : arr[] = {1, 2, 3}
###Output : arr[] = {3, 2, 1}


def reverse_it(s,arr):
    rev_str = s[::-1]
    rev_arr = arr[::-1]
    return rev_str,rev_arr

### Using recursion
def reverse_it_using_rec(s):
    if len(s) is 1:
        return s
    
    rev = ""
    rev = s[len(s)-1] + reverse_it_using_rec(s[:len(s)-1])
    return rev




if __name__ == '__main__':
    s=input()  #string
    arr=[int(i) for i in input().split()]
    print(reverse_it(s,arr))
    print(reverse_it_using_rec(s))