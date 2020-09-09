class SmartCalc:
    def __init__(self):
        self.variables = dict()

    def precedence(self, operator):
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/':
            return 2
        elif operator == '**':
            return 3
        elif operator == '(' or operator == ')':
            return 4
        else:
            raise SyntaxError
    
    def scrub(self, operation):
        if '//' in operation:
            raise SyntaxError
        values = operation.replace('+', ' ').replace('-', ' ').replace('/', ' ').replace('*', ' ')
        for i in values.split():
            self.valid_ident(i.replace('(', '').replace('(', ''))
        for i in values:
            if i in self.variables.keys():
                operation = operation.replace(i, str(self.variables[i]))
        if any(char.isalpha() for char in operation):
            raise NameError("Unknown variable")
        elements = []
        for i in operation.split():
            if '(' in i:
                elements.append('(')
                elements.append(i.replace('(', ''))
            elif ')' in i:
                elements.append(i.replace(')', ''))
                elements.append(')')
            else:
                elements.append(i)
        return elements
    
    def postfix(self, elements):
        operators = []
        post = []
        for i in elements:
            if any(char.isdigit() for char in i):
                post.append(i)
            elif len(operators) == 0 or operators[-1] == '(':
                operators.append(i)
            elif i == '(':
                operators.append(i)
            elif i == ')':
                while len(operators) > 0 and operators[-1] != '(':
                    post.append(operators.pop())
                if len(operators) > 0:
                    operators.pop()
                else:
                    raise SyntaxError
            elif len(operators) > 0 and self.precedence(i) > self.precedence(operators[-1]):
                operators.append(i)
            elif len(operators) > 0 and self.precedence(i) <= self.precedence(operators[-1]):
                while len(operators) > 0 and self.precedence(i) <= self.precedence(operators[-1]) and operators[-1] != '(':
                    post.append(operators.pop())
                operators.append(i)
            #print(post, operators, sep='\n')
        while len(operators) > 0:
            post.append(operators.pop())
        return post
    
    def valid_ident(self, identifier):
        if any(char.isalpha() for char in identifier) and any(char.isdigit() for char in identifier):
            raise TypeError("Invalid identifier")
            
    def evaluate(self, operation):
        postfix = self.postfix(self.scrub(operation))
        equation = []
        for i in postfix:
            if any(char.isdigit() for char in i):
                equation.append(i)
            else:
                b, a = equation.pop(), equation.pop()
                equation.append(eval(str(a) + i + str(b)))
        return equation[0]
    
    def assign(self, line):
        variable = line.split('=')
        if len(variable) > 2:
            raise TypeError("Invalid assignment")
        self.valid_ident(variable[0])
        self.variables.update({variable[0].strip(): self.evaluate(variable[1])})
        return
    
    def process(self):
        line = input()
        while line != '/exit':
            try:
                if line == '/help':
                    print("The program calculates the sum of numbers")
                    line = input()
                    continue
                elif line == '':
                    line = input()
                    continue
                elif '=' in line:
                    self.assign(line)
                    line = input()
                    continue
                else:
                    print(self.evaluate(line))
                    line = input()
                    continue
            except SyntaxError:
                print("Invalid expression")
                line = input()
            except EOFError:
                print("Invalid expression")
                line = input()
            except Exception as e:
                if line[0] == '/':
                    print("Unknown command")
                else:
                    print(e)
                line = input()
                continue
        print("Bye!")

calc = SmartCalc()
calc.process()