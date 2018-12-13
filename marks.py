def grades():
    marks = [23,4,5,6,64,90,67,98,45,23,67,78,89]
    list1=[]
    list2=[]
    for mark in marks:
        if mark > 50:
            list1.append(mark)
        elif mark < 50:
            list2.append(mark)
    for mark in list1:
        if mark >= 90 and mark <= 100:
            print (str(mark)+' '+'Excellent')   
        elif mark >= 70 and mark <= 89:
            print (str(mark)+' '+'very good') 
        elif mark >= 60 and mark <= 69:
            print (str(mark)+' '+'good')     
        else:
            print (str(mark)+' '+'poor')          

    for mark in list2:
        if mark >= 40 and mark <= 50:
            print (str(mark)+' '+'poor')  
        elif mark >= 20 and mark <= 39:
            print (str(mark)+' '+'very poor') 
        else:
            print (str(mark)+' '+'repeat')    


grades()
