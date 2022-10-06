class Solution:
   def isValid (self, sequence: str):
       '''
       Function to pair if sequence contains valid parenthesis
       :param sequence: Sequence of brackets
       :return: True is sequence is valid else False
       '''
       stack = []
       opening = set('([{')
       closing = set(')]}')
       pair = {')' : '(' , ']' : '[' , '}' : '{'}
       for i in sequence :
           if i in opening :
               stack.append(i)
           if i in closing :
               if not stack :
                   return False
               elif stack.pop() != pair[i] :
                   return False
               else :
                   continue
       if not stack :
           return True
       else :
           return False

if __name__ == '__main__':
   sequence = '{[()]}'
   print(f'Is {sequence} valid ? : {Solution().isValid(sequence)}')
   sequence1 = '{[()]}{]{}}'
   print(f'Is {sequence1} valid ? : {Solution().isValid (sequence1)}')
   



######################################################################################
# Python program to check for
# balanced parentheses in a string


# Function to check for
# balanced parentheses in a string


def check_parentheses(st, N):
    ans = True

    s = []

    for i in st:
        # push if opening bracket

        if i == "(" or i == "[" or i == "{":
            s.append(i)

        else:

            if len(s) > 0:

                # check if top of s is pair of current
                # element

                temp = s[len(s) - 1]
                s.pop()

                if i == "(" and temp != ")":
                    ans = False
                    break

                if i == "[" and temp != "]":
                    ans = False
                    break

                if i == "{" and temp != "}":
                    ans = False
                    break

            # if stack is empty, not balanced

            else:
                ans = False
                break

    # If stack is not empty after traversal
    # then not balanced

    if len(s) > 0:
        ans = False

    if ans:
        print("balanced")
    else:
        print("Not balanced")


# Driver code

s = "(){}([])"
N = len(s)

check_parentheses(s, N)








