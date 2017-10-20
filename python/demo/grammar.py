#!/usr/bin/env python3  #告诉unix服务器这是一个Python可执行程序

# -*- coding: utf-8 -*-  #告诉Python解释器，按照UTF-8编码读取源代码

#python原样字符串输出用r''

#python字符串换行除了用\n外还可以用'''...'''

#python有整数、浮点数、字符串、布尔类型、宿舍(None)

#python在不声明变量类型的时候可以先赋值为整数再赋值为字符串，如果在声明的时候指定类型以后就不可以这样做了

#python中/表示除法，结果是浮点数，//表是除法结果是整数

#ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符

#python中的list类型可以认为是一个数组，用[]来初始化；len()得到list元素的个数
#list可以用负数来访问，-1访问的是最后一个，依次类推
#list.append('Adam')向末尾追加元素
#list.insert(1, 'Jack')向第一个插入元素，之后的向后移动一位
#list.pop()默认删除最后一个元素，加上int参数删除相应的元素
#list[int]=''修改相应的元素信息
#list.sort()可以进行排序

#python中的tuple跟list一样用()来初始哗，旦初始化就不能修改

#python中使用global声明变量代表的就是一个全局变量，或者在单独的模块中定义好将定义的全局变量模块导入
#SOLR_URL='http://www.baidu.com'

#def tt():
#	global SOLR_URL
#	SOLR_URL+="#aaa"

#if __name__=='__main__':
#	tt()
#	print(SOLR_URL)
#python中是先局部再全局


#python所有的流程语句开始的每一句后要加:号

#if age >= 18:
	#print('')
#elif age >=6
	#print('')
#else:
	#print('')

#if的条件判断还可以简写为if x:  其中只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
#if L is None:  判断一个变量是否为None值

#int()用来把字符串转换为整数

#range()可以生成一个序列
#for x in ...循环就是把每个元素代入变量x中，然后执行缩进块语句
#while x>0  只要条件满足，就不断循环，条件不满足时退出循环

#dic字典类型d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# if 'Thomas' in d  用来判断Key是否存在   还可以通过通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
#要删除一个key，用pop(key)方法

#set与dict类型，只是一组Key集合由于key不能重复，所以，在set中，没有重复的key
#add(key)可以添加元素到set中   通过remove(key)方法可以删除元素
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作 s1 & s2  s1 | s2

#replace()返回替换后的字符串

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
#a=abs
#a(-1)
#其中abs就是一个函数

#定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回
#如果没有return语句，函数执行完毕后也会返回结果，只是结果为None
#return None可以简写为return

#def power(x, n):  x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n
#def power(x, n=2):  n是默认参数，调用的时候可以不用传
#默认参数可以简化函数的调用。但要注意：必选参数在前，默认参数在后；
#enroll('Adam', 'M', city='Tianjin') 这里city指的是形参的名字
#要注意的是Python函数在定义的时候，默认参数的值就被计算出来了
#def calc(*numbers):  其中*numbers是可变参数，calc(1, 3, 5, 7)可以这样调用，如果调用时传入一个数组加以前面加一个*号
#def person(name, age, **kw): 定义了一个关键字参数，person('Michael', 30)，person('Bob', 35, city='Beijing')，person('Adam', 45, gender='M', job='Engineer')extra = {'city': 'Beijing', 'job': 'Engineer'};person('Jack', 24, city=extra['city'], job=extra['job'])或person('Jack', 24, **extra)调用
#关键字参数扩展函数的功能，关键字参数可以理解为dict类型
#def person(name, age, *, city, job):  命名关键字参数，和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符* 这样person的关键字参数只能是city与job
#def f1(a, b, c=0, *args, **kw):  可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用;但是参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

#python的切片用法跟golang是一样的，不同的是可以使用负数索引

