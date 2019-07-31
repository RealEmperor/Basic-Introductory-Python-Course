
# 文本文件读写3种方法

## 第一种方法

直接读入


```python
file1 = open("data/test.txt")
file2 = open("data/output.txt", "w")

while True:
    line = file1.readline()
    # 这里可以进行逻辑处理
    file2.write('"' + line[:1] + '"' + ",")
    if not line:
        break
# 记住文件处理完，关闭是个好习惯
file1.close()
file2.close()
```

读文件有3种方法：

- read()将文本文件所有行读到一个字符串中。
- readline()是一行一行的读
- readlines()是将文本文件中所有行读到一个list中，文本文件每一行是list的一个元素。 优点：readline()可以在读行过程中跳过特定行。

## 第二种方法：

文件迭代器，用for循环的方法


```python
file2 = open("data/output.txt", "w")
for line in open("data/test.txt"):
    # 这里可以进行逻辑处理
    file2.write('"' + line[:1] + '"' + ",")
```

## 第三种方法：

文件上下文管理器


```python
# 打开文件
# 用with..open自带关闭文本的功能
with open('data/somefile.txt', 'r') as f:
    data = f.read()

# loop整个文档
with open('data/somefile.txt', 'r') as f:
    for line in f:
        # 处理每一行
        pass

# 写入文本 
with open('data/somefile.txt', 'w') as f:
    f.write('text1')
    f.write('text2')
    # ...

# 把要打印的line写入文件中 
with open('data/somefile.txt', 'w') as f:
    print('line1', file=f)
    print('line2', file=f)
```

# 二进制文件读写

Python默认读取的都是文本文件。要是想要读取二进制文件，需要把刚刚的'r'改成'rb'.


```python
f = open('data/pic.jpg', 'rb')
print(f.read())
# 输出 '\xff\xd8\xff\xe0\x00\x10JFIF\x00\...' # 十六进制表示的字节
```

简单说就是，任何非标准的文本文件（对于Py2来说，标准是ASCII，对于Py3来说，标准是unicode），你就需要用二进制读入这个文件，然后再用 .decode('...')的方法来解码这个二进制文件：


```python
f = open('DegangGuo.txt', 'rb')
# 读入郭德纲老师的作文, 但是郭老师用的是参合着错别字的繁体编码，假设叫个"DeyunCode"
# 那么你读入以后，就需要解码它
u = f.read().decode('DeyunCode')
```

# 文件和目录操作

在图形界面的操作系统下，这个很简单，就是右键/拖拽 等等。

但是在Python的代码内该怎么做呢？

## 基本操作

用Python内置的os模块直接调用操作系统提供的接口函数：


```python
import os
os.name
```

这里是通过OS告诉我们 我的操作系统的名字。 如果是posix，说明系统是#nix族，如果是nt，就是Windows

我们可以调用uname()来看看具体信息

## 环境变量

在操作系统中定义的环境变量，全部保存在os.environ这个dict中，可以直接查看：


```python
os.environ
```

## 操作文件与目录

查看、创建和删除目录可以这么调用：


```python
# 当前目录的绝对路径
os.path.abspath('.')
# 比如这里返回：'/Users/EDC'

# 在某个目录下创建一个新目录，
# 首先把新目录的完整路径表示出来:
os.path.join('/Users/EDC', 'Pictures')
# 这里你得到的是一个字符串，代表了新的文件夹是这个位置：/Users/EDC/Pictures/
# 自己也可以拼起来，但是怕不同操作系统下的区分符问题，最好是用OS接口
# 但是你还并没有创建任何的文件

# 需要用mkdir创建：
os.mkdir('/Users/EDC/Pictures/')

# 同理，删除一个文件夹
os.rmdir('/Users/EDC/Pictures/')
```

同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：


```python
os.path.split('/Users/EDC/Pictures/AJiao.avi')
# ('/Users/EDC/Pictures/', 'AJiao.avi')
```

或者靠os.path.splitext()得到文件扩展名：


```python
os.path.splitext('/Users/EDC/Pictures/AJiao.avi')
# ('/Users/EDC/Pictures/AJiao', '.avi')
```

文件重命名：


```python
os.rename('JAV-001.avi', '学习资料')
```

删除文件


```python
os.remove('学习资料')
```

尴尬的是。。复制文件并不存在于os里。。(⊙﹏⊙)b

原因是复制这个操作，不是由操作系统提供的系统调用。

