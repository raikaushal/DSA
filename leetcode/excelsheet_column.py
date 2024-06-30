
from tokenize import Number


# DP
def convertToExcel(number, col=""):
    if number <= 26:
        col += chr(number+64)
        return col

    res = number//26
    col += chr(res+64)
    return convertToExcel(number % 26, col)


print(convertToExcel(702))


# def convertToTitle(columnNumber):
#     number = columnNumber
#     res = ""
#     while columnNumber:
