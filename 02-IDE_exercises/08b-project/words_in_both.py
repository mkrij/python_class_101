def words_in_both(str1: str, str2: str) -> set:
   set1 = set(str1.lower().split())
   set2 = set(str2.lower().split())
   return set1 & set2
print(words_in_both("She's a jack of all trades", 'Jack was tallest of all'))