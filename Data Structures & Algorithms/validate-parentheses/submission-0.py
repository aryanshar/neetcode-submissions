class Stack:
    def __init__(self):
        self.arr = []
    
    def push(self, x) -> None:
        self.arr.append(x)

    def pop(self) -> Optional[Any]:
        if not self.is_empty():
            return self.arr.pop()
        return None
    
    def peek(self) -> Optional[Any]: 
        if not self.is_empty():
            return self.arr[-1]
        return None

    def is_empty(self) -> bool:
        return len(self.arr) == 0
    
    def size(self) -> int:
        return len(self.arr)


class Solution:
    
    def isValid(self, s: str) -> bool:
        key_store = {"]":"[", "}":"{", ")": "("}
        check_valid = Stack()
        for ch in s:
            # if check_valid is empty -> push to stack
            # if check_valid.peek() == reverse of ch -> just pop
            # else
            if ch in key_store.keys() and check_valid.peek() == key_store[ch]:
                check_valid.pop()
            else:
                check_valid.push(ch)

        

        return check_valid.size() == 0



        