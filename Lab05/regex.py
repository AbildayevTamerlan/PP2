import re

text_to_match = """\
John's email is john.doe@example.com, and his backup is johndoe123@work.net.  
Call him at +1-555-123-4567 or his office line (555) 765-4321.  
His website is https://www.johndoe.dev, and his IP address is 192.168.0.1.  
The price of the item is $19.99, but with a discount, it's now $14.99.  
Today's date is 17/02/2025, and another format is 2025-02-17.  
Here's some HTML: <div class="container">Hello, World!</div>  
Watch out for special characters like !@#$%^&*()_+={}[]|:;"'<>,.?/
abbb

NewLineOfText

A regular expression (or RE) specifies a set of strings that matches it; 
the functions in this module let you check if a particular string matches a given regular expression (or if a given regular expression matches a particular string, which comes down to the same thing). 
Regular expressions can be concatenated to form new regular expressions; 
if A and B are both regular expressions, then AB is also a regular expression. 
In general, if a string p matches A and another string q matches B, the string pq will match AB. 
This holds unless A or B contain low precedence operations; boundary conditions between A and B; 
or have numbered group references. 
Thus, complex expressions can easily be constructed from simpler primitive expressions like the ones described here. 
For details of the theory and implementation of regular expressions, consult the Friedl book [Frie09], or almost any textbook about compiler construction. 
A brief explanation of the format of regular expressions follows. 
For further information and a gentler presentation, consult the Regular Expression HOWTO. 
Regular expressions can contain both special and ordinary characters. 
Most ordinary characters, like 'A', 'a', or '0', are the simplest regular expressions; 
they simply match themselves. You can concatenate ordinary characters, so last matches the string 'last'. 
(In the rest of this section, we'll write RE's in this special style, usually without quotes, and strings to be matched 'in single quotes'.)
some_text
"""

# Task 1
pattern = r"ab*"

result = re.findall(pattern, text_to_match)

print(result, "\n")


# Task 2
pattern = r"ab{2,3}"

result = re.findall(pattern, text_to_match)

print(result, "\n")


# Task 3
pattern = r"\b[a-z]+_[a-z]+\b"

result = re.findall(pattern, text_to_match)

print(result, "\n")


# Task 4
pattern = r"[A-Z][a-z]+"

result = re.findall(pattern, text_to_match)

print(result, "\n")


# Task 5
pattern = r"a.+?b"

result = re.findall(pattern, text_to_match)

print(result, "\n")


# Task 6
pattern = r"[\s,\.]"

result = re.sub(pattern, ':', text_to_match)

print(result, "\n")


# Task 7
pattern = r"_(\w)"

def to_camel_case(match):
   return match.group(1).upper()

result = re.sub(pattern, to_camel_case, text_to_match)

print(result)


# Task 8
pattern = r"[A-Z]"

result = re.split(pattern, text_to_match)

print(result, "\n")


# Task 9
pattern = r"([a-z])([A-Z])"

result = re.sub(pattern, r"\1 \2", text_to_match)

print(result)


# Task 10
pattern = r"([a-z])([A-Z])"

def to_snake_case(match):
   return f"{match.group(1)}_{match.group(2).lower()}"

result = re.sub(pattern, to_snake_case, text_to_match)

print(result)