'''
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.
'''

# 나중에 방문할 곳을 스택에 먼저 쌓아서 순서를 정한 후 계산 진행

# 스택, 팝 사용
# 링크드 리스트 먼저 공부해보기

# 노드 추가 삭제 부분은 심화 부분

RootNode = None

class Node:
    def __init__(self, parents, left_child, right_child):
        self.data = parents
        self.left = left_child
        self.right = right_child
    
# 노드추가
def add():
    if self.root = None:
        self.root = N


'''class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:

'''
    