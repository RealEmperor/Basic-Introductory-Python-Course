
# 类和实例

**类(Class)**：用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。

**对象**：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

**类变量**：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。

**实例变量**：定义在方法中的变量，只作用于当前实例的类。

对“类”和“对象”的使用：

　　类就是一个模板，模板里可以包含多个函数，函数里实现一些功能。

　　对象则是根据模板创建的实例，通过实例对象可以执行类中的函数。


```python
# 创建类
class Foo:
    # 类中的函数
    def bar(self):
        # 功能阐述
        pass


# =====完毕========

# 根据Foo创建对象obj
obj = Foo()
# 创建对象的时候 记得后面加个括号

```

注意，按照Python通用规则，Class用驼峰式表示(HelloWorld)

而其他的obj等等，都用‘_’隔开(this_is_object)

类中的函数第一个参数必须是self，类中定义的函数叫做“方法”。


```python
# 创建类
class Foo:

    def bar(self):
        print('Bar')

    def hello(self, name):
        print('i am %s' % name)


# 根据Foo创建的对象
obj = Foo()
obj.Bar()  # 执行Bar方法
obj.Hello('july')  # 执行Hello方法　
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-2-d2c525f2bacd> in <module>()
         11 # 根据Foo创建的对象
         12 obj = Foo()
    ---> 13 obj.Bar()  # 执行Bar方法
         14 obj.Hello('july')  # 执行Hello方法
    

    AttributeError: 'Foo' object has no attribute 'Bar'


self 是个什么鬼呢？它是为了指代它所存在的类Class之中。

比如我们如果有好几个不同的obj被创建成同一个类，

那么有了self，我们的class Foo就能很好的知道哪个指的是自己，不会乱


```python
# 创建类
class Foo:
    # 这里我们可以创建一个类级别的变量
    # 它不会随着由此类创建的变量而变化
    name = 'Jan'

    def bar(self):
        print('Bar')

    def hello(self, name):
        print('you are %s' % self.name)
        print('I am %s' % name)
        print('\n')


# 根据Foo创建的对象
obj1 = Foo()
obj2 = Foo()
obj1.hello('August')
obj2.hello('July')
```

    you are Jan
    I am August
    
    
    you are Jan
    I am July
    
    
    

所以说，这个 self 就是个代指。代指了自己所在的class。你可以由 self 点进所指class本身的函数。由此可见，self 本身作为一个代词，并不一定要叫self。你也可以用个其他什么来代替。只不过，必须得是这个类的所有子方法的第一个参数：


```python
# 创建类
class Foo:
    # 这里我们可以创建一个类级别的变量
    # 它不会随着由此类创建的变量而变化
    name = 'Jan'
    
    def bar(july):
        print('Bar')
 
    def hello(july, name): # 我这里把self改成了july，
        # 但是只要它作为第一参数的位置没变，它依旧是Foo Class的自我指代
        print('you are %s' %july.name)
        print('I am %s' %name)
        print('\n')


# 根据Foo创建的对象
obj1 = Foo()
obj2 = Foo()
obj1.hello('August')
obj2.hello('July') 
```

    you are Jan
    I am August
    
    
    you are Jan
    I am July
    
    
    

**构造函数**：构造函数，是一种特殊的方法。主要用来在创建对象时初始化对象， 即为对象成员变量赋初始值。

跟所有OOP语言一样，python也是有构造函数的，默认为:


```python
# 创建类
class Foo:

    def __init__(self):  # 这就是构造函数，它的职责是在模型创建的初期，就完成一些动作
        # 简单的说就是，自定义的初始化步骤：
        # 同样，它需要self来指代本身这个class
        self.name = 'Jan'

    def hello(self, name):
        print('you are %s' % self.name)
        print('I am %s' % name)
        print('\n')


# ==== 完毕 =====

# 当你创建一个Foo类的时候，init会被自动跑一遍：
obj = Foo()
# 在我们的例子中，我们默认给self自己的name变量，赋值为’JAN‘
# 此刻，当我们调用Foo的hello()方法时，hello自己的name变量，被赋值为'July'
obj.hello('July')

```

    you are Jan
    I am July
    
    
    

init是可以带更多的参数的，用以初始化我们的class本身。

比如说，你要初始化一个类的时候要用到一些外部参数:


```python
# 创建类
class Foo:

    def __init__(self, name2):  # 你可以在这里附加上一些参数
        # 这些参数将是你创建一个Foo类时的必要条件
        self.name = name2

    def hello(self, name):
        print('you are %s' % self.name)
        print('I am %s' % name)
        print('\n')