#迭代dict   for key in d:  默认是迭代key，迭代values：for value in d.values()；迭代key和value：or k, v in d.items()
#from collections import Iterable 里的Iterable类型来判断是否可以迭代：isinstance('abc', Iterable)
#对list实现有下标的迭代：for i, value in enumerate(['A', 'B', 'C']):  Python内置的enumerate函数可以把一个list变成索引-元素
#or循环里，同时引用了两个变量：for x, y in [(1, 1), (2, 4), (3, 9)]:

#列表生成式可以用一行语句代替循环生成；[x * x for x in range(1, 11)] 结果是：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#[x * x for x in range(1, 11) if x % 2 == 0] 结果是：[4, 16, 36, 64, 100]
#[m + n for m in 'ABC' for n in 'XYZ'] 结果是：['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

#import os
#print([d for d in os.listdir("../../../")])
#列出指定目录下的文件和目录

#d = {'x': 'A', 'y': 'B', 'z': 'C' }
#print([k + '=' + v for k, v in d.items()])
#列表生成式也可以使用两个变量来生成list，每次生成list输出信息会不一样

#for k,v in d.items():
#	print(k,v)
#每次打印的顺序不一样

#生成器：要创建一个generator(generator保存的是算法,generator也是可迭代对象)，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
#g = (x * x for x in range(10))
#创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator
#可以通过next()函数获得generator的下一个返回值
#g = (x * x for x in range(10))
#for n in g:
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
#generator和函数的执行流程不一样,在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
#但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中

#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator;把list、dict、str等Iterable变成Iterator可以使用iter()函数
#Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

#函数本身也可以赋值给变量，即：变量可以指向函数

#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

#reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

#filter()和map()类似,也接收一个函数和一个序列;把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素

#sorted()函数就可以对list进行排序:sorted([36, 5, -12, 9, -21])
#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序:sorted([36, 5, -12, 9, -21], key=abs)
#忽略大小写排序：sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
#反射排序：sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

#list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
#关键字lambda表示匿名函数，冒号前面的x表示函数参数,就是只能有一个表达式，不用写return，返回值就是该表达式的结果

#函数对象有一个__name__属性，可以拿到函数的名字 now.__name__

#装饰器
#def log(func):
#    def wrapper(*args, **kw):
#        print('call %s():' % func.__name__)
#        return func(*args, **kw)
#    return wrapper
#
#@log
#def now():
#    print('2015-3-25')

#now()
#由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数
#wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
#import functools
#def log(text):
#    def decorator(func):
#		 @functools.wraps(func)  #如果不加则调用—__name__时返回的是wrapper
#        def wrapper(*args, **kw):
#            print('%s %s():' % (text, func.__name__))
#            return func(*args, **kw)
#        return wrapper
#    return decorator


#@log('execute')
#def now():
#    print('2015-3-25')

#now()



#偏函数：functools.partial就是帮助我们创建一个偏函数，作用是把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
#import functools
#int2 = functools.partial(int, base=2)
#int2('1000000')
#当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。


#一个.py文件就称之为一个模块（Module），可以通过包来组织模块，避免冲突。
#每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是目录名。
#自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。
#任何模块代码的第一个字符串都被视为模块的文档注释
#' 这是第一行，用于模块的文档注释 ' #这就是一个模块的文档注释
#__author__变量把作者写进去
#__author__ = '这个写模块的作者'
#在内置的sys模块里有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，第一个参数永远是该.py文件的名称
#当在单独运行一个模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该模块时这个变量就不是__main__了。

#作用域：正常的函数和变量名是公开的（public），可以被直接引用。类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量。模块定义的文档注释也可以用特殊变量__doc__访问。
#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用；private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。
#在Python中，安装第三方模块，是通过包管理工具pip完成的。

#在Python中，定义类是通过class，关键字class后面紧接着是类名，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的；如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
#创建类实例是通过类名+()实现的
#在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法。
#__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
#有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去。
#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
#和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同。
#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问。
#在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

#bart = Student('Bart Simpson', 98)
#bart.get_name()
#bart.__name = 'New Name'
#bart.__name
#表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。

#判断一个变量是否是某个类型可以用isinstance()判断
#在Python中pass是空语句，是为了保持程序结构的完整性。pass 不做任何事情，一般用做占位语句。

