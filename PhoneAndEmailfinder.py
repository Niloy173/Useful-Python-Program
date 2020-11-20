import pyperclip,re

# creating regex format for phone number
# sample - 183-555-1212 and ni@gmail.com
phoneNumberRegex = re.compile(r'''(
              (\d{3}|\(\d{3}\))? #area code
              (\s|-|\.|:|)?          #seperator
              (\d{3})
              (\s|-|\.)
              (\d{4})
             #(\s*(ext.|ex|x)\s*\d{2,5})? extention
             
             # for bd mobile number - regex expression would be (\d{11})

)''',re.VERBOSE)

EmailaddressRegex = re.compile(r'''(


       [a-zA-Z0-9._+%-]+   #username
       @
       [a-zA-Z0-9.-]+  # domain name
       (\.[a-zA-z]{2,4}) #dot.name



)''',re.VERBOSE)

text= str(pyperclip.paste())

matcher = []

for groups in EmailaddressRegex.findall(text):
    matcher.append(groups[0])


for groups in phoneNumberRegex.findall(text):
    phoneNum = ':'.join([groups[1],groups[3],groups[5]])
    """if groups[6]!='':
        phoneNum+='X'+groups[6]"""
    matcher.append(phoneNum)




if (len(matcher)) > 0:
    pyperclip.copy('\n'.join(matcher))
    print('copied to clipboard')
    print('\n'.join(matcher))
else:
    print("no email or phone found")

