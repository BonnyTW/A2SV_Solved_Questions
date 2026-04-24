class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count = Counter(moves)
        if count['L'] >= count['R']:
            return count['L'] - count['R'] + count['_'] 
        else:
            return -count['L'] + count['R'] + count['_']