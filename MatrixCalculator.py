class Matrix:
    
    def __init__(self, row, col, elements):
        self.row, self.col = row, col
        self.elements = [[0] * self.col for _ in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                self.elements[i][j] = elements[i][j]

    def __str__(self):
        printable = ""
        for i in range(self.row):
            for j in range(self.col):
                printable += str(self.elements[i][j]) + " "
            printable += "\n"
        return printable

class MatrixCalculator:
    
    menu = '1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinant\n0. Exit\nYour choice: '
    
    def create_matrix(self, ordinal=""):
        row, col = input(f"Enter size of {ordinal}matrix: ").split()
        print(f"Enter {ordinal}matrix: ")
        elements = [[0] * int(col) for _ in range(int(row))]
        for i in range(int(row)):
            current_row = input().split()
            if len(current_row) == int(col):
                for j in range(len(current_row)):
                    elements[i][j] = float(current_row[j])
            else:
                raise Exception("ERROR")
        return Matrix(int(row), int(col), elements)
    
    def add_matrix(self, a, b):
        if a.row == b.row and a.col == b.col:
            ret_elements = [[0] * a.col for _ in range(a.row)]
            for i in range(a.row):
                for j in range(a.col):
                    ret_elements[i][j] = a.elements[i][j] + b.elements[i][j]
        else:
            raise Exception("ERROR")
        return Matrix(a.row, a.col, ret_elements)
    
    def scalar(self, a, scale):
        ret_elements = [[0] * a.col for _ in range(a.row)]
        for i in range(a.row):
            for j in range(a.col):
                ret_elements[i][j] = float(a.elements[i][j]) * scale
        return Matrix(a.row, a.col, ret_elements)
    
    def multiply(self, a, b):
        if a.col == b.row:
            ret_elements = [[0] * b.col for _ in range(a.row)]
            for i in range(a.row):
                for j in range(b.col):
                    for k in range(a.col):
                        ret_elements[i][j] += a.elements[i][k] * b.elements[k][j]
        else:
            raise Exception("The operation cannot be performed.")
        return Matrix(a.row, b.col, ret_elements)
    
    def transpose(self, a, line):
        ret_elements = [[0] * a.row for _ in range(a.col)]
        if line == '1':
            for i in range(len(ret_elements)):
                for j in range(len(ret_elements[i])):
                    ret_elements[i][j] = a.elements[j][i]
        elif line == '2':
            for i in range(len(ret_elements)):
                for j in range(len(ret_elements[i])):
                    ret_elements[i][j] = a.elements[-(j + 1)][-(i + 1)]
        elif line == '3':
            for i in range(len(ret_elements)):
                for j in range(len(ret_elements[i])):
                    ret_elements[i][j] = a.elements[i][-(j + 1)]
        elif line == '4':
            for i in range(len(ret_elements)):
                for j in range(len(ret_elements[i])):
                    ret_elements[i][j] = a.elements[-(i + 1)][j]
        else:
            raise Exception("Invalid input")
        return Matrix(a.col, a.row, ret_elements)
    
    def determinant(self, a):
        determinant_ = 0
        if len(a) == 1:
            return a[0][0]
        elif len(a) == 2:
            return a[0][0] * a[1][1] - a[1][0] * a[0][1]
        for i in range(len(a[0])):
            submatrix = [row[:] for row in a]
            submatrix.pop(0)
            for j in range(len(submatrix)):
                submatrix[j].pop(i)
            if ((i + 1) + 1) % 2 == 0:
                determinant_ += a[0][i] * self.determinant(submatrix)
            else:
                determinant_ -= a[0][i] * self.determinant(submatrix)
        return determinant_
    
    def process(self):
        choice = input(self.menu)
        #try:
        while choice != '0':
                if choice == '1':
                    print("The result is:\n", self.add_matrix(self.create_matrix('first '), self.create_matrix('second ')), sep='')
                elif choice == '2':
                    print("The result is:\n", self.scalar(self.create_matrix(), float(input("Enter constant: "))), sep='')
                elif choice == '3':
                    print("The result is:\n", self.multiply(self.create_matrix('first '), self.create_matrix('second ')), sep='')
                elif choice == '4':
                    line = input("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line\nYour choice:")
                    print(self.transpose(self.create_matrix(), line))
                elif choice == '5':
                    print("The result is:\n", self.determinant(self.create_matrix().elements), sep='')
                elif choice == '0':
                    break
                else:
                    raise Exception("Invalid input")
                choice = input(self.menu)
        #except Exception as e:
        #    print(str(e))

calculator = MatrixCalculator()
calculator.process()