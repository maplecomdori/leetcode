class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:
        total = 0

        unopened = set([box for box in initialBoxes if status[box] == 0])

        queue = deque([box for box in initialBoxes if status[box] == 1])

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()

                total += candies[curr]

                for nei in containedBoxes[curr]:
                    if status[nei] == 1:
                        queue.append(nei)
                    else:
                        unopened.add(nei)

                for key in keys[curr]:
                    status[key] = 1

                    if key in unopened:
                        unopened.remove(key)
                        queue.append(key)

        return total


"""
status: 1 = open, 0 is closed

Example 1
status = [1,0,1,0], 
candies = [7,5,4,100], 
keys = [[],[],[1],[]], 
containedBoxes = [[1,2],[3],[],[]], 
initialBoxes = [0]

box0(open) => 7 candy, box1(closed), box2(open)
    box1(closed) => no key
    box2(open) => 4 candy, key1
    box1(found key) => 5candy, no key, box3 
    box3(no new key found, no new box found, finished)

Example 2
status = [1,0,0,0,0,0], 
candies = [1,1,1,1,1,1], 
keys = [[1,2,3,4,5],[],[],[],[],[]], 
containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], 
initialBoxes = [0]

box0(open) => 1 candy, key1, key2, key3, key4, key5, box1, box2, box3, bo4, box5


found box X but no key X => no candy
found key X but no box X => no candy
found key X and box X => add candy
"""