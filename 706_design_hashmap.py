class MyHashMap:

    def __init__(self):
        self.table = [None] * 1001

    def put(self, key: int, value: int) -> None:
        table_number = key // 1000
        if not self.table[table_number]:
            self.table[table_number] = [-1] * 1000
        idx = key % 1000
        self.table[table_number][idx] = value

    def get(self, key: int) -> int:
        table_number = key // 1000
        if not self.table[table_number]:
            return -1
        idx = key % 1000
        return self.table[table_number][idx]

    def remove(self, key: int) -> None:
        table_number = key // 1000
        if not self.table[table_number]:
            return
        idx = key % 1000
        self.table[table_number][idx] = -1
