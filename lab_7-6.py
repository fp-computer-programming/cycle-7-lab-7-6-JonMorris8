"""
Create a Python file named lab_7-6.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a 2 separate functions within the same document. 
Create a 3rd function which requires both the first two functions within it
Create 4 test cases for your 3rd function. 
"""
#author Jon Morris
def multiply_numbers(num1, num2):
    result = num1 * num2
    return result
my_product = multiply_numbers (-2, -6)
print(my_product)

def add_numbers(num1, num2):
    result = num1 +num2
    return result

my_sum = add_numbers(5, 7)

def perform_operations(num1, num2):
    #this finction performs multiplecation and addition using the multiply numbers and add numbers functions

    product = multiply_numbers(num1, num2)
    print(product)

    #call the add numbers fucntion
    sum= add_numbers(num1, num2)
    print(sum)

    #display the results
    print("f*multiplecation results : {product}")
    print(f"addition result: {sum}")

#test case 1 - positive numbers
perform_operations(3, 4)
#test case 2 - negative numbers
perform_operations(-2, 6)
#test case 3 - zero and positive numbers 
perform_operations(0, 9)
#test case 4 - zero and negative numbers
perform_operations(0, -5)
