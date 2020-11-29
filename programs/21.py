# FooBar.

numb = int(input("Enter the numb: "))

for item in range(1, numb):
    if item % 2 == 0:
        continue
    if item % 3 == 0 and item % 5 == 0:
        print("FooBar")
    elif item % 3 == 0:
        print("Foo")
    elif item % 5 == 0:
        print("Bar")
    else:
        print(item)

# Enter the numb: 20
# 1
# Foo
# Bar
# 7
# Foo
# 11
# 13
# FooBar
# 17
# 19