# ==== 完毕 =====

# 当你创建一个Foo类的时候，init会被自动跑一遍：
# 此刻，你不可以直接跑Foo(),你需要填入一个参数：name2
obj = Foo('Feb')
# 然后再调用hello, 并赋值July
obj.hello('July')

```

    you are Feb
    I am July
    
    
    

由楼上这些例子，我们大概可以知道整个Python的OOP概念了：

Class(类)就是一个把一堆Object(对象？)集合起来的地方。

在这里，无论是变量还是方法，他们享有基本一样的层级概念。只不过,方法要做一点事儿，而变量直接就是一个值。

# 访问限制

我们刚刚看到，在调用obj的时候，可以直接调出name或者使用hello()。那么我们怎么知道什么时候可以调用他们，什么时候不可以呢？

在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线、\_\_，在Python中，实例的变量名如果以\_\_开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
举个学生的例子，我们可以用一个学生类来存储学生的信息，但是我们在外部可以接触到name，那么其实我们就是可以直接修改name的，这是不安全的


```python
class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age  
    
    def detail(self):
        print(self.name)
        print(self.age)

LiLei = Student('LiLei', 12)
LiLei.age = 20
LiLei.detail()
```

    LiLei
    20
    

为了防止这种篡改年龄的事情发生，为了维护世界的和平，我们需要把关键的信息给做好隐藏：


```python
class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def detail(self):
        print(self.__name)
        print(self.__age)


LiLei = Student('LiLei', 12)
LiLei.__age = 20
LiLei.detail()
```

    LiLei
    12
    

看，如此一来，年龄就不会被更改了。

那么如何既保证安全，又能被外部修改呢？

我们使用OOP家族传统理念：**Getter+Setter**


```python
class Student(object):
    ...

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
```


```python
class Student(object):
    ...

    def set_age(self, age):
        self.__age = age
```

至此，我们应该学会使用Class来定义我们自己的类了

接下来，我们来看看：

# 在Python中展现面向对象三大特性：

面向对象的三大特性是指：封装、继承和多态。

## 封装

指的就是把内容封装到某个地方，用于日后调用

它需要：

把内容封装在某处

从另一处调用被封装的内容

### 通过对象直接调用

我们可以在存完一个内容以后，在类以外的地方，通过这个类的对象，来直接“点”调用


```python
class Student:
    # 假定我们初始化一个Student类的时候要做的就是，记录下每个学生的名字和年龄
    def __init__(self, name, age):
        self.name = name
        self.age = age  
    # 至此，我们用self指代student本身，并用name和age存下了他们的年龄和名字

    # === 完毕 ===

#此时，我们新建一个学生
obj1 = Student('July', 18)
print(obj1.name)    # 直接调用obj1对象的name属性
print(obj1.age)   # 直接调用obj1对象的age属性
obj2 = Student('Aug', 73)
print(obj2.name)    # 直接调用obj2对象的name属性
print(obj2.age)     # 直接调用obj2对象的age属性
```

    July
    18
    Aug
    73
    

### 通过self间接调用

执行类中某一个方法时，通过self来调用了类自己的变量


```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def detail(self):
        print(self.name)
        print(self.age)

    # === 完毕 ===


# 此时，我们新建一个学生
obj1 = Student('July', 18)
obj1.detail()  # Python默认将obj1传给self，所以其实我们做的是obj1.detail(obj1)
# 那么，detail()内部的样貌其实就是：
# print(obj1.name)
# print(obj1.age)
obj2 = Student('Aug', 73)
obj2.detail()

```

    July
    18
    Aug
    73
    

综上所述，对于面向对象的封装来说，其实就是使用构造方法将内容封装到 对象 中，然后通过对象直接或者self间接获取被封装的内容。

## 继承

继承，面向对象中的继承和现实生活中的继承相同，即：子可以继承父的内容（爸爸有的儿子都有）。

例如，每个学生都有名字和年龄，木有问题。我们可以把这个作为我们的父亲类。

但是，每个学生自己，可能有自己不同的“方法”，比如，每个人有每个人不同的外号，不同的口号，不同的饮食习惯，不同的……


```python
# 我们首先创建一个学生类，这个类是所有学生的爸爸
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def detail(self):
        print(self.name)
        print(self.age)


