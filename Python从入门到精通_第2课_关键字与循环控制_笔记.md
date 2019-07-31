
# 变量和类型

## 基本变量类型
整数 int

浮点数 float

字符串 str

布尔值 bool

空值 NoneType

函数 function

模块 module

## 变量定义
变量存储在内存中的值。这就意味着在创建变量时会在内存中开辟一个空间。
基于变量的数据类型，解释器会分配指定内存，并决定什么数据可以被存储在内存中。
变量可以指定不同的数据类型，这些变量可以存储整数，小数或字符。（弱类型）

## 变量赋值
每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。（重要！！！）
等号（=）用来给变量赋值，等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。


```python
# 基本类型
print(type(None))
print(type(True))
print(type(12345))
print(type(123.45))
print(type(1234.))
print(type('abc'))
```

    <class 'NoneType'>
    <class 'bool'>
    <class 'int'>
    <class 'float'>
    <class 'float'>
    <class 'str'>
    


```python
# 容器类型
print(type([1, 2, 3, 'a', 'bc']))
print(type((1, 2, 3, 'abc')))
values = ['abc', 1, 2, 3.]
print(type(values[3]))
print(type(set(['a', 1, 2.])))
print(type({'a': 123, 4: 'bcd', 5: 'efg'}))
```

    <class 'list'>
    <class 'tuple'>
    <class 'float'>
    <class 'set'>
    <class 'dict'>
    


```python
# 函数
def func():
    print(100)


print(type(func))
```

    <class 'function'>
    


```python
# 模块
import string
print(type(string))
```

    <class 'module'>
    


```python
# 自定义类型与类型实例
class Cls:
    pass


print(type(Cls))
cls = Cls()
print(type(cls))
```

    <class 'type'>
    <class '__main__.Cls'>
    


```python
# 变量赋值
try:
    print(x)    # 变量必须先赋值再使用
except NameError:
    print("NameError: name 'x' is not defined")
    
x = 100
x = 'abcd'  # x的类型不受限制
```

    NameError: name 'x' is not defined
    

# 常见字符串处理

去除空格及特殊符号：strip, lstrip, rstrip


复制字符串：str1 = str2


连接字符串

str2 += str1

new_str = str2 + str1


查找字符串：pos = str1.index(str2)


比较字符串：cmp(str1, str2)


字符串长度：len(str)


大小写转换

u_str = str.upper()

l_str = str.lower()


首字母大写：str.capitalize(); string.capword(str)


分割与合并字符串：split, splitlines, join


类型转换：int, float转换

格式化字符串


字符串测试

str.startwith(prefix)	

str.endwith(suffix)

str.isalnum() # 是否全是字母和数字，并至少有一个字符。

str.isalpha() # 是否全是字母，并至少有一个字符。

str.isdigit() # 是否全是数字，并至少有一个字符。

str.isspace() # 是否全是空白字符，并至少有一个字符。

str.islower() # 字母是否全是小写

str.isupper() # 字母是否全是大写

str.istitle() # 首字母是否大写



```python
# strip去除空格
s = ' abcd efg  '
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s)
```

    abcd efg
    abcd efg  
     abcd efg
     abcd efg  
    


```python
# 字符串连接
print('abc_' + 'defg')
s = 'abcdefg'
s += '\nhijk'
print(str)
```

    abc_defg
    <class 'str'>
    


```python
# 大写小
s = 'abc defg'
print(s.upper())
print(s.upper().lower())
print(s.capitalize())
```

    ABC DEFG
    abc defg
    Abc defg
    


```python
# 位置和比较
s_1 = 'abcdefg'
s_2 = 'abdefgh'
print(s_1.index('bcd'))
try:
    print(s_1.index('bce'))
except ValueError:
    print('ValueError: substring not found')
print(s_1 == s_1)  # cmp函数被Python3移除了
print(s_1 > s_2)
print(s_2 > s_1)
```

    1
    ValueError: substring not found
    True
    False
    True
    


```python
# 分割和连接
s = 'abc,def,ghi'
print(s.split(','))
s = '123\n456\n789'
numbers = s.splitlines()
print(numbers)
print('-'.join(numbers))
```

    ['abc', 'def', 'ghi']
    ['123', '456', '789']
    123-456-789
    