我们可以用上面的代码，读入一个文件，再写入一个文件，来达到复制的目的。

当然，Python作为一个Glue Language的调性，总有第三方库来帮我们stay lazy：

Shutil就是其中一个。基本上可以看做是os的补充。它提供copyfile()方法，来复制你的文件:


```python
import shutil  
shutil.copyfile('/path/to/file', '/path/to/other/file')
```

这个库用起来比os爽很多。你们可以自己百度一下。看看文档。比较简单易用

小例子：

通过我们之前提过的方法，我们来看看怎么完成如下任务：

列出当前目录下的所有目录：


```python
[x for x in os.listdir('.') if os.path.isdir(x)]
# 你会得到一个list of 文件夹
```

只想列出.py文件：


```python
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
# 列出所有的py文件
```

# 序列化和反序列化

什么是序列化？

程序运行的过程中，所有变量都是在内存中操作的，当程序一旦执行完毕，结束退出后，变量占有的内存就被操作系统回收了。 因此我们需要将某些数据持久化存储到磁盘中，下次运行的时候从磁盘中读取相关数据。

我们将变量从内存中变成可以存储或传输的过程称之为序列化，在Python中叫做pickling，在其它语言中也称之为 serialization、marshaling、flattening等等，说的都是一个意思。 反之，则为反序列化，称之为unpickling，把变量内容从序列化的对象重新读取到内存中。

## 序列化：


```python
import pickle

# 此处定义一个dict字典对象
d = dict(name='思聪', age=29, score=80)
str = pickle.dumps(d)  # 调用pickle的dumps函数进行序列化处理
print(str)
# 你可以看看它长什么样子

# 定义和创建一个file文件对象，设定模式为wb
f = open('data/dump.txt', 'wb')
# 将内容序列化写入到file文件中
pickle.dump(d, f)
f.close()  # 最后关闭掉文件资源
```

## 反序列化：

就是把刚刚的搞成的“序列化”的码，转成python看得懂的object


```python
import pickle

# 从之前序列化的dump.txt文件里边读取内容
f = open('data/dump.txt', 'rb')  # 设定文件选项模式为rb
d = pickle.load(f)  # 调用load做反序列处理过程
f.close()  # 关闭文件资源
print(d)
print('name is %s' % d['name'])
```

稍微注意一下，python2和python3里面的pickle不一样。

为了保证2，3的和谐，你可以用这个方法来保证你import正确：


```python
try:
    import cPickle as pickle
except ImportError:
    import pickle
```

## 用JSON实现序列和反序列化

同时，也许你们也会发现，这个pickle完的东西，是让人看不懂的。只有python自己可以把它unpickle回来。

如果我们有一个文件现在存下来，并且日后要在其他地方用到的话，

我们可以用JSON来做序列化。Python的数据结构跟Json有非常完美的兼容：

| JSON类型	| Python类型 |
| --------   | -----:  | :----:  |
| {}	| dict |
| []	| list |
| "string" |	'str'或者u'unicode' |
| 1234.56	| int或float |
| true/false |	True/False |
| null	| None |

如果你有一个比较结构化的数据想要序列化，并且想要别的地方别的语言也能看得懂。那么你可以用JSON来做：


```python
import json
 
# 定义dict字典对象
d1 = dict(name='小王', age=20, score=80)
str = json.dumps(d1) # 调用json的dumps函数进行json序列化处理
print(str)
 
# 调用json的loads函数进行反序列化处理
d2 = json.loads(str)
```

# 高阶函数

可以把别的函数作为参数传入的函数叫高阶函数。

举个例子：求绝对值的函数 abs()


```python
abs(-10)
```




    10



如果只写abs我们得到是它是一个叫abs的函数


```python
abs
```




    <function abs>




```python
上堂课我讲过，python里变量和函数都是object

那么就是说，abs这函数可以直接复制给另外一个变量：
```


      File "<ipython-input-33-db33b7caa8f7>", line 1
        上堂课我讲过，python里变量和函数都是object
                                  ^
    SyntaxError: invalid character in identifier
    



```python
f = abs
f(-9)
```




    9



看，现在f有了abs的功能！既然如此，我们知道，函数本身就是可以作为一个变量。那我们的变量是可以作为另一个函数的参数的，那么一个函数也可以作为另一个函数的参数。

我们来看一个简单的高阶函数：


```python
def add(x, y, f):
    return f(x) + f(y)
```