# 然后，我们创建一个小学生类，小学生特点是，LOL sala无敌
class PrimaryStudent(Student):  # 因为是继承于学生类，所以我们写在括号内
    # 这里我们可以不写构造函数，于是我们就是直接沿用Student类的构造函数
    def lol(self):  # 我们有一些新的独有的方法，会被叠加起来
        print('不服sala！')


# 接下来，我们创建一个大学生类，大学生特点是，额，每个人都有个妹子。。
class CollegeStudent(Student):
    def __init__(self, name, age, gf):  # 这里，我们改写一下构造函数
        # 于是爸爸的init会被直接overwrite
        self.name = name
        self.age = age
        self.gf = gf

    def gf_detail(self):
        print(self.gf)


# 来，我们来创建一下
obj1 = PrimaryStudent('小王', 7)
obj1.lol()  # 独有的方法
obj1.detail()  # 继承与爸爸的方法

obj2 = CollegeStudent('王思聪', 29, '张雨馨')
obj2.detail()
obj2.gf_detail()
```

所以，对于面向对象的继承来说，其实就是将多个类共有的方法提取到父类中，子类仅需继承父类而不必一一实现每个方法。

这样可以极大的提高效率，减少代码的重复。

### 问题来了，如果我想多认个干爹呢？

Python和Java/C#的不同就是，Python可以多类继承，也就是，可以认很多干爹

但是干爹多了，就出了问题了。继承的时候，从谁先开始？

有两种方式，分别是深度优先和广度优先

>* 当本身的类是经典类的时候，就按照深度优先方式查找继承的方法 （即，找到一个爸爸，继续找这个爸爸的爸爸，爸爸的爸爸的爸爸。。。）
>* 当本身的类是新式类的时候，就按照广度优先的方式查找 （即，找到一个爸爸，再找下一个爸爸，再找下一个爸爸，平辈之间查找）

那么为什么有经典类和新类之分呢？

这是个历史遗留问题，新类 统一了类(class)和类型(type)，所以其实也是社区推荐的写法，只不过。。很多程序员都很懒。。

在2.2之前，比如2.1版本中，类和类型是不同的，如a是ClassA的一个实例，那么a.\_\_class\_\_返回 ‘ class    \_\_main\_\_.ClassA‘ ，type(a)返回总是<type 'instance'>。而引入新类后，比如ClassB是个新类，b是ClassB的实例，b.\_\_class\_\_和type(b)都是返回‘class '\_\_main\_\_.ClassB' ，这样就统一了。
于是乎，在新版的Python中，这个经典类和新类的区别已经不存在，都统一使用广度优先。

我们先假设我们还活在python2.2的时代：


```python
#经典类的写法
class c1:
    pass
class c2(c1):
    pass

#新类的写法
class N1(object):
    pass
class N2(N1):
    pass
```

可见，新类的标志就是，大家的老祖宗继承于一个系统级的类，叫Object

具体的，我们来看看：

经典类


```python
class D:

    def bar(self):
        print('D.bar')


class C(D):

    def bar(self):
        print('C.bar')


class B(D):
    pass


class A(B, C):
    pass


a = A()
# 执行bar方法时
# 首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有，则继续去D类中找，如果D类中么有，则继续去C类中找，如果还是未找到，则报错
# 所以，查找顺序：A --> B --> D --> C
# 在上述查找bar方法的过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
a.bar()

```

    C.bar
    

新类


```python
class D(object):

    def bar(self):
        print('D.bar')


class C(D):

    def bar(self):
        print('C.bar')


class B(D):
    pass


class A(B, C):
    pass


a = A()
# 执行bar方法时
# 首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有，则继续去C类中找，如果C类中么有，则继续去D类中找，如果还是未找到，则报错
# 所以，查找顺序：A --> B --> C --> D
# 在上述查找bar方法的过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
a.bar()

```

    C.bar
    

当然，对我们先现在而言，两种写法都得出C.bar ；这说明，已经木有区别了。

# 多态

Pyhon不支持多态并且也用不到多态，多态的概念是应用于Java和C#这一类强类型语言中，而Python崇尚“鸭子类型（Duck Typing）”。

什么是鸭子类型？其实翻译成中文最好是叫：好猫类型。

也就是引用了小平同志的一句话，不管黑猫白猫抓到老鼠的就是好猫。

不同于强类型的语言，一个类型的obj只能一种事儿，

在Python中，只要是能“不报错运行”的类型，都可以塞进参数中去：


```python
class F1:
    pass


