from uuid import UUID, uuid4

class StackUnderflow(Exception):
    pass

class Stack:
    def __init__(self, id=None):
        self._id = id or uuid4()
        self._size = 0
        self._items = {}

    @property
    def id(self):
        return self._id

    def is_empty(self):
        '''
        newStack_isEmpty
        >>> s = Stack()
        >>> assert s.is_empty()
        '''
        return self._size == 0

    def push(self, item: UUID):
        '''
        afterOnePush_isNotEmpty
        >>> from uuid import uuid4
        >>> s = Stack()
        >>> s.push(uuid4())
        >>> assert not s.is_empty()
        '''
        self._items[self._size] = item
        self._size += 1

    def pop(self) -> UUID:
        '''
        willThrowUnderflow_whenEmptyStackIsPopped
        >>> s = Stack()
        >>> try:
        ...     s.pop()
        ... except StackUnderflow:
        ...     pass
        ... else:
        ...     assert False, 'StackUnderflow expected'

        afterOnePushAndOnePop_willBeEmpty
        >>> from uuid import uuid4
        >>> s = Stack()
        >>> s.push(uuid4())
        >>> s.pop()
        >>> assert s.is_empty()

        afterTwoPushesAndOnePop_willNotBeEmpty
        >>> from uuid import uuid4
        >>> s = Stack()
        >>> s.push(uuid4())
        >>> s.push(uuid4())
        >>> s.pop()
        >>> assert not s.is_empty()

        afterPushingX_willPopX
        >>> from uuid import uuid4
        >>> s = Stack()
        >>> x = uuid4()
        >>> s.push(x)
        >>> assert s.pop() == x
        >>> y = uuid4()
        >>> s.push(y)
        >>> assert s.pop() == y

        aftetrPushingXAndY_willPopYThenX
        >>> from uuid import uuid4
        >>> x, y = uuid4(), uuid4()
        >>> s = Stack()
        >>> s.push(x)
        >>> s.push(y)
        >>> assert s.pop() == y
        >>> assert s.pop() == x
        '''
        if self.is_empty():
            raise StackUnderflow()
        self._size -= 1
        result = self._items[self._size]
        return result
