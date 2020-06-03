def cadbury(M,N,O,P):
    
    chocolate_Distribution_Count = 0
    length=[M,N]
    breadth=[O,P]
    
    for i in length:
        for j in breadth:
            students_Count = calculateCountOfStudents(i,j)
            chocolate_Distribution_Count += students_Count

    return chocolate_Distribution_Count

def calculateCountOfStudents(length,breadth):
    
    temp_Count = 0
    while(length !=0 and breadth !=0):
        if length > breadth:
            length = length-breadth
            temp_Count+=1
        elif length == breadth:
            length = 0
            breadth = 0
            temp_Count+=1
        else:
            breadth = breadth-length
            temp_Count+=1
            
    return temp_Count
cadbury(5,2,5,2)