# 假设，S1是我们的正统类，它继承于根正苗红的F1，是我们的正统类
class S1(F1):
    def show(self):
        print('S1.show')


# S2是路人甲，是个歪瓜裂枣，但是他自己也有一个叫show的方法。
class S2:
    def show(self):
        print('S2.show')


# 在Java或C#中定义函数参数时，必须指定参数的类型，也即是说，我们如果用
# Java写下面的Func，需要告知，obj是F1类还是其他什么东西。
# 如果限定了F1，那么S2是不可以被采纳的。
# 然而，在Python中，一切都是Obj，它不care你到底是什么类，直接塞进去就可以

def Func(obj):
    """Func函数需要接收一个F1类型或者F1子类的类型"""
    obj.show()


s1_obj = S1()
Func(s1_obj)  # 在Func函数中传入S1类的对象 s1_obj，执行 S1 的show方法，结果：S1.show

s2_obj = S2()
Func(s2_obj)  # 在Func函数中传入Ss类的对象 ss_obj，执行 Ss 的show方法，结果：S2.show

```

    S1.show
    S2.show
    

# 获取对象信息

当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？

## 用type()


```python
type(123)
```




    int




```python
type('str')
```




    str




```python
type(None)
```




    NoneType




```python
type(abs)
```




    builtin_function_or_method




```python
class a:
    def __init__(self):
        pass


type(a)

```




    type




```python
type(123)==type(456)
```




    True




```python
type('abc')==type('123')
```




    True




```python
type('abc')==type(123)
```




    False




```python
type('abc')==str
```




    True




```python
type([])==list
```




    True



## 用isinstance()
isinstance()可以告诉我们，一个对象是否是某种类型（包括继承关系）。


```python
class A:
    pass


class B(A):
    pass


class C(B):
    pass


k = A()
g = B()
y = C()

isinstance(y, C)

```




    True




```python
isinstance(y, B)
```




    True



同理，isinstance()也可以当type()用


```python
isinstance('a', str)
```




    True



## 使用dir()

如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：


```python
dir('ABC')
```




    ['__add__',
     '__class__',
     '__contains__',
     '__delattr__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getitem__',
     '__getnewargs__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__iter__',
     '__le__',
     '__len__',
     '__lt__',
     '__mod__',
     '__mul__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rmod__',
     '__rmul__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     'capitalize',
     'casefold',
     'center',
     'count',
     'encode',
     'endswith',
     'expandtabs',
     'find',
     'format',
     'format_map',
     'index',
     'isalnum',
     'isalpha',
     'isdecimal',
     'isdigit',
     'isidentifier',
     'islower',
     'isnumeric',
     'isprintable',
     'isspace',
     'istitle',
     'isupper',
     'join',
     'ljust',
     'lower',
     'lstrip',
     'maketrans',
     'partition',
     'replace',
     'rfind',
     'rindex',
     'rjust',
     'rpartition',
     'rsplit',
     'rstrip',
     'split',
     'splitlines',
     'startswith',
     'strip',
     'swapcase',
     'title',
     'translate',
     'upper',
     'zfill']



类似\_\_xxx\_\_的属性和方法在Python中都是有特殊用途的，比如\_\_len\_\_方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的\_\_len\_\_()方法，所以，下面的代码是等价的：


```python
'ABC'.__len__()
```




    3



我们自己写的类，如果也想用len(myObj)的话，就自己写一个\_\_len\_\_()方法：


```python
class MyObject:
    def __len__(self):
        return 100


obj = MyObject()
len(obj)
```




    100



仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：


```python
class MyObject:
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
```

紧接着，可以测试该对象的属性：


```python
hasattr(obj, 'x') #有木有属性'x'
```




    True




```python
obj.x
```




    9




```python
hasattr(obj, 'y') # 有属性'y'吗？
```




    False




```python
setattr(obj, 'y', 19) # 设置一个属性'y'
```


```python
hasattr(obj, 'y') # 有属性'y'吗？
```




    True




```python
getattr(obj, 'y') # 获取属性'y'
```




    19




```python
obj.y # 获取属性'y'
```




    19



可以传入一个default参数，如果属性不存在，就返回默认值：


```python
getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
```




    404



也可以获得对象的方法：


```python
hasattr(obj, 'power') # 有属性'power'吗？
```




    True




```python
getattr(obj, 'power') # 获取属性'power'
```




    <bound method MyObject.power of <__main__.MyObject object at 0x000001B7A99D5DA0>>




```python
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
```


```python
fn # fn指向obj.power
```




    <bound method MyObject.power of <__main__.MyObject object at 0x000001B7A99D5DA0>>




```python
fn() # 调用fn()与调用obj.power()是一样的
```




    81



# 实例属性和类属性

由于Python是动态语言，根据类创建的实例可以任意绑定属性。

给实例绑定属性的方法是通过实例变量，或者通过self变量：


```python
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
```

但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：


```python
class Student(object):
    name = 'Student'
