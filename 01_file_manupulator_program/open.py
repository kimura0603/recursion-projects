file = open('test.txt')
contents = file.read()
file.close()

file = open('test.txt', 'w')
file.write(contents + "\nAppending more text to this file!")
file.close()