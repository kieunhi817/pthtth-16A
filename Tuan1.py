import re
def positive_negative_sum(str1):
    positive_values = sum(int(n) for n in re.findall('\d+', str1))
    negative_values = sum(int(n) for n in re.findall('-\d+', str1))
    return positive_values, negative_values

str1 = '-100#^sdfkj8902w3ir021@swf-20'
print("Original string:")
print(str1)
print("\nSum of all positive, negative integers present in the said string:")
result = positive_negative_sum(str1)
print("Positive values:",result[0])
print("Negative values:",result[1])
