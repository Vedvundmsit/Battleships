def contains(s1, s2): 
    for i in range(len(s1)): 
        if s1[i:i+len(s2)] == s2:
            return True 
    return False 

print(contains("Hello world", "world"))