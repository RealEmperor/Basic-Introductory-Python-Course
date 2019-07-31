
# __slots__和property

方法和属性的动态绑定

使用\_\_slots\_\_限定class实例能添加的属性

\_\_slots\_\_仅对当前类实例起作用，对继承的子类是不起作用的。

例子代码


```python
# __slots__
import traceback

from types import MethodType


class MyClass(object):
    __slots__ = ['name', 'set_name']


def set_name(self, name):
    self.name = name


cls = MyClass()
cls.name = 'Tom'
cls.set_name = MethodType(set_name, cls)
cls.set_name('Jerry')
print(cls.name)
try:
    cls.age = 30
except AttributeError:
    traceback.print_exc()
```


```python
class ExtMyClass(MyClass):
    pass


ext_cls = ExtMyClass()
ext_cls.age = 30
print(ext_cls.age)
```

直接暴露属性的局限性

使用get/set方法

利用@property简化get/set方法

利用@property实现只读属性

例子代码


```python
import traceback


class Student:
    # get
    @property
    def score(self):
        return self._score

    # set
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('not int')

        elif (value < 0) or (value > 100):
            raise ValueError('not between 0 ~ 100')

        self._score = value

    # get, 只有get相当于只读
    @property
    def double_score(self):
        return self._score * 2


s = Student()
s.score = 75
print(s.score)
```


```python
try:
    s.score = 'abc'
except ValueError:
    traceback.print_exc()
```


```python
try:
    s.score = 101
except:
    traceback.print_exc()
```


```python
print(s.double_score)
```


```python
try:
    s.double_score = 150
except AttributeError:
    traceback.print_exc()
```

装饰器与property实现


```python
# 实现了__set__，__get__，__delete__ 方法的类称为描述了，控制类的读、写、删除
# 具体定义查百度
# 参考 class property(object) 源码，自定义类：MyProperty
class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        print(fget)
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, cls):
        if self.fget:
            print('__get__')
            return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset:
            print('__set__')
            return self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel:
            return self.fdel(instance)

    def getter(self, fn):
        self.fget = fn

    def setter(self, fn):
        self.fset = fn

    def deleter(self, fn):
        self.fdel = fn


class Student:
    @MyProperty
    def score(self):
        return self._score

    @score.setter
    def set_score(self, value):
        self._score = value


s = Student()
s.score = 95
print(s.score)

```

# 特殊方法与类的定制

类的默认行为与定制

常见特殊方法

例子代码


```python
# __str__
class MyClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print('print will call __str__ first.')
        return 'Hello ' + self.name + '!'


print(MyClass('Tom'))
```


```python
#  __next__
class Fib100:
    def __init__(self):
        self._1, self._2 = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self._1, self._2 = self._2, self._1 + self._2
        if self._1 > 100:
            raise StopIteration()
        return self._1


for i in Fib100():
    print(i)

```


```python
# __call__
class MyClass:
    def __call__(self):
        print('You can call cls() directly.')


cls = MyClass()
cls()

print(callable(cls))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))

```

# 枚举类

枚举 vs 变量

@unique帮助去重

例子代码


```python
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

jan = Month.Jan
print(jan)

```

# 元类

运行时动态创建 vs 编译时定义

使用type创建新类型


```python
def init(self, name):
    self.name = name


def say_hello(self):
    print('Hello, %s!' % self.name)


# Hello = type('Hello', (object, ), dict(__init__ = init, hello = say_hello))
Hello = type('Hello', (object,), {'__init__': init, 'hello': say_hello})
'''
class Hello:
    def __init__(...)
    def hello(...)
'''
h = Hello('Tom')
h.hello()

```

metaclass（元类）

metaclass -> class -> instance

继承和动态绑定可以解决问题吗？

\_\_new\_\_函数


```python
def add(self, value):
    self.append(value)


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        print(cls)  # <class '__main__.ListMetaclass'>
        print(name)  # MyList
        print(bases)  # (<class 'list'>,)
        print(type(attrs))  # <class 'dict'>
        # attrs['add'] = lambda self, value: self.append(value)
        attrs['add'] = add
        attrs['name'] = 'Tom'
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):  # 额外增加add方法，实际等价于append。
    pass


mli = MyList()
mli.add(1)
mli.add(2)
mli.add(3)
print(mli.name)
print(mli)

```

ORM框架实例分析


```python
class Field:
    def __init__(self, name, col_type):
        self.name = name
        self.col_type = col_type


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'integer')


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(1024)')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Model name: %s' % name)
        mappings = {}
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Field name: %s' % k)
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kvs):
        super(Model, self).__init__(**kvs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '%s'." % key)

    def __setattr__(self, key, value):
        print('__setattr__')
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s(%s) values(%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('sql:', sql)
        print('args:', args)


class User(Model):
    id = IntegerField('id')
    name = StringField('name')


# u = User(id = 100, name = 'Tom')
u = User()
u.id = 100
u.name = 'Tom'
u.save()

```

# 异常与错误处理

为什么使用异常？

异常的抛出与捕捉

traceback使用 （参考：https://docs.python.org/zh-cn/3/library/traceback.html ）

logging使用与配置（参考：https://cloud.tencent.com/developer/article/1354396 ）

例子代码


```python
import traceback

try:
    # r = 10 / 0
    r = 10 / 1
except ZeroDivisionError as e:
    print(e)
    r = 1
else:
    print('没有异常')
finally:
    print('不管有没有异常都执行')
print(r)

```

# 单元测试

为什么需要单元测试

unittest使用 （参考：https://docs.python.org/zh-cn/3/library/unittest.html ）

mock介绍与使用 （参考：https://docs.python.org/zh-cn/3/library/unittest.mock-examples.html ）

例子代码：


```python
import unittest


class MyDict(dict):
    pass


class TestMyDict(unittest.TestCase):
    def setUp(self):
        print('测试前准备')

    def tearDown(self):
        print('测试后清理')

    def test_init(self):
        md = MyDict(one=1, two=2)
        self.assertEqual(md['one'], 1)
        self.assertEqual(md['two'], 2)
        # self.assertEqual(md['two'], 3)

    def test_nothing(self):
        pass


if __name__ == '__main__':
    unittest.main()

# python test_module.py
# python -m unittest test_module
# python -m unittest test_module.test_class
# python -m unittest test_module.test_class.test_method

```

参考资料：七月在线课程
