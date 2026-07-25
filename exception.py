while True:
    try:

     a = int(input("enter number 1:"))
     b = int(input("enter number 2:"))
     print(f"the division is {a/b} ")
    except ValueError:
       print( "don't perform bad typecasts" )
    except ZeroDivisionError:
       print("dont divide by zero")
    except Exception as e:
       print("unknown error occure")