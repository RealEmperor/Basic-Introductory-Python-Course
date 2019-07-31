
# 容器

## list 列表

序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。

列表的数据项不需要具有相同的类型

## tuple 元组（只读列表）

## dict 字典

字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中。

## set 集合

是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算。

# list/tuple基本操作

创建

添加元素（list only）：append, extend

删除元素（list only）：del, pop

根据索引读写（tuple只读）

判断容器是否为空

容器元素数量	

遍历


```python
li = [1, 2, 3, '456', [1, 2, 3], {1: 'one', 2: 'two'}]
print(type(list))
print(type(li))
```

    <class 'type'>
    <class 'list'>
    


```python
# 元素访问
print(li[0])
print(li[-1])  # li[len(li) - 1]
print(li[-2])  # li[len(li) - 2]
```

    1
    {1: 'one', 2: 'two'}
    [1, 2, 3]
    


```python
# 查找元素位置
print(li.index('456'))
print(li.index([1, 2, 3]))
# print(li.index(-1)) # 如果不存在会报错：ValueError: -1 is not in list
```

    3
    4
    


```python
# 遍历
for i in li:
    print(i)
    
for i in range(len(li)):
    print(li[i])
```

    1
    2
    3
    456
    [1, 2, 3]
    {1: 'one', 2: 'two'}
    1
    2
    3
    456
    [1, 2, 3]
    {1: 'one', 2: 'two'}
    


```python
# 删除
del (li[-1])  # del(list[index])
del (li[1])
del (li[-2])
print(li)
```

    [1, 3, [1, 2, 3]]
    


```python
# 添加元素
l_a = [1, 2, 3]
l_a.append(4)
l_a.append(5)
l_b = [6, 7, 8]
l_a.extend(l_b)
print(l_a)
# 对比append的结果
l_a.append(l_b)
print(l_a)
```

    [1, 2, 3, 4, 5, 6, 7, 8]
    [1, 2, 3, 4, 5, 6, 7, 8, [6, 7, 8]]
    


```python
l_a = []
if not l_a:
    print('Empty')  # not XX和is None不是一回事

if len(l_a) == 0:
    print('Empty')
```

    Empty
    Empty
    


```python
t = (1, 2, 3, '456')
print(type(t))
# t[0] = 'a' # 不能被修改，会报错：
# TypeError: 'tuple' object does not support item assignment

# t.append('x') 
# AttributeError: 'tuple' object has no attribute 'append'
```

    <class 'tuple'>
    

# dict基本操作

初始化

访问

添加元素

修改元素	

删除元素

判断key是否存在	

判断容器是否为空

容器元素数量	

遍历


```python
d = {'a': 1, 'b': 2, 1: 'one', 2: 'two', 3: [1, 2, 3]}
print(type(dict))
print(type(d))
print(d)
```

    <class 'type'>
    <class 'dict'>
    {'a': 1, 'b': 2, 1: 'one', 2: 'two', 3: [1, 2, 3]}
    


```python
# 访问元素
print(d['a'])
print(d[1])
print(d[3])
```

    1
    one
    [1, 2, 3]
    


```python
# 判断key是否存在
print('two' in d)
print(3 in d)
```

    False
    True
    


```python
# 删除
del(d[3])   # del(dict[key])
print(len(d))
```

    4
    


```python
# 添加元素
d[3] = [1, 2, 3, 4]
# 修改元素
d[3] = '1234'
```


```python
# 遍历
for key in d:
    print(d[key])
```

    1
    2
    one
    two
    1234
    


```python
for k, v in d.items():
    print(k, v)
```

    a 1
    b 2
    1 one
    2 two
    3 1234
    


```python
keys = d.keys()
print(type(keys))
print(keys)
```

    <class 'dict_keys'>
    dict_keys(['a', 'b', 1, 2, 3])
    

# set基本操作

并/交/差集：|/union, &/intersection, -/difference

对称差集：^/symmetric_difference（不同时出现在2个集合中的项）

包含关系：>=/issuperset

添加元素

更新元素

删除元素

元素是否存在

容器元素数量

遍历


```python
s_a = set([1, 2, 2, 3, 4, 5, 6])
s_b = set([4, 5, 6, 7, 8, 9])
print(s_a)
print(s_b)
```

    {1, 2, 3, 4, 5, 6}
    {4, 5, 6, 7, 8, 9}
    


```python
# 判断元素是否存在
print(5 in s_a)
print(10 in s_b)
```

    True
    False
    


```python
# 并集
print(s_a | s_b)
print(s_a.union(s_b))
```

    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    


```python
# 交集
print(s_a & s_b)
print(s_a.intersection(s_b))
```

    {4, 5, 6}
    {4, 5, 6}
    


```python
# 差集 A - (A & B)
print(s_a - s_b)
print(s_a.difference(s_b))
```

    {1, 2, 3}
    {1, 2, 3}
    


```python
# 对称差 (A | B) - (A & B)
print(s_a ^ s_b)
print(s_a.symmetric_difference(s_b))
```

    {1, 2, 3, 7, 8, 9}
    {1, 2, 3, 7, 8, 9}
    


```python
# 修改元素
s_a.add('x')
s_a.update([4, 5, 60, 70])
print(s_a)
```

    {1, 2, 3, 4, 5, 6, 70, 'x', 60}
    


