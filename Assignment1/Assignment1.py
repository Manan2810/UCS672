import nltk
from nltk.tokenize import word_tokenize

# Q1
s1="Hi there class!"
tokens = list(word_tokenize(s1.lower()))
print(tokens)

#Q2
planet = "Earth"
diameter = 12742
sentence = "The diameter of {} is {} kilometers.".format(planet, diameter)
print(sentence)

#Q3
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])

#Q4
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
target_value = d['k1'][3]['tricky'][3]['target'][3]
print(target_value)

#Q5
def extract_domain(email):
    try:
        # Split the email address at the '@' symbol
        _, domain_part = email.split('@')
        
        # Split the domain part at the '.' symbol
        domain = domain_part.split('.')[0]
        
        return domain
    except ValueError:
        # Handle the case where the email format is incorrect
        return None

# Example usage:
email_address = input("enter email address :-")
domain = extract_domain(email_address)

if domain:
    print(f"The domain of the email '{email_address}' is '{domain}'.")
else:
    print(f"The email address '{email_address}' is not in the expected format.")
    
    
#Q6
def WordContained(word):
    sentence="manan has a pet dog ."
    found = 0
    l1 = list(word_tokenize(sentence.lower()))
    for i in l1:
        if i == word:
            found = 1
    
    if found == 1:
        return True
    else :
        return False
    
ans=WordContained("dog")
if ans == True:
    print("found")
else:
    print("not found")
    
#Q7
def countWordOccured(word):
    sentence = "The dog barked loudly attracting the attention of everyone nearby A small dog brown in color chased its tail in excitement . A friendly dog approached, wagging its tail happily. The children gathered around, eager to pet the dog . Meanwhile, another dog , a black Labrador, strolled casually along the path. The sound of footsteps echoed as the dog padded across the pavement . Overall, it was a day filled with the joyful presence of man's best friend the dog ."
    count = 0
    l1 = list(word_tokenize(sentence.lower()))
    for i in l1:
        if i == word:
            count = count+1
    
    return count

ans2=countWordOccured("dog")
print(ans2)

#Q8
words =  ['soup','dog','salad','cat','great']

# Using filter with a lambda function
filtered_words = list(filter(lambda word: word.startswith('s'), words))

print("Original words:", words)
print("Filtered words (starting with 's'):", filtered_words)


#Q9
def caughtSpeed(speed,birthday):
    if birthday == True:
        speed=speed-5
        if speed <= 60:
            print("no challan")
        elif speed>61 and speed<=80:
            print("small chalan")
        else:
            print("heavy chalan")
    else:
        if speed <= 60:
            print("no challan")
        elif speed>61 and speed<=80:
            print("small chalan")
        else:
            print("heavy chalan")

caughtSpeed(81,True)

#Q10
list1 = ["M", "na", "i", "She"] 
list2 = ["y", "me", "s", "lly"]
list3 = []

for i in range(0,len(list1)):
    list3.append(list1[i] + list2[i])
print(list3)

#Q11
list11 = ["Hello ", "take "]
list21 = ["Dear", "Sir"]
output=[]

for i in range(len(list11)):
    for j in range(len(list21)):
        output.append(list11[i]+list21[j])
print(output)

#Q12
list10 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list10[2][2].append(7000)
print(list10)

#Q13
list13 = [5, 20, 15, 20, 25, 50, 20]
list14=[]
for i in range(len(list13)):
    if list13[i]!=20:
        list14.append(list13[i])
print(list14)

#Q14
d11 = {'a': 100, 'b': 200, 'c': 300}
listofvalues = list(d11.values())
found = 0
for i in listofvalues:
    if i == 200:
        found =1
if found ==1:
    print("value found")
else:
    print("value not found")
    

#Q15
def generate_series(n):
    series = [int('2' * i) for i in range(1, n + 1)]
    return series

def sum_of_series(series):
    return sum(series)

n_terms = 5  # You can change this value to the desired number of terms
series = generate_series(n_terms)
total_sum = sum_of_series(series)

print(f"The series is: {series}")
print(f"The sum of the series is: {total_sum}")