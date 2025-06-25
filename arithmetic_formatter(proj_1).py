def arithmetic_arranger(problems, show_answers=False):
    # result = ""
    if len(problems) > 5:
        return 'Error: Too many problems.'
    first_line = []
    # operator_line = []
    second_line = []
    dash_line = []
    answers = []
    for problem in problems:
        part = problem.split()
        num1, operator, num2 = part
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits"
        # first_line.append(num1)
        
        # # operator_line.append(operator)
        # second_line.append(operator + num2)
        # dash_line.append('----')
        width = max(len(num1), len(num2)) + 2
        first_line.append(num1.rjust(width))
        second_line.append(operator + ' ' + num2.rjust(width - 2))
        dash_line.append('-' * width)
        if show_answers:
           result = str(int(num1) + int(num2)) if operator == '+' else str(int(num1) - int(num2))
           answers.append(result.rjust(width))

        arranged = ('    '.join(first_line) + '\n' + 
                    '    '.join(second_line) + '\n' +
                    '    '.join(dash_line))
        if show_answers:
            arranged += '\n' + '    '.join(answers)
        
    #     result = "\n".join(part)
    #     parts.append(result)
    
    # for vertical in parts:
    #     print(vertical)
    #     print()
    #     # print(result)   
    return arranged


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
# print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
# problems = ['32 + 64', '68 + 69']
# result = ""

# for problem in problems:
    
#     part = problem.split()
#     result += "\n".join(part) + "\n"
    
# print(result)