```python
# 删除元素
s_a.remove(70)
print(s_a)
# s_a.remove(100)
# 如果不存在则报错：KeyError: 100
```

    {1, 2, 3, 4, 5, 6, 'x', 60}
    


```python
print(len(s_a))
# 遍历
for i in s_a:
    print(i)
```

    8
    1
    2
    3
    4
    5
    6
    x
    60
    

# 切片

存取序列（列表，元组，字符串）的任意一部分

格式：seq[开始索引:结束索引:步长]

默认值

负数索引

负数步长


```python
li = list(range(10))
print(li)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    


```python
# 切片 [start:end:steps]  >= start & < end
print(li[2:5])  # [3, 4, 5]
print(li[:4])   # [0, 1, 2, 3]
print(li[5:])   # [6, 7, 8, 9]
print(li[0:20:3])   # [0, 3, 6, 9]
```

    [2, 3, 4]
    [0, 1, 2, 3]
    [5, 6, 7, 8, 9]
    [0, 3, 6, 9]
    


```python
# 负值怎么处理？
print(li[5: -2])    # [5, 6, 7]
print(li[9:0:-1])   # [9, 8, 7, 6, 5, 4, 3, 2,1]
print(li[9::-1])   # [9 ... 0]
print(li[::-2]) # [9, 7, 5, 3, 1]
```

    [5, 6, 7]
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    [9, 7, 5, 3, 1]
    


```python
# 切片生成一个新的对象
print(li)   # 还是保持原样

re_li = li[::-1]
print(re_li)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    

# 列表推导

问题的提出

快速简单的生成一个列表

对原有的列表进行简单的转换

一维列表推导

二维列表推导以及注意事项


```python
li = []
for i in range(20):
    if (i % 2) == 0:
        li.append(i)
print(li)
```

    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    


```python
li = [1] * 10
li[3] = 3
print(li)
li = [i * 2 for i in range(10)]
print(li)
```

    [1, 1, 1, 3, 1, 1, 1, 1, 1, 1]
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    


```python
# 创建数组时浅拷贝的问题
li_2d = [[0] * 3] * 3
print(li_2d)
li_2d[0][0] = 100 # 这里将会修改3个值，因为用这种方式创建二维及以上维度时用的是浅拷贝
print(li_2d)
```

    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    [[100, 0, 0], [100, 0, 0], [100, 0, 0]]
    


```python
# 解决创建数组时浅拷贝的问题
li_2d = [[0] * 3 for i in range(3)]
li_2d[0][0] = 100
print(li_2d)
```

    [[100, 0, 0], [0, 0, 0], [0, 0, 0]]
    


```python
# 创建set
s = {x for x in range(10) if x % 2 == 0}
print(s)

# 创建dict
d = {x: x % 2 == 0 for x in range(10)}
print(d)
```

    {0, 2, 4, 6, 8}
    {0: True, 1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False}
    

# 生成器

问题的提出

创建一个巨大的列表而仅仅需要访问其中少量几个元素

如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。

生成生成器：列表推导时用()替换[]（关于yield的使用后面再讲）

遍历：next或者for循环


```python
print(type(range(10)))
```

    <class 'range'>
    


```python
# 平方表
square_table = []
for i in range(5000):
    square_table.append(i * i)
for i in range(5):
    print(square_table[i])
```

    0
    1
    4
    9
    16
    


```python
square_generator = (x * x for x in range(50000))
print(type(square_generator))
```

    <class 'generator'>
    


```python
for i in range(5):
    print(next(square_generator))
```

    0
    1
    4
    9
    16
    


```python
def fib(limit):
    n, a, b = 0, 0, 1
    while n < limit:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


f = fib(5)
print(type(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
```

    <class 'generator'>
    1
    1
    2
    3
    5
    


```python
import traceback
try:
    print(next(f))
except StopIteration:
    traceback.print_exc()
```

    Traceback (most recent call last):
      File "<ipython-input-40-28968900716f>", line 3, in <module>
        print(next(f))
    StopIteration: done
    


```python
# 遍历
for i in fib(5):
    print(i)
```

    1
    1
    2
    3
    5
    

# 迭代器

问题的提出

可以直接作用于for循环的对象统称为可迭代对象：Iterable

可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator（表示一个惰性计算的序列）

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。


```python
from collections import Iterable
from collections import Iterator

print(isinstance([1, 2, 3], Iterable))
print(isinstance({}, Iterable))
print(isinstance(123, Iterable))
print(isinstance('abc', Iterable))

print(isinstance([1, 2, 3], Iterator))

g = (x * x for x in range(10))
print(type(g))
print(isinstance(g, Iterable))
print(isinstance(g, Iterator))
for i in g:
    print(i)
```

    True
    True
    False
    True
    False
    <class 'generator'>
    True
    True
    0
    1
    4
    9
    16
    25
    36
    49
    64
    81
    


```python
def fib(limit):
    n, a, b = 0, 0, 1
    while n < limit:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


f = fib(6)
print(type(f))
print(isinstance(f, Iterable))
print(isinstance(f, Iterator))
for i in f:
    print(i)
```

    <class 'generator'>
    True
    True
    1
    1
    2
    3
    5
    8
    

参考资料：七月在线课程
