try:
    print(1 / 0)
except ZeroDivisionError as e:
    print("It's a Zero Division error")
except Exception as e:
    print(f"The error thrown is : {e}")
else:
    print("This will run only if except is not running")
finally:
    print("Run always")
