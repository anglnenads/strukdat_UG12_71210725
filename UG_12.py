class Node:
    def __init__(self, data):
        self._data = data
        self._children = []
        # self._parent = parent
 
    #menambahkan child
    def addChild(self, data):
        self._children.append(data)
 
    #mendapatkan isi elemen
    def operator(self):
        return self._data
 
    #mendapatkan node parent
    def parent(self):
        return self._parent
 
    #mendapatkan node children
    def children(self):
        return self._children
 
    #mengecek apakah node merupakan root
    def isRoot(self):
        return self._parent is None
 
    #mengecek apakah node merupakan external/leaf
    def isExternal(self):
        return len(self._children) == 0

class Tree:
    def __init__(self, data, parent = None):
        self._data = data
        self._children = []
        self._parent = parent

    #menambahkan child
    def addChild(self,parent, data):
        self._parent = parent
        self._children.append(data)

def minus(node):
        # total = node._data
    for i in node._children():
        total =- node._children()
    print(node.operator(), end = ' ')

def sibling(node):
    total += 0
    for i in node.parent().children():
        total += 1

# def postorder(node):
#     for i in node.children():
#         postorder(i)
#     print(node.operator(), end = ' ')

# child daftar ke parent
# root = Tree(300, None)
# a = Tree(9, root)
# b = Tree(1, root)
# c = Tree(11, root)
# d = Tree(99, root)
# e = Tree(28, c)
# f = Tree(72, c)
# g = Tree(90, d)
# h = Tree(33, d)
# i = Tree(17, root)
# j = Tree(2, i)
# k = Tree(4, i)
# l = Tree(43, i)

# # parent daftarin childnya
# a.addChild(c)
# a.addChild(d)
# c.addChild(e)
# c.addChild(f)
# d.addChild(g)
# d.addChild(h)
# b.addChild(i)
# i.addChild(j)
# i.addChild(k)
# i.addChild(l)
# root.addChild(a)
# root.addChild(b)

#untuk mengecek urutan
# print("=== Postorder ===")
# postorder(root)

if __name__ =='__main__':
    val300 = Node(300)
    t = Tree(val300) #Level 0
 
    #Level 1 parent 120
    val9 = t.addChild(val300, 9) 
    val1 = t.addChild(val300, 1)
 
    #Level 2 parent 9
    val11 = t.addChild(val9, 11) 
    val99 = t.addChild(val9, 99) 
 
    #Level 2 parent 1
    val17 = t.addChild(val1, 17) 
 
    #Level 3 parent 11
    val28 = t.addChild(val11, 28) 
    val72 = t.addChild(val11, 72)
 
    #Level 3 parent 99
    val90 = t.addChild(val99, 90) 
    val33 = t.addChild(val99, 33)
 
    #Level 3 parent 17
    val17 = t.addChild(val17, 2)
    val17 = t.addChild(val17, 4)
    val17 = t.addChild(val17, 43)

def postorder(node):
    for i in node.children():
        postorder(i)
    print(node.operator(), end = ' ')

postorder(Node)
 
# No 2. #
print(f'Sisa hasil pengurangan dari node {val300._data} adalah {t.minus(val300)}')
 
# No 3. #
print(f'Total nilai dari semua saudara pada node {val90._data} adalah {t.sibling(val90)}')

