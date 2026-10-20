def grade(a) :

    A= 4.5
    B = 3.5
    C = 2.5
    F = 0

    for i in range (len(a)):    
        if grade(a[i]) >= 90 : 
            a[i]*=A
        elif grade(a[i]) >= 80:
            a[i]*=B
        elif grade(a[i]) >= 70:
            a[i]*=C 
        else :
            a[i]*=F

        return a 
