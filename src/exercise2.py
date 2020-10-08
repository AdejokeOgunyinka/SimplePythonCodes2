def quadraticSolver(a, b, c):
  ''' quadraticSolver function solves quadratic equations. It takes in
  3 arguments(a,b,c). The variables in these function are:
  rootExpression, x1(first root) and x2(second root)'''
  # Using try and except statement to catch the Zero Error
  try:   
    '''solving the square root side of the formula and storing it 
    with variable "rootExpression" '''
    rootExpression = ((b*b)-(4*a*c))**0.5
    # calculating the first root of the equation
    x1 = (-b + rootExpression)/(2*a)
    #calculating the second root of the equation
    x2 = (-b - rootExpression)/(2*a)    
    #:.3f is to format the answers to 3 decimal places
    return "x = {:.3f} or {:.3f} ".format(x1,x2)
  except ZeroDivisionError:
    return("Zero Division Error!!: the value of 'a' cannot be 0")
  
print(quadraticSolver(2,5,3))
print(quadraticSolver(-2, 6, 4))
print(quadraticSolver(1,-4,5))
print(quadraticSolver(-3,9,-4))
print(quadraticSolver(1,2,3))
print(quadraticSolver(0,3,5))