# def first_non_repeating_letter(string):
#     letter = ''
#     contain = []
#     for i in string:
#         if i in contain:
#             contain.pop(contain.index(i))
#         contain.append(i)
#     letter += contain[0]
#     return letter
# print(first_non_repeating_letter('sTreSs'))



# inbs = '1 1 1 2 2 2 3 3 3 9 x'
# def isbn_validation(arr):
#     arr.split()
#     if len(arr) != 10:
#         return False
#     fin = 0
#     for c, v in enumerate(arr, start=1):
#         fin += c*int(v)
#     if arr[9].lowercase() == 'x':
#         fin += 10*10
#     return True if fin % 11 == 0 else False
# print(isbn_validation(inbs))



# from string import ascii_letters
# def alphanumetric(string):
#     return len([s for s in string if s not in acsii_letters]) == 0
# print(alphanumetric('ajafga'))




# arr1 = [10, 20, 10, 2]
# arr2 = [10, 25, 5, -2]
# def Mean_Square_Error(arr1, arr2):
#     return sum([(e1 - e2)** 2 for e1, e2 in zip(arr1, arr2)]) / len(arr1)
# print(Mean_Square_Error(arr1, arr2))



# val = "#FF9933"
# def hex_to_rgb(hex):
#     hex = hex.lstrip('#')
#     return set(int(hex[i:i+2], 16) for i in (0, 2, 4))
# print(hex_to_rgb(val))



# hashtag = '   Hello          world'
# def has(tag):
#     res = '#'
#     for i in tag.split():
#         res += i.capitalize()
#     return res
# print(has(hashtag))



# fw = 'abba'
# sw = ['aabb', 'bbaa', 'abcd', 'dada']
# def anagram(word, words):
#     emp = []
#     for i in words:
#         if sorted(i) == sorted(word):
#             emp.append(i)
#     return emp
# print(anagram(fw, sw))


# def increment_string(strng):
#     head = strng.rstrip('0123456789')
#     tail = strng[len(head):]
#     print(tail)
#     if tail == "": return strng+"1"
#     return head + str(int(tail) + 1).zfill(len(tail))



# smth = 'Hello World !'
# def pig_it(text):
#     fin = ''
#     for i in text.split():
#         if i.isalpha():
#             fin += i[1:]+i[0]+"ay"+' '
#         else:
#             fin += i
#     return fin
# print(pig_it(smth))


# str1 = 'cedewaraaossoqqyt'
# str2 = 'codewars'
# def scramblies(str1, str2):
#     return all([s in str1 for s in str2])
# print(scramblies(str1, str2))
