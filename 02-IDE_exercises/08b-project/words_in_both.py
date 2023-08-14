def words_in_both(str1: str, str2: str) -> set:
   """
   Takes two strings and returns a set of all common words (regardless of case) in lowercase."""
   set1 = set(str1.lower().split())
   set2 = set(str2.lower().split())
   return set1 & set2