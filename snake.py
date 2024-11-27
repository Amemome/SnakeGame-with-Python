import obj,queue

class Snake(obj.GameObject):
    """플레이어가 조작할 수 있는 뱀 클래스"""

    def __init__(self, x, y,color):
        super().__init__(x, y, color)
        self.head = (24,18) # 중간 지점에 머리를 둠.
        self.body = queue() # 몸통은 덱으로 관리.

