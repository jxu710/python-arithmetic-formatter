def arithmetic_arranger(problems):
  arranged_problems = ""

  # 1st type of error
  if len(problems) > 5:
      return "Error: Too many problems."

  top_lines = []
  bottom_lines = []
  dash_lines = []

  for problem in problems:
      item = problem.split()

      operator = ["+", "-"]
      # 2nd error, to see if operators are "+" or "-" only
      if item[1] not in operator:
          return "Error: Operator must be '+' or '-'."

      # 3rd error, to see if numbers are digits only
      if not item[0].isdigit() or not item[2].isdigit():
          return "Error: Numbers must only contain digits."

      # 4th error
      if len(item[0]) > 4 or len(item[2]) > 4:
          return "Error: Numbers cannot be more than four digits."

      # find the longest of numbers 
      longest_number = max(len(item[0]), len(item[2]))
      # length of the longest number + 2 for the space
      width = (longest_number + 2)  

      top_lines.append(f"{item[0]:>{width}}")
      bottom_lines.append(f"{item[1]}{item[2]:>{width-1}}")
      dash_lines.append('-' * width)

  # Combine the lines to form the output
  # takes each element in the top_lines list (which contains the top lines of each problem) and joins them together with four spaces in between each element.
  arranged_problems += "    ".join(top_lines) + "\n"
  arranged_problems += "    ".join(bottom_lines) + "\n"
  arranged_problems += "    ".join(dash_lines)

  return arranged_problems

