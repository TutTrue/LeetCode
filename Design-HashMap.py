class MyHashMap:

    def __init__(self):
        self.hash = [0] * 8
        self.count = 0

    def put(self, key: int, value: int) -> None:
        if self.count >= len(self.hash) * 0.7:
            self.rebalance()
        capacity = len(self.hash)
        index = key % capacity
        first_available = -1
        found = False
        for j in range(capacity):
            current_i = (index + j) % capacity
            entry = self.hash[current_i]
            if entry == 0:
                if first_available == -1:
                    first_available = current_i
                break
            elif entry[2] == 1:
                if first_available == -1:
                    first_available = current_i
            else:
                if entry[0] == key:
                    self.hash[current_i] = (key, value, 0)
                    found = True
                    break
        if not found and first_available != -1:
            self.hash[first_available] = (key, value, 0)
            self.count += 1

    def get(self, key: int) -> int:
        capacity = len(self.hash)
        index = key % capacity
        for j in range(capacity):
            current_i = (index + j) % capacity
            entry = self.hash[current_i]
            if entry == 0:
                return -1
            elif entry[2] == 1:
                continue
            elif entry[0] == key:
                return entry[1]
        return -1

    def remove(self, key: int) -> None:
        capacity = len(self.hash)
        index = key % capacity
        for j in range(capacity):
            current_i = (index + j) % capacity
            entry = self.hash[current_i]
            if entry == 0:
                return
            elif entry[2] == 1:
                continue
            elif entry[0] == key:
                self.hash[current_i] = (entry[0], entry[1], 1)
                self.count -= 1
                return

    def rebalance(self):
        old_hash = self.hash
        old_capacity = len(old_hash)
        new_capacity = old_capacity * 2
        self.hash = [0] * new_capacity
        self.count = 0

        for entry in old_hash:
            if entry != 0 and entry[2] == 0:
                key, value, _ = entry
                self.put(key, value)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)