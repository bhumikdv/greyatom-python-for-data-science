def main():
    # Write code here 
    while True:
        N=int(input())
        if 1<=N and N<=100:
            break
    List_elements=[]
    List_elements=[int(x) for x in input().split()]
        #List_elements.append(element)
        
    List_elements.sort()
    print(List_elements)
    
    Absent_students=[]
    
    for i in range(N):
        if i+1 not in List_elements:
            Absent_students.append(i+1) 
    
    print(" ".join(str(x) for x in Absent_students))

main()