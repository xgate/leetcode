class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len(list(filter(lambda x: x in jewels, stones)))