```


```python
我们来用一个例子说明一下实例与类的属性差异：
```


      File "<ipython-input-50-186a434d98b3>", line 1
        我们来用一个例子说明一下实例与类的属性差异：
                             ^
    SyntaxError: invalid character in identifier
    



```python
class Student(object):
    name = 'Student'

s = Student() # 创建实例s
print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
```

    Student
    


```python
print(Student.name) # 打印类的name属性
```

    Student
    


```python
s.name = 'Michael' # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
```

    Michael
    


```python
print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
```

    Student
    


```python
del s.name # 如果删除实例的name属性
```


```python
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
```

    Student
    

从上面的例子可以看出，在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

# 模块和包

Python的程序由包（package）、模块（module）和函数组成。包是由一系列模块组成的集合。模块是处理某一类问题的函数和类的集合。

包就是一个完成特定任务的工具箱，Python提供了许多有用的工具包，如字符串处理、图形用户接口、Web应用、图形图像处理等。这些自带的工具包和模块安装在Python的安装目录下的Lib子目录中。

注意：
包必须至少含有一个\_\_int\_\_.py文件按，该文件的内容可以为空。\_\_int\_\_.py用于标识当前文件夹是一个包。

## 模块

在python中一个文件可以被看成一个独立模块，而包对应着文件夹，模块把python代码分成一些有组织的代码段，通过导入的方式实现代码重用。

导入模块时，是按照sys.path变量的值搜索模块，sys.path的值是包含每一个独立路径的列表，包含当前目录、python安装目录、PYTHONPATH环境变量，搜索顺序按照路径在列表中的顺序（一般当前目录优先级最高）。

想看自己的Python路径，大家可以

import sys
print(sys.path)
如果你发现你在某个地方写的文件（包）import错误，你就可以看看这个sys.path是否囊括了你那批文件的根目录。

## 导入模块

使用import语句（不管是你自己写的，还是你下载的别人的）

import module1

import module2

import module3

import module1,module2,module3

这两种方式的效果是一样的，但是第一种可读性比第二种好，推荐按照下面的顺序导入模块，并且一般在文件首部导入所有的模块

python标准库

第三方模块

应用程序自定义模块

## 使用from-import语句导入模块的属性

单行导入

from module import name1,name2,name3

多行导入

from module import name1,name2,name3

导入全部属性（由于容易覆盖当前名称空间中现有的名字，所以一般不推荐使用，适合模块中变量名很长并且变量很多的情况）

from module import \*

## 自定义导入模块名称

就是为了用的时候方便好记。

import simplejson as json

## 包

包将有联系的模块组织在一起，有效避免模块名称冲突问题，让应用组织结构更加清晰。 一个普通的python应用程序目录结构：

app/
\_\_init\_\_.py
a/
\_\_init\_\_.py
a.py
b/
\_\_init\_\_.py
b.py
app是最顶层的包，a和b是它的子包，可以这样导入：

from app.a import a
from app.b.b import test

a.test()
test()
上面代码表示：导入app包的子包a和子包b的属性test，然后分别调用test方法。
每个目录下都有\_\_init\_\_.py文件，这个是初始化模块，from-import语句导入子包时需要它，可以在里面做一些初始化工作，也可以是空文件。ps：\_\_init\_\_.py定义的属性直接使用 顶层包.子包 的方式导入，如在目录a的\_\_init\_\_.py文件中定义init_db()方法，调用如下：
from app import a

a.init_db()

## 实战

我们现在已经完全掌握了使用包，自己定义类，组件一个可运行的程序的方法

现在我们可以专注于Machine Learning方面，来看看实战是怎么运用这些知识的。


```python
from sklearn import svm, datasets


