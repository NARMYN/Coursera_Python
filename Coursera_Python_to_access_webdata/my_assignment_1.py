from bs4 import BeautifulSoup
#import re
#fhand = open('Coursera_Python_to_access_webdata/regex_sum_1487139.txt')
#my_file = fhand.read()
#my_list = re.findall('[0-9]+', my_file)
#for val in range(0, len(my_list)):
#    my_list[val]= int(my_list[val])
#my_sum = sum(my_list, 0)
#print(my_sum)

#the code above is without list comprehension while the code below is with list comprehension
import re
print( sum( [ int(re.findall('[0-9]+',open('Coursera_Python_to_access_webdata/regex_sum_1487139.txt').read())[val]) for val in range(0, len(re.findall('[0-9]+',open('Coursera_Python_to_access_webdata/regex_sum_1487139.txt').read()))) ] ) )