alpha = input()
dial = [
    ['A', 'B', 'C'],      
    ['D', 'E', 'F'],      
    ['G', 'H', 'I'],      
    ['J', 'K', 'L'],      
    ['M', 'N', 'O'],      
    ['P', 'Q', 'R', 'S'], 
    ['T', 'U', 'V'],      
    ['W', 'X', 'Y', 'Z']  
]

total = 0

for ch in alpha:
    for i in range(len(dial)):
        if ch in dial[i]:
            total += i + 3  
            break

print(total)