当我们调用add(-5, 6, abs)时，参数x，y和f分别接收-5，6和abs：


```python
add(-5, 6, abs)
```




    11



# 匿名函数

python 使用 lambda 来创建匿名函数。

- lambda只是一个表达式，函数体比def简单很多。

- lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。

- lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。

- 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

- **最重要的一点**，Lambda表达式可以体现你的逼格。华尔街和伦敦银行高街最逼的一群人都是自诩用且只用函数式编程的。什么是函数式编程？就是类似于全篇程序都用python中lambda这样的一行代码来解决问题。为什么他们逼？因为数学家们学编程的时候，脑子还在数学公式这条线上；他们不会写面对对象编程，只会死想出一条条公式来解决问题；其实这是智商堪忧的体现；但是因为投行基金们很倾向于聘用这群数学家转型的半吊子程序员；他们的使用习惯于是成了圈内高逼的体现；恩，葡萄就是这么酸。:P。

## 语法

Lambda函数的语法只包含一个语句，如下：

lambda [arg1 [,arg2,.....argn]]:expression

比如，我写个相加函数：


```python
sum = lambda arg1, arg2: arg1 + arg2

sum(10, 20)
```




    30



楼上这个，实际上就是一个函数：



```python
def sum(arg1, arg2):
    return arg1 + arg2
```

除了Lambda本身，Python还提供了其他几个辅助工具，让你的函数式代码块更加牛逼：

**reduce**

Python中的reduce内建函数是一个二元操作函数，他用来将一个数据集合(列表，元组等)中的所有数据进行如下操作：传给reduce中的函数func() (必须是一个二元操作函数)先对集合中的第1，2个数据进行操作，得到的结果再与第三个数据用func()函数运算，最后得到一个结果。

顾名思义，reduce就是要把一个list给缩成一个值。所以你必须用二元操作函数。


```python
from functools import reduce

l = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x + y, l))
# 这里代表着，把list中的值，一个个放进lamda的x,y中

# 如果你给出一个初始值，可以放在list后面
print(reduce(lambda x, y: x + y, l, 10))
# 这样，x开始的时候被赋值为10，然后依次
```

    15
    25
    

**map**

map函数应用于每一个可迭代的项，返回的是一个结果list。如果有其他的可迭代参数传进来，map函数则会把每一个参数都以相应的处理函数进行迭代处理。map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。

格式：map(func, seq1[, seq2...] )

Python函数式编程中的map()函数是将func作用于seq中的每一个元素，并用一个列表给出返回值。

map可以使用任何的lambda函数操作，本质上是把原有的list根据lambda法则变成另外一个list


```python
li = [1, 2, 3]
new_list = list(map(lambda i: i+1, li))
print(new_list)
# Py3里，外面需要套个list：
# 这是为了让里面的值给显示出来，要不然你会得到这是个map函数
# 而不是里面的值。
# Py2的童鞋不虚

# 我们也可以把两个数组搞成一个单独的数组
li2 = [4, 5, 6]
new_list = list(map(lambda x, y: x+y, li, li2))
print(new_list)
```

    [2, 3, 4]
    [5, 7, 9]
    

**filter**
filter()函数可以对序列做过滤处理，就是说可以使用一个自定的函数过滤一个序列，把序列的每一项传到自定义的过滤函数里处理，并返回结果做过滤。最终一次性返回过滤后的结果。 和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

语法

filter(func, seq)


```python
li = [100, 20, 24, 50, 110]
new = list(filter(lambda x: x < 50, li))
# 同理，py3得套个list来转化成list函数，便于打印出来
print(new)
```

    [20, 24]
    

熟练运用以上三个玩意儿，你就可以一行写出几乎所有的复杂计算了。

# 装饰器

装饰器就是函数的『包装』：

我们来看一个代码：


```python
def hello(fn):
    def wrapper():
        print("hello, %s" % fn.__name__)
        fn()
        print("goodby, %s" % fn.__name__)
    return wrapper
 
@hello
def foo():
    print("i am foo")
 
foo()
```

    hello, foo
    i am foo
    goodby, foo
    

你可以看到如下的东西：

1）函数foo前面有个@hello的“注解”，hello就是我们前面定义的函数hello

2）在hello函数中，其需要一个fn的参数（这就用来做回调的函数）

3）hello函数中返回了一个inner函数wrapper，这个wrapper函数回调了传进来的fn，并在回调前后加了两条语句。

所以，本质上来讲，用@decorator来装饰某个函数时，其实是做了下面这件事儿：


