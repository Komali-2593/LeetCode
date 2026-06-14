class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        result=[]
        deck.sort()
        while deck:
            if result:
                last=result.pop()
                result.insert(0,last)
            result.insert(0,deck.pop())
        return result


        