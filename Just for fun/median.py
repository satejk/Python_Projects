
#Author : SATEJ V. KHANDEPARKAR
# MASTERS IN EMBEDDED AND INTELLIGENT SYSTEMS
# HALMSTAD UNIVERSITY, sweden.

# This program finds the median of the input array.


def median(seq):
    sort_seq = sorted(seq)
    
    length = len(sort_seq)
    print length
    x = 0
    if (length % 2 == 0):
        med = ((sort_seq[(length/2)]) + (sort_seq[(length/2) - 1 ] ))/ 2.0
        
    else:
        med = sort_seq [length / 2]
        
    print med   
    
    
seq = [7,3,1,4] # change the input to test the program.

median(seq)    
    
    
