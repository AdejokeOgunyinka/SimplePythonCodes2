def nameValidator(name):
  ''' nameValidator function validates the name argument that is passed
  into the function.
  '''
  # checking if the name type is not a string
  if type(name)!= str:
    #raises a value error
    raise ValueError("This is not a string")
  else: 
    #if the type is string, then split the name into substrings   
    listName = name.split(" ")
    #if the length of the substrings is not equal to 2, raise an error
    if len(listName)!=2:
      raise ValueError ("Your name should contain your Firstname and Surname")
      #else if len(substrings)==2,check if all the elements in the substrings
      #are alphabets
    elif all(x.isalpha() for x in listName):
      '''for all elements in the list, check the length of the name(between 5&20)'''
      for num in range(len(listName)):
        if 5<=len(listName[num-1])<=20 and 5<=len(listName[num])<=20:
          return name + ", your name is valid"
        else:
          #return error if the length of any of the substrings is either beyond 20 or less than 5
          raise ValueError("Your firstname or(and) lastname has exceeded 20 letters(or characters) or is less than 5 characters")
    else:
      #return error if there is a non-alphabet in the 'name' 
      raise ValueError("Something is not an alphabet")
