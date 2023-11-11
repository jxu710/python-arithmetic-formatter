def arithmetic_arranger(problems):
  
  arranged_problems = ""
  # 1st type pf error
  if len(problems) > 5:
    return "Error: Too many problems."

  # 2nd error, to see if operators are "+" or "-" only
  for problem in problems:
    item = problem.split(" ")
    # print(item)

    operator = ["+","-"]
    if item[1] not in operator:
      return "Error: Operator must be '+' or '-'."

    # 3rd error, to see if numbers are digits only
    if item[0].isdigit() and item[2].isdigit() is False:
      return "Error: Numbers must only contain digits."

    # 4th error
    if len(item[0]) > 4 or len(item[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    # find the longest of numbers 
    longest_number = max(len(item[0]), len(item[2]))
    # length of the longest number + 2 for the space
    width = (longest_number + 2)  

    # to show the operation format

    every_problems = f"{item[0]:>{width}}\n{item[1]:>{width}}{item[2]:>{width}}\n{'-'* width}"

    # arranged_problems += every_problems
    print(every_problems)
  return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))