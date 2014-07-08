#Author : SATEJ V. KHANDEPARKAR
# MASTERS IN EMBEDDED AND INTELLIGENT SYSTEMS 
# HALMSTAD UNIVERSITY


print "***************************************************\n"
print "THE CENSOR PROGRAM\n"

text = raw_input("Enter the sentence: \n")
word = raw_input("Enter the word you want to censor: \n")
def censor(text,word):
	store = []
	asterix = []
	crypt =[] 
	store = text.split()
	
	for i in store:
 	 if (i == word):
 	  #print i
 	  asterix = list(i)
 	  #print asterix,
 	  
 	  crypt.append("*" * len(asterix))
 	  #print crypt   
 	 
         else:
          crypt.append(i)
          #print crypt
      	print " ".join(crypt)     
            
censor (text,word)
print "*****************\n" 
           
