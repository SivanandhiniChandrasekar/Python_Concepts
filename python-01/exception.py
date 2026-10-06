# # try, except, finally
try:
    arr = [89,78,653,93]
    print("There are 6 elements in this array and the sixth element is ", arr[5])
except NameError as e:
    print("NameError",e)
except ValueError:
    print("ValueError")
except IndexError:
    print("IndexError")
except Exception as e:
    print(e)
finally:
    print("This will always run")

# ZeroDivisionError
# TypeError
a, b, c = '+', '-', '/', '*', '%'
testcase:1
12
0
testcase:2
2
"oko"
