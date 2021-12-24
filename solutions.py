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






# binary.py
# '''
# linear    |  binary
# 100 = 100 |  100 == 4
# 4 bil = 4 |  32
# '''
# l = [1, 2, 3, 4, 5, 6, 7]
# left = 0
# right = 6
# mid = 3
# x = 5
# l[mid] == x
# l[mid] > x
# l[mid] < x
# def binary_search(arr, item):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         guess = arr[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             right = mid - 1
#         else:
#             left = mid +1
#     return None
# x = int(input('Enter a number: '))
# if (binary_search([1,2,3,4,5,6,7], x)):
#     print ('Number found')
# else:
#     print('Not found')





# def buble_sort(arr):
#     n=len(arr)
#     for i in range (n-1):
#         for j in range (n-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
# l=[0, 8, 56, 62, 7, 2, 34, 8]
# print(l)
# print(buble_sort(l))
