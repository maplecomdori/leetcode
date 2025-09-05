"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total = 0

        id_to_employee = dict()
        for emp in employees:
            id_to_employee[emp.id] = emp

        queue = deque() # [ id ]
        queue.append(id)

        while queue:
            emp_id = queue.popleft()

            employee = id_to_employee[emp_id]
            total += employee.importance

            for sub_id in employee.subordinates:
                queue.append(sub_id)

        return total