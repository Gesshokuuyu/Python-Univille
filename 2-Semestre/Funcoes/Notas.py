def CalculateGrade(grade:float):
    if(grade > 10 or grade < 0):
        print("Invalid Grade.")
        return

    code = ""
    if(grade >= 9):
        code = "A"
    elif(grade >= 8 and grade < 9):
        code = "B"
    elif(grade >= 7 and grade < 8):
        code = "C"
    elif(grade >= 6 and grade < 7):
        code = "D"
    else:
        code = "F"

    return code


print("Codigo de nota: ", CalculateGrade(9.9))