class Dataset:
    # 我们创造一个dataset的类，这个类会帮我们下载相关的数据集，
    # 并给我们分类好x,y
    def __init__(self, name):
        # 告诉类，我们需要哪一个数据集
        # 我们有两个选择，一个是'iris'一个是'digits'
        self.name = name

    def download_data(self):
        # 从sklearn的自带集中下载我们指定的数据集
        if self.name == 'iris':
            # 这里是sklearn自带的数据集下载方法，更多信息可以参照官网
            self.downloaded_data = datasets.load_iris()
        elif self.name == 'digits':
            self.downloaded_data = datasets.load_digits()
        else:
            # 如果不是我们预想的两种数据集，则报错
            print('Dataset Error: No named datasets')

    def generate_xy(self):
        # 通过这个过程来把我们的数据集分为原始数据以及他们的label
        # 我们先把数据下载下来
        self.download_data()
        x = self.downloaded_data.data
        y = self.downloaded_data.target
        print('\nOriginal data looks like this: \n', x)
        print('\nLabels looks like this: \n', y)
        return x, y

    def get_train_test_set(self, ratio):
        # 这里，我们把所有的数据分成训练集和测试集
        # 一个参数要求我们告知，我们以多少的比例来分割训练和测试集
        # 首先，我们把XY给generate出来：
        x, y = self.generate_xy()

        # 有个比例，我们首先得知道 一共有多少的数据
        n_samples = len(x)
        # 于是我们知道，有多少应该是训练集，多少应该是测试集
        n_train = int(n_samples * ratio)
        # 好了，接下来我们分割数据
        X_train = x[:n_train]
        y_train = y[:n_train]
        X_test = x[n_train:]
        y_test = y[n_train:]
        # 好，我们得到了所有想要的玩意儿
        return X_train, y_train, X_test, y_test
# ====== 我们的dataset类创造完毕=======

```

接下来，我们在main中code以下来调用我们自己写的类：


```python
# 比如，我们使用digits数据集
data = Dataset('digits')
# 接着，我们可以用0.7的分割率把xy给分割出来
X_train, y_train, X_test, y_test = data.get_train_test_set(0.7)
```

    
    Original data looks like this: 
     [[  0.   0.   5. ...,   0.   0.   0.]
     [  0.   0.   0. ...,  10.   0.   0.]
     [  0.   0.   0. ...,  16.   9.   0.]
     ..., 
     [  0.   0.   1. ...,   6.   0.   0.]
     [  0.   0.   2. ...,  12.   0.   0.]
     [  0.   0.  10. ...,  12.   1.   0.]]
    
    Labels looks like this: 
     [0 1 2 ..., 8 9 8]
    

同样，我们也不一定需要自己创造类，我们可以引用第三方库里的类， 比如这里，我们用SVM作为我们的分类器，去训练我们的算法 我们就直接建造一个object，使他成为SVM类


```python
clf = svm.SVC()
```

这里 clf 是 classifier的简称，SVC指的是SVM的classification版本。

因为我们的数据集都是分类问题，所以我们使用SVC()

接下来，我们fit我们的数据（也就是训练我们的数据）

显然，做fit的时候，我们只可以使用训练集


```python
clf.fit(X_train, y_train)
```




    SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
      decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
      max_iter=-1, probability=False, random_state=None, shrinking=True,
      tol=0.001, verbose=False)



好，现在你的clf已经训练好了，我们来看看它的表现：

我们随便取test集中的一个数据点，并对应它的真实label


```python
test_point = X_test[12]
y_true = y_test[12]
```

好，现在你的clf已经训练好了，我们来看看它的表现：

我们随便取test集中的一个数据点，并对应它的真实label


```python
test_point = X_test[12]
y_true = y_test[12]
```

我们来看看，我们的clf给出的预测是什么：


```python
clf.predict(test_point)
```

    C:\ProgramData\Anaconda3\lib\site-packages\sklearn\utils\validation.py:395: DeprecationWarning: Passing 1d arrays as data is deprecated in 0.17 and will raise ValueError in 0.19. Reshape your data either using X.reshape(-1, 1) if your data has a single feature or X.reshape(1, -1) if it contains a single sample.
      DeprecationWarning)
    




    array([7])



再看看真正的label应该是什么:


```python
y_true
```




    7



正确！

那么这样，你们已经学会如何训练数据集并作出新的预测了。

把所有的测试集都导入clf，让他pridict，并看看跟真实的label相差多少。

参考资料：七月在线课程
