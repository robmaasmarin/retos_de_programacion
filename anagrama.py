def miAnagrama(first, second):
    firstlower = first.lower()
    secondlower = second.lower()
    x = sorted(list(firstlower))
    y = sorted(list(secondlower))
    if x == y:
        return True
    else:
        return False
    

        
print(miAnagrama("cara", "arca"))
print(miAnagrama("cara", "arc"))
print(miAnagrama("castor", "castro"))
print(miAnagrama("Castor", "castro"))