#我们来判断对象类型，使用type()函数。
#type(123)==type(456)  #比较两个变量类型是否相等
#type('abc')==str  #判断是否是字符串，判断基本数据类型可以直接写int，str等；
#types模块中定义的常量可以判断一个对象是否是函数
#type(fn)==types.FunctionType
#type(abs)==types.BuiltinFunctionType
#type(lambda x: x)==types.LambdaType
#type((x for x in range(10)))==types.GeneratorType
#能用type()判断的基本类型也可以用isinstance()判断，并且还可以判断一个变量是否是某些类型中的一种

#isinstance([1, 2, 3], (list, tuple))
#isinstance((1, 2, 3), (list, tuple))
#判断是否是list或者tuple

#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list


#实例属性与类属性
#>>> class Student(object):
#     name = 'Student'

#>>> s = Student() # 创建实例s
#>>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
#Student
#>>> print(Student.name) # 打印类的name属性
#Student
#>>> s.name = 'Michael' # 给实例绑定name属性
#>>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
#Michael
#>>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
#Student
#>>> del s.name # 如果删除实例的name属性
#>>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了


#在python中可以通过types的MethodType给对象动态绑定一个方法，但是给一个对象绑定的方法，对另一个实例是不起作用的；

#为了给所有实例都绑定方法，可以给class绑定方法
#def set_score(self, score):
#	pass
#Student.set_score = set_score

#使用__slots__可以对类的实例限制属性
#class Student(object):
#    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
#Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性


#Python内置的@property装饰器就是负责把一个方法变成属性调用的
#class Student(object):

#    @property
#    def score(self):
#        return self._score

#    @score.setter
#    def score(self, value):
#        if not isinstance(value, int):
#            raise ValueError('score must be an integer!')
#        if value < 0 or value > 100:
#            raise ValueError('score must between 0 ~ 100!')
#        self._score = value


#s = Student()
#s.score = 60 # OK，实际转化为s.set_score(60)
#s.score # OK，实际转化为s.get_score()


#class Student(object):

#    @property
#    def birth(self):
#        return self._birth

#    @birth.setter
#    def birth(self, value):
#        self._birth = value

#    @property  #age是个只读属性
#    def age(self):
#        return 2015 - self._birth


#python支持多重继承，通过多重继承，一个子类就可以同时获得多个父类的所有功能。
#class Bat(Mammal, Flyable):
#    pass
#多重继承每个父用类逗号隔开
#在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
#在类里__len__()方法是为了能让class作用于len()函数。
#在类里__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的；同理__str__()与__repr__()可以通过print(Student('Michael'))与s调用
#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
#class Fib(object):
#    def __init__(self):
#        self.a, self.b = 0, 1 # 初始化两个计数器a，b

#    def __iter__(self):
#        return self # 实例本身就是迭代对象，故返回自己

#    def __next__(self):
#        self.a, self.b = self.b, self.a + self.b # 计算下一个值
#        if self.a > 100000: # 退出循环的条件
#            raise StopIteration()
#        return self.a # 返回下一个值


#for n in Fib():
#	print(n)

#Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素会报错
#要表现得像list那样按照下标取出元素，需要实现__getitem__()方法，__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice；
#class Fib(object):
#    def __getitem__(self, n):
#        if isinstance(n, int): # n是索引
#            a, b = 1, 1
#            for x in range(n):
#                a, b = b, a + b
#            return a
#        if isinstance(n, slice): # n是切片
#            start = n.start
#            stop = n.stop
#            if start is None:
#                start = 0
#            a, b = 1, 1
#            L = []
#            for x in range(stop):
#                if x >= start:
#                    L.append(a)
#                a, b = b, a + b
#            return L



#f = Fib()
#f[0:5]
#如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
#与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。


#__getattr__  可以动态调用一个不存在的属性
#class Student(object):

#    def __init__(self):
#        self.name = 'Michael'

#    def __getattr__(self, attr):
#        if attr=='score':
#            return 99

