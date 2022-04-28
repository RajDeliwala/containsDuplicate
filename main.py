#Using an hashset, we need to check before adding it if the index
#already exists, if it does return True
from genericpath import exists
from typing import Hashable

def containsDuplicate(self, nums):
        Hashable = set()
        for n in nums:
            if n in Hashable:
                return True
            else:
                Hashable.add(n)
        return False



commonlist = [1,2,3,4,1]
print(containsDuplicate(commonlist))

