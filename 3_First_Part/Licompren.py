# list double comprehension

nums=[1,2,3,4]
doubled= [x*2 for x in nums]
print("Doubled List:", doubled)


# uppercase comprehension
letters = ['a', 'b', 'c', 'd']
upper=[ch.upper() for ch in letters]
print("Uppercase List:", upper)


# even number comprehension
nums=[1,2,3,4,5 ,6 ,7]
evens=[x for x in nums if x % 2 ==0]
print("Even Numbers List even", evens)


# odd numbers comperehension
nums=[1,2,3,4,5 ,6 ,7,8]
odds=[x for x in nums if x %2 ==1]
print("Even Numbers List odds", odds)