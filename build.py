import operator


def solution_asc(dic):
    '''
    Enter your code here
    '''
    # return sorted(dic.items(), reverse=True, key= lambda x:x[1])
    return sorted(dic.items())
def solution_desc(dic):
    '''
    Enter your code here
    '''
    return sorted(dic.items(), reverse = True)
