def function(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*function(n-1)
print(function(3))
print(function(4))
print(function(5))