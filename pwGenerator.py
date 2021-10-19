

#generate all passwords
# for given characters
  
# Recursive helper function, 
# adds/removes characters
# until len is reached

#the w handle overwrites existing file if there is one, 
#if there is not one it creates it
file1 = open("test.txt","w")
def generate(arr, i, s, len):           
                                        
    # base case                         
    if (i == 0): # when len has
                 # been reached
      
        # print it out
        file1.write(s)
        file1.write('\n')
        print(s)
        return
      
    # iterate through the array
    for j in range(0, len):             
        
        # Create new string with 
        # next character Call 
        # generate again until 
        # string has reached its len
        appended = s + arr[j]
        #print('this is whats in j : ', j)
        generate(arr, i - 1, appended, len)
  
    return

# function to generate 
# all possible passwords
def crack(arr, len):                    
  
    # call for all required lengths     
    for i in range(1 , len + 1):        
        print(i) 
        generate(arr, i, "", len)
      
# Driver Code
#arr = ['g','d','g','3','1','2']
arr = ['G','D']
len = len(arr)
crack(arr, len)
file1.close()