```python
@decorator
def func():
    pass
```


```python
# 变成 =====》
func = decorator(func)
```

再简单点说，就是把一个函数传到另外一个函数中，再调回给自己。

所以：
**
hello(foo)返回了wrapper()函数，所以，foo其实变成了wrapper的一个变量，而后面的foo()执行其实变成了wrapper()
**
同理，我们也可以搞多个decorator：


```python
@decorator_one
@decorator_two
def func():
    pass

# 相当于：
func = decorator_one(decorator_two(func))
```

你还可以给这个decorator带个参数：


```python
@decorator(arg1, arg2)
def func():
    pass

# 相当于：
func = decorator(arg1,arg2)(func)
```

好了，讲这么多比较复杂，我们来看个网页编程的case:


```python
def makeHtmlTag(tag, *args, **kwds):
    def real_decorator(fn):
        css_class = " class='{0}'".format(kwds["css_class"]) \
                                     if "css_class" in kwds else ""
        def wrapped(*args, **kwds):
            return "<"+tag+css_class+">" + fn(*args, **kwds) + "</"+tag+">"
        return wrapped
    return real_decorator
 
@makeHtmlTag(tag="b", css_class="bold_css")
@makeHtmlTag(tag="i", css_class="italic_css")
def hello():
    return "hello world"
 
print(hello())
```

在上面这个例子中，我们可以看到：makeHtmlTag有两个参数。所以，为了让 hello = makeHtmlTag(arg1, arg2)(hello) 成功，makeHtmlTag 必需返回一个decorator（这就是为什么我们在makeHtmlTag中加入了real_decorator()的原因），这样一来，我们就可以进入到 decorator 的逻辑中去了—— decorator得返回一个wrapper，wrapper里回调hello。

这里插一个知识，我们看到parameters里面有个(\*args, \*\*kwargds)，指的是：
一个星星，指的是这里可以随便放多少个参数，内部提及的时候，当做一个list看。
两个星星指的也是随便多少个参数，但是这里可以带上参数的名字，比如（x='1', y='2'），内部提及的时候，当做一个dict看。

Decorator这个东西，也可以写成class样式：


```python
class myDecorator(object):
    def __init__(self, fn):
        print("inside myDecorator.__init__()")
        self.fn = fn

    def __call__(self):
        self.fn()
        print("inside myDecorator.__call__()")


@myDecorator
def aFunction():
    print("inside aFunction()")


print("Finished decorating aFunction()")

aFunction()
```

这个class样式的看起来比函数样式看着清楚点儿，这样我们再把刚刚的网页编程那段改一下，就得到：


```python
class makeHtmlTagClass(object):
    def __init__(self, tag, css_class=""):
        self._tag = tag
        self._css_class = " class='{0}'".format(css_class) \
            if css_class != "" else ""

    def __call__(self, fn):
        def wrapped(*args, **kwargs):
            return "<" + self._tag + self._css_class + ">" \
                   + fn(*args, **kwargs) + "</" + self._tag + ">"

        return wrapped


@makeHtmlTagClass(tag="b", css_class="bold_css")
@makeHtmlTagClass(tag="i", css_class="italic_css")
def hello(name):
    return "Hello, {}".format(name)


print(hello("Baby"))
```

    <b class='bold_css'><i class='italic_css'>Hello, Baby</i></b>
    

**装饰器的副作用：**

因为decorator的因素，我们原本的函数其实已经变成了一个叫wrapper函数。

比如，你再调用\_\_name\_\_的时候，他会告诉你，这是 wrapper, 而不是 foo 或者 hello。

当然，虽然功能效果不变，但是有些处女座的童鞋会觉得很不爽。

所以，Python 的 functool 包中提供了一个叫 wrap 的 decorator 来消除这样的副作用：


```python
from functools import wraps


def hello(fn):
    @wraps(fn)
    def wrapper():
        print("hello, %s" % fn.__name__)
        fn()
        print("goodby, %s" % fn.__name__)

    return wrapper


@hello
def foo():
    '''foo help doc'''
    print("i am foo")
    pass


foo()
print(foo.__name__)
print(foo.__doc__)
```

    hello, foo
    i am foo
    goodby, foo
    foo
    foo help doc
    

来个经典例子：

斐波那契数列递归法：


