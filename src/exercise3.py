def dictComp(stop, step):
  ''' dictComp function accepts 2 arguments (stop,step) 
  The variables in this function are: numbers(a list of numbers),
  value(a list with four numbers each in each index),
  keyFormat(the string to be joined to a list of numbers),
  keys(the keys to be used in the dictionary comprehension),
  dictionary(the dictionary consisting of keys:values)''' 

  #create a numbers and values list for the dictionary comprehension
  numbers =[i for i in range(1,stop+1)]
  value=[numbers[a:a+step] for a in range(0,stop,step) if len(numbers[a:a+step])==step]
  #store the string value to be joined to numbers so as to create the key
  keyFormat = "items-"
  keys =[keyFormat+str(x) for x in range(1,len(value)+1)]
  #create the dictionary 
  dictionary = {keys[j]:value[j] for j in range(len(value))}

  return dictionary  
        
print(dictComp(9,2))
print(dictComp(11,3))
print(dictComp(15,4))
print(dictComp(14,5))