```python
# 常用判断
s = 'abcdefg'
print(s.startswith('abc'))
print(s.endswith('efg'))
print('abcd1234'.isalnum())
print('\tabcd1234'.isalnum())
print('abcd'.isalpha())
print('12345'.isdigit())
print('  '.isspace())
print('acb125'.islower())
print('A1B2C'.isupper())
print('Hello world!'.istitle())
```

    True
    True
    True
    False
    True
    True
    True
    True
    True
    False
    


```python
# 数字到字符串
print(str(5))
print(str(5.))
print(str(-5.23))
print(int('1234'))
print(float('-23.456'))
```

    5
    5.0
    -5.23
    1234
    -23.456
    


```python
# 格式化字符串
print('Hello %s!' % 'world')
print('%d-%.2f-%s' % (4, -2.3, 'hello'))
```

    Hello world!
    4--2.30-hello
    

# 条件判断

真值判断

if x == True:

if x:

if not x:

空值判断

if x is None:

if not x:

比较

if a == b:

if a > b:

...


```python
# if判断
a = 100
b = 200
c = 300
if c == a:
    print(a)
elif c == b:
    print(b)
else:
    print(c)
```

    300
    


```python
# None的判断
x = None
if x is None:
    print('x is None')
if not x:
    print('x is None')
```

    x is None
    x is None
    

# 循环控制

for循环

for i in range(begin, end, steps): <=> for (i = begin; i < end; i += steps)

while循环

while 条件判断:

循环嵌套

循环控制

break

continue

pass


```python
# for循环
s = 0
for i in range(0, 101):
    s += i
print(s)
```

    5050
    


```python
# while循环
s = 0
i = 0
while i <= 100:
    s += i
    i += 1
print(s)
```

    5050
    


```python
# continue/pass/break
for i in range(0, 100):
    if i < 10:
        pass
    elif i < 30:
        continue
    elif i < 35:
        print(i)
    else:
        break
```

    30
    31
    32
    33
    34
    

# 函数

函数定义格式

默认参数

可变参数：*args，自动组装成tuple

关键字参数：*args，自动组装成dict

命名关键字参数

函数调用

函数名(参数名)

模块名.函数名(参数名)

带参数名调用

什么是递归？


```python
# 函数定义和默认参数
def func(x, y=500):
    print(x, y)


func(150)
func(100, 200)
func(y=300, x=100)
```

    150 500
    100 200
    100 300
    


```python
# 可变参数
def func(name, *numbers):
    print(name)
    print(numbers)


func('Tom', 1, 2, 3, 4)
```

    Tom
    (1, 2, 3, 4)
    


```python
# 关键字参数
def func(name, **kvs):
    print(name)
    print(kvs)
    
    
func('Jack', china='Beijing', uk='London')
```

    Jack
    {'china': 'Beijing', 'uk': 'London'}
    


```python
# 命名关键字参数
def func(*, china, uk):  # *用于和普通参数做分割，*args一样效果
    print(china, uk)


func(china='Beijing', uk='London')  # 必须传入参数名
```

    Beijing London
    


```python
# 复杂情况
def func(a, b, c=0, *args, **kvs):
    print(a, b, c, args, kvs)


func(1, 2)
func(1, 2, 3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', china='Beijing', uk='London')
func(1, 2, 3, *('a', 'b'), **{'china': 'Beijing', 'uk': 'London'})
```

    1 2 0 () {}
    1 2 3 () {}
    1 2 3 ('a', 'b') {}
    1 2 3 ('a', 'b') {'china': 'Beijing', 'uk': 'London'}
    1 2 3 ('a', 'b') {'china': 'Beijing', 'uk': 'London'}
    


```python
# 递归的经典例子！
# 斐波那契数列
def fib(n):
    if n < 1:
        raise ValueError
    elif (n == 1) or (n == 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
```

    1
    1
    2
    3
    5
    8
    


```python
# 汉诺塔
def move(n, source, target, helper):
    if n == 1:
        print(source + ' -> ' + target)
    else:
        move(n - 1, source, helper, target)
        print(source + ' -> ' + target)
        move(n - 1, helper, target, source)


move(4, 'A', 'B', 'C')
```

    A -> C
    A -> B
    C -> B
    A -> C
    B -> A
    B -> C
    A -> C
    A -> B
    C -> B
    C -> A
    B -> A
    C -> B
    A -> C
    A -> B
    C -> B
    

参考资料：七月在线课程
