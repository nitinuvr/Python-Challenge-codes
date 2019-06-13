def  looknsay(N):
    i, j, k, l =0, 0, 1, 0
    looksay= []
    number = 11
	
    if N=='1':
        return 1
    elif N=='2':
        return 11
    
    else:
        while i<N-2:
            while j<len(str(number)):
                l = str(number)[j]
               
                j+=1
                
                
                if j>=len(str(number)):
                    looksay.append(str(k))
                    looksay.append(str(l))
                    k = 1
                    
                elif str(number)[j]!=str(number)[j-1]:
                    looksay.append(str(k))
                    looksay.append(str(l))
                    k =1
                    
                elif str(number)[j]==str(number)[j-1]:
                    k+=1
                    
        
            j = 0
            i+=1
            
            number = int(''.join(looksay))
            
            looksay = []
        
        
        return number
        
num = int(input("Insert Term Number Here: "))
print(len(str(looknsay(num))))