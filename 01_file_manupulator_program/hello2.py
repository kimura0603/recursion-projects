import sys
sys.stdout.buffer.write(b'What is your favorite food?\n')
sys.stdout.flush()
food = sys.stdin.buffer.readline()
print("your favorite food is " + food.decode())
