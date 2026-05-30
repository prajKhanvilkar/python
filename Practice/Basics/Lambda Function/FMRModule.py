def filterx(Task, Elements):
    result = list()
    for no in Elements:
        ret = Task(no)
        if(ret == True):
            result.append(no)  
    return result

def mapx(Task,Element):
    result =list()
    for no in Element:
        ret = Task(no)
        result.append(ret)
    return result   

def reducex(Task,Element):
    sum = 0
    for no in Element:
         sum = Task(sum,no)
    return sum  
