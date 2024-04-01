def canConstruct(ransomNote, magazine):
    magazine_count = {}
    for letter in magazine:
        if letter not in magazine_count:
            magazine_count[letter] = 1
        else:
            magazine_count[letter] +=1
    for letter in ransomNote:
        if letter not in magazine_count or magazine_count[letter]== 0: # if letter not in magazine_count or if there is no such letter in magazine_count
            return False
        else:
            magazine_count[letter] -=1 #-1 because we already took this letter
  
    return True