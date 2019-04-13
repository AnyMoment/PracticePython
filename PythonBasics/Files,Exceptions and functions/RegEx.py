"""
......................Regular Expressions.....................
..........................match method.................

////////////////////////////////////////
what is the importance of * and **
////////////////////////////////////////


import re
#print(dir(re))
Line="Pet:cat I like pets"
Mat=re.match(r"Pet:\w\w\w",Line)
print(Mat)
Mat=re.match(r"Pet:\w\w\w",Line)
print(Mat.group(0))
Mat=re.match(r"Pet:\w\w",Line)
print(Mat.group(0))
print(Mat.start())
print(Mat.end())


//////////////////////////////////////
But if the pattern is I like pets Pet:cat
It throws an error because the match method is only for the start of string. 
/////////////////////////////////////



..............................Search method...................


#re.search(pattern,string)
import re
Line="I like Pets Pet:cat"
Mat=re.search(r"Pet:\w\w\w",Line)
print(Mat.group(0))

#............................ProgramWithError

import re
Line="Pet:Cow I like Pets Pet:cat"
Mat=re.search(r"Pet:\w\w\w",Line)
print(Mat.group(0))
print(Mat.group(1)) # No Such group 

///////////////////////////////////////
This is because the method only checks for first occurence of the pattern. 
//////////////////////////////////////

#.........................EndError


.................................Findall Method...................


import re
Line="Pet:Cat I like Pets Pet:Cow I Like cows"
Mat=re.findall(r"Pet:\w\w\w",Line)
print(Mat)

....................................Split.......................

import re
Line="Pet:Cat I like Pets Pet:Cow I Like cows Pet:Cow"
Mat=re.split(r"Pet:\w\w\w",Line)
print(Mat)


////////////////////////////////////////////
If the mathc occurs at start or End of string, then
an empty item is inserted in the list automatically
///////////////////////////////////////////


..................................Sub..........................


import re
Emails="google@inst.com,institute@gail.com,holly@yahoo.com"
pattern=re.sub(r"@w\+","@gmail",Emails)
print(pattern)
"""