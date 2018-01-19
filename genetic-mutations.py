# Problem statement: https://leetcode.com/problems/minimum-genetic-mutation/description/


import collections

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        queue = collections.deque()
        queue.append([start, start, 0])
        while queue:
            current, previous, num_steps = queue.popleft()
            if current == end:
                return num_steps
            for string in bank:
                if validMutation(current, string) and string != previous:
                    queue.append([string, current, num_steps+1])
        return -1

def validMutation(curMutation, nextMutation):
    changes = 0
    for i in xrange(len(curMutation)):
        if curMutation[i] != nextMutation[i]:
            changes += 1
    return changes == 1