#		 if attr=='age':
#            return lambda: 25 #返回一个函数

#		 raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)



#只有在没有找到属性的情况下，才调用__getattr__，已有的属性
#注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误

#__call__()方法可以直接对实例进行调用
#class Student(object):
#    def __init__(self, name):
#        self.name = name

#    def __call__(self):
#        print('My name is %s.' % self.name)


#s = Student('Michael')
#s()
#__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
#判断一个对象是否能被调用，能被调用的对象就是一个Callable对象。通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
#callable(Student())

#Python提供了Enum类来实现枚举
#from enum import Enum
#Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#for name, member in Month.__members__.items():
#    print(name, '=>', member, ',', member.value)
#以上是列举枚举所有成员
#value属性则是自动赋给成员的int常量，默认从1开始计数。
#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
#from enum import Enum, unique

#@unique
#class Weekday(Enum):
#    Sun = 0 # Sun的value被设定为0
#    Mon = 1
#    Tue = 2
#    Wed = 3
#    Thu = 4
#    Fri = 5
#    Sat = 6

#@unique装饰器可以帮助我们检查保证没有重复值。
#访问这些枚举类型可以有若干种方法：
#day1 = Weekday.Mon
#print(day1)
#Weekday.Mon
#>>> print(Weekday.Tue)
#Weekday.Tue
#>>> print(Weekday['Tue'])
#Weekday.Tue
#>>> print(Weekday.Tue.value)
#2
#>>> print(day1 == Weekday.Mon)
#True
#>>> print(day1 == Weekday.Tue)
#False
#>>> print(Weekday(1))
#Weekday.Mon
#>>> print(day1 == Weekday(1))
#True
#>>> Weekday(7)
#Traceback (most recent call last):
#  ...
#ValueError: 7 is not a valid Weekday
#>>> for name, member in Weekday.__members__.items():
#		print(name, '=>', member)


#type()函数可以查看一个类型或变量的类型
#type()函数既可以返回一个对象的类型，又可以创建出新的类型
#>>> def fn(self, name='world'): # 先定义函数
#        print('Hello, %s.' % name)

#>>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
#>>> h = Hello()
#>>> h.hello()
#Hello, world.
#>>> print(type(Hello))
#<class 'type'>
#>>> print(type(h))
#<class '__main__.Hello'>
#要创建一个class对象，type()函数依次传入3个参数：
#1、class的名称；
#2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
#通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。



# metaclass是类的模板，所以必须从`type`类型派生：
#class ListMetaclass(type):
#	def __new__(cls,name,bases,attrs):
#		attrs["add"]=lambda self,value:self.append(value)
#		return type.__new__(cls,name,bases,attrs)
		

#有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass
#class MyList(list,metaclass=ListMetaclass):
#	pass
		
#L=MyList()
#L.add(1)
#print(L)
#指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
#metaclass可以看作是类的模板，在写orm框架时属性这块可以用到

#python中的异常处理
#try:
#	...
#except ... as ... e:
#	...
#else:  #当没有发生异常的时候执行这里的代码
#	...
#finally:
#	...

#Python内置的logging模块可以非常容易地记录错误信息
#try:
#    bar('0')
#except Exception as e:
#    logging.exception(e)

#用raise语句抛出一个错误的实例
#def foo(s):
#    n = int(s)
#    if n==0:
#        raise FooError('invalid value: %s' % s)
#    return 10 / n

#raise语句如果不带参数，就会把当前错误原样抛出
#def bar():
#    try:
#        foo('0')
#    except ValueError as e:
#        print('ValueError!')
#        raise

#在except中raise一个Error，还可以把一种类型的错误转化成另一种类型
#try:
#    10 / 0
#except ZeroDivisionError:
#    raise ValueError('input error!')
#只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError

#断言
#def foo(s):
#    n = int(s)
#    assert n != 0, 'n is zero!'
#    return 10 / n

#def main():
#    foo('0')
#启动Python解释器时可以用-O参数来关闭assert
#python3 -O err.py