```python
from functools import wraps


def memo(fn):
    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result

    return wrapper


@memo
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

我们知道，这个递归是相当没有效率的，因为会重复调用。比如：我们要计算fib(5)，于是其分解成fib(4) + fib(3)，而fib(4)分解成fib(3)+fib(2)，fib(3)又分解成fib(2)+fib(1)…… 你可看到，基本上来说，fib(3), fib(2), fib(1)在整个递归过程中被调用了两次。

而我们用decorator，在调用函数前查询一下缓存，如果没有才调用了，有了就从缓存中返回值。一下子，这个递归从二叉树式的递归成了线性的递归。

# 偏函数

Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。

偏函数又可以翻译成部分函数，大概意思就是说，只设置一部分参数。

举个例子，我们知道int()可以把字符串变成十进制数字：


```python
int('12345')
```




    12345



但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：


```python
int('12345', base=8)
```




    5349




```python
int('12345', 16)
```




    74565



假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：


```python
def int2(x, base=2):
    return int(x, base)
```

这样，我们转换二进制就非常方便了：


```python
int2('1000000')
```




    64



functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：


```python
import functools

int2 = functools.partial(int, base=2)
int2('1000000')
```




    64



所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值：


```python
int2('1000000', base=10)
```




    1000000



最后，创建偏函数时，实际上可以接收函数对象、\*args和\*\*kw这3个参数，当传入：


```python
int2 = functools.partial(int, base=2)
int2('10010')
```




    18




```python
实际上固定了int()函数的关键字参数base。

同理：我们刚刚说的**可以当成一个dict带入
```


      File "<ipython-input-66-d6459545d34d>", line 1
        实际上固定了int()函数的关键字参数base。
                               ^
    SyntaxError: invalid character in identifier
    



```python
kw = {'base': 2}
int('10010', **kw)
```




    18



继续同理，我们可以用*把一个list塞进来


```python
max2 = functools.partial(max, 10)

max2(5, 6, 7)
```




    10



相当于：


```python
args = (10, 5, 6, 7)
max(*args)
```




    10



注意，10在最左边。

# 实战：

今天的课程实践会结合上节课给你们的代码内容。

上节课我们讲了如果写个Dataset类来帮我们下载和处理数据。

这节课我们学习了文本的读入，那我们就来做做更加复杂的内容：

本节课的压缩包里有一个数据文件，是我们今天实战的数据。

这是美国亚利桑那州Pima印第安女人患有糖尿病状况的数据集（因为他们的得病率很高）。

这个数据是一个txt文件（其实是个csv），每一行就是一个数据条，长这样：

6,148,72,35,0,33.6,0.627,50,1

1,85,66,29,0,26.6,0.351,31,0

8,183,64,0,0,23.3,0.672,32,1

1,89,66,23,94,28.1,0.167,21,0

0,137,40,35,168,43.1,2.288,33,1

其中，前面N-1个数据，分别是一些身体的指标，比如：血压，血糖，身高，是否怀孕等等。 最后第N个数据点是记录她是否患有糖尿病，它只有0或者1两种可能。这也就是我们说的数据标签。

所以，这里我们脑海中应该浮现的数据结构如下：

x = [

[6,148,72,35,0,33.6,0.627,50],

[1,85,66,29,0,26.6,0.351,31],

[8,183,64,0,0,23.3,0.672,32],

...

]

y = [1,0,1,0,1,1,1,0,...]

所以，这是一个二元分类问题。

参照上一堂课的内容，我们要做如下的修改：

1.Dataset这个类中的download_data函数要被修改，改成我们从外部读入数据的过程。并且要把我们的x和y分开储存，并返回。

2.我们这次依旧是以0.7的比率分开训练集和测试集。当我们得到区分开的 x_train, x_test, y_train, y_test以后，我们把这些个数据分别用Json或者Pickle的方法序列化在我们文件夹内。然后我们新建一个程序，从中反序列化我们处理好的数据。并进行之后的Machine Learning过程。

3.当我们把一个model训练好以后，我们代入全部的x_test数据，并得到我们预测出来的分类值y_preds。我们把这个值(list)与我们的y_test相互比较，用一些正确率统计的方法计算我们model的准确率，并用lambda函数来实现

预测数据的直接准确率怎么计算？

准确率 = (对的数据数 / 全部数据数) * 100%

高级一点，

我们可以再实现一点其他准确率计算方式：

AUC，MSE，...

详情可见附录的cheat sheet，或者自行百度。

OK！

自己动手尝试一下吧！

么么哒！

参考资料：七月在线课程
