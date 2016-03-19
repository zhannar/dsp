
# Option 1 - Direct
print math.cos(math.pi)
print math.cos(math.pi)


# Option 2 - Via a function
def print_twice(something):
    print something
    print something

print_twice(math.cos(math.pi))
-1.0
-1.0


# While Loops

## Stop Condition Expressed "NEGATIVELY"
## "Keep going until X Happens"

while n > 0: # <-- Stopping Condition Checked
    # (Many additional steps can happen here)
    # ...
    print n
    n = n - 1 #Increments to stopping condition

## Stop Condition Expressed "POSITIVELY"
## "STOP when X Happens"

while True:
    # (Many additional steps can happen here)
    # ...
    if n <= 0:
        break   # <-- Stopping Condition Checked
    else:
        n = n - 1 #Increments to stopping condition