#日志logging：和assert比，logging不会抛出错误，而且可以输出到文件；需要导入import logging
#允许你指定记录信息的级别，有debug，info，warning，error等几个级别
# python3 -m pdb err.py #pdb可以进行调试，一般用ide进行调试，一般用PyCharm这个ide


#读写文件
#f = open('/Users/michael/test.txt', 'r')  #把开一个文件，r表示读,如果文件不存在，就会有一个IOError异常
#f.read()  #把内容一次性读出来
#f.close()  #关闭文件
#使用with语句就可以不用显示调用close()方法
#with open('/path/to/file', 'r') as f:
#    print(f.read())
#read(size)每次最多读取size个字节的内容。readline()可以每次读取一行内容，readlines()一次读取所有内容并按行返回list
#for line in f.readlines():
#    print(line.strip()) # 把末尾的'\n'删掉
#f = open('/Users/michael/test.jpg', 'rb')  #要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
#f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')   #读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
#f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')  #编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略
#f = open('/Users/michael/test.txt', 'w')  #写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
#要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码


#Python内置的os模块也可以直接调用操作系统提供的接口函数
#>>> import os
#>>> os.name # 操作系统类型
#'posix'  #posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
#要获取详细的系统信息，可以调用uname()函数
#>>> os.uname()
#posix.uname_result(sysname='Darwin', nodename='MichaelMacPro.local', release='14.3.0', version='Darwin Kernel Version 14.3.0: Mon Mar 23 11:59:05 PDT 2015; root:xnu-2782.20.48~5/RELEASE_X86_64', machine='x86_64')
#uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的
#操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看；
#要获取某个环境变量的值，可以调用os.environ.get('key')


#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
# 查看当前目录的绝对路径:
#>>> os.path.abspath('.')
#'/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
#>>> os.path.join('/Users/michael', 'testdir')
#'/Users/michael/testdir'
# 然后创建一个目录:
#>>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
#>>> os.rmdir('/Users/michael/testdir')
#要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
#>>> os.path.split('/Users/michael/testdir/file.txt')
#('/Users/michael/testdir', 'file.txt')
#os.path.splitext()可以直接让你得到文件扩展名
#>>> os.path.splitext('/path/to/file.txt')
#('/path/to/file', '.txt')
#合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作
# 对文件重命名:
#>>> os.rename('test.txt', 'test.py')
# 删掉文件:
#>>> os.remove('test.py')
#列出当前目录下的所有目录
#>>> [x for x in os.listdir('.') if os.path.isdir(x)]
#['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]
#列出所有的.py文件
#>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
#['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']
#shutil模块提供了copyfile()的函数来复制文件


#把变量从内存中变成可存储或传输的过程称之为序列化，Python中pickling就是序列化；反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling；

#>>> import pickle
#>>> d = dict(name='Bob', age=20, score=88)
#>>> pickle.dumps(d)
#b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq\x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'
#pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
#>>> f = open('dump.txt', 'wb')
#>>> pickle.dump(d, f)
#>>> f.close()
#当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象
#>>> f = open('dump.txt', 'rb')
#>>> d = pickle.load(f)
#>>> f.close()
#>>> d
#{'age': 20, 'score': 88, 'name': 'Bob'}


#Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
#>>> import json
#>>> d = dict(name='Bob', age=20, score=88)
#>>> json.dumps(d)
#'{"age": 20, "score": 88, "name": "Bob"}'
#dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object
#要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
#>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
#>>> json.loads(json_str)
#{'age': 20, 'score': 88, 'name': 'Bob'}


#Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类
#import json

#class Student(object):
#    def __init__(self, name, age, score):
#        self.name = name
#        self.age = age
#        self.score = score

#def student2dict(std):
#    return {
#        'name': std.name,
#        'age': std.age,
#        'score': std.score
#    }

#def dict2student(d):
#    return Student(d['name'], d['age'], d['score'])

