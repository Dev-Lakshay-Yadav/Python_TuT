file = open('basics/test.py', 'w')


try:
    file.write("print('hello world')")
finally:
    file.close()

    