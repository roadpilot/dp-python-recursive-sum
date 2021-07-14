# given a list of non-negative integers representing the value of each element, determine the maximum sum of individual elements.  you cannot add adjacent elements. 

houses1 = [100,2,3,100] # => 200
houses2 = [2,7,9,3,1] # => 12

# RECURSIVE APPROACH
def rob(houses):
  return rob_rec(houses, len(houses)-1)

def rob_rec(houses, i):
  if (i<0):
    return 0
  current_house = houses[i] + rob_rec(houses, i-2)
  adjacent_house = rob_rec(houses, i-1)
  print ("CURRENT HOUSE:", current_house, "ADJACENT HOUSE:", adjacent_house)
  return max(current_house, adjacent_house)

# MEMOIZED APPROACH
def memo_rob(houses):
  memo = len(houses) * [float('-inf')]
  return memo_rob_rec(houses, len(houses)-1, memo)

def memo_rob_rec(houses, i, memo):
  if (i<0):
    return 0
  if memo[i] != float('-inf'):
    return memo[i]
  current_house = houses[i] + memo_rob_rec(houses, i-2, memo)
  adjacent_house = memo_rob_rec(houses, i-1, memo)
  print (i,"CURRENT HOUSE:", current_house, "ADJACENT HOUSE:", adjacent_house)
  calc = max(current_house, adjacent_house)
  memo[i] = calc
  return calc

print(rob(houses1)) 
print(memo_rob(houses1)) 