#s = Student('Bob', 20, 88)
#print(json.dumps(s, default=student2dict))
#dumps()方法还提供了一个可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可。也可以用以下方式
#print(json.dumps(s, default=lambda obj: obj.__dict__))
#通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class
#把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例
#>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
#>>> print(json.loads(json_str, object_hook=dict2student))

#Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
#子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
#Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程
#import os

#print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
#pid = os.fork()
#if pid == 0:
#    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
#else:
#    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


#python提供了multiprocessing就是跨平台版本的多进程模块
#multiprocessing模块提供了一个Process类来代表一个进程对象
#from multiprocessing import Process
#import os

# 子进程要执行的代码
#def run_proc(name):
#    print('Run child process %s (%s)...' % (name, os.getpid()))

#if __name__=='__main__':
#    print('Parent process %s.' % os.getpid())
#    p = Process(target=run_proc, args=('test',))
#    print('Child process will start.')
#    p.start()
#    p.join()
#    print('Child process end.')
#创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。


#如果要启动大量的子进程，可以用进程池的方式批量创建子进程，pool
#from multiprocessing import Pool
#import os, time, random

#def long_time_task(name):
#    print('Run task %s (%s)...' % (name, os.getpid()))
#    start = time.time()
#    time.sleep(random.random() * 3)
#    end = time.time()
#    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

#if __name__=='__main__':
#    print('Parent process %s.' % os.getpid())
#    p = Pool(4)
#    for i in range(5):
#        p.apply_async(long_time_task, args=(i,))
#    print('Waiting for all subprocesses done...')
#    p.close()
#    p.join()
#    print('All subprocesses done.')
#对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了

#很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出
#subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出
#import subprocess

#print('$ nslookup www.python.org')
#r = subprocess.call(['nslookup', 'www.python.org'])
#print('Exit code:', r)


#Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据
#from multiprocessing import Process, Queue
#import os, time, random

# 写数据进程执行的代码:
#def write(q):
#    print('Process to write: %s' % os.getpid())
#    for value in ['A', 'B', 'C']:
#        print('Put %s to queue...' % value)
#        q.put(value)
#        time.sleep(random.random())

# 读数据进程执行的代码:
#def read(q):
#    print('Process to read: %s' % os.getpid())
#    while True:
#        value = q.get(True)
#        print('Get %s from queue.' % value)

#if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
#    q = Queue()
#    pw = Process(target=write, args=(q,))
#    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
#    pw.start()
    # 启动子进程pr，读取:
#    pr.start()
    # 等待pw结束:
#    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
#    pr.terminate()
#在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，所有，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。


#python多线程有两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块
#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
#import time, threading

# 新线程执行的代码:
#def loop():
#    print('thread %s is running...' % threading.current_thread().name)
#    n = 0
#    while n < 5:
#        n = n + 1
#        print('thread %s >>> %s' % (threading.current_thread().name, n))
#        time.sleep(1)
#    print('thread %s ended.' % threading.current_thread().name)

#print('thread %s is running...' % threading.current_thread().name)
#t = threading.Thread(target=loop, name='LoopThread')
#t.start()
#t.join()
#print('thread %s ended.' % threading.current_thread().name)
#由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……


#多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
#balance = 0
#lock = threading.Lock()

#def run_thread(n):
#    for i in range(100000):
        # 先要获取锁:
#        lock.acquire()
#        try:
            # 放心地改吧:
#            change_it(n)
#        finally:
            # 改完了一定要释放锁:
#            lock.release()
#以上是线和锁的使得


#在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。
#要共享对象可以用ThreadLocal
#import threading

# 创建全局ThreadLocal对象:
#local_school = threading.local()

#def process_student():
    # 获取当前线程关联的student:
#    std = local_school.student
#    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

#def process_thread(name):
    # 绑定ThreadLocal的student:
#    local_school.student = name
#    process_student()

#t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
#t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
#t1.start()
#t2.start()
#t1.join()
#t2.join()
#全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
#ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
#一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题


#Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。
#multiprocessing可以很容易地编写分布式多进程程序。





























