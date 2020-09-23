# 一、正则表达式

## · re模块

### 1. 匹配对象方法

#### 1.1 group

##### a. 根据组编号索引

```python
# group(num=0)

import re
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
# group()等同于group(0)
g0 = m.group(0) # 或者m[0]
g1 = m.group(1) # 或者m[1]
g2 = m.group(2) # 或者m[2]
for i, g in enumerate((g0, g1, g2)):
    print('g{} [content: {}, type: {}]'.format(i, g, type(g)))
'''
g0 [content: Isaac Newton, type: <class 'str'>]
g1 [content: Isaac, type: <class 'str'>]
g2 [content: Newton, type: <class 'str'>]
'''

print(m.group(0,1,2))
'''
('Isaac Newton', 'Isaac', 'Newton')
'''
```

返回一个或者多个匹配的子组。如果只有一个参数，结果就是一个字符串（组之间以空格隔开），如果有多个参数，结果就是一个元组（每个参数对应一个项），如果没有参数或者参数为0(默认0)，（整个匹配都被返回）。如果它是一个范围 [1..99]，结果就是相应的括号组字符串。如果一个组号是负数，或者大于样式中定义的组数，一个 [`IndexError`](https://docs.python.org/zh-cn/3/library/exceptions.html#IndexError) 索引错误就 `raise`。

如果一个组包含在样式的一部分，并被匹配多次，就返回最后一个匹配。:

```python
import re

m = re.match(r"(..)+", "a1b2c3")  # Matches 3 times.
m.group(1)

'''
m
<re.Match object; span=(0, 6), match='a1b2c3'>
m.group(1)
'c3'
'''
```



##### b. 根据组名索引

命名：?P\<name\>

格式：(?P\<name\>正则匹配模式)

放到括号外面会报错

示例：

```python
import re

x = "abc <haha,123> test @@"
pattern = "(?P<test>\<\w+,\d+\>)"
m = re.search(pattern, x)
# 根据组名索引
r = m.group("test")
print (r)
'''<haha,123>'''
```

命名之后依然可以用id索引



#### 1.2 groups

以元组的形式返回参与匹配的所有组匹配的字符串，若该组没有匹配，则返回给定默认参数值，

参数默认为None，也可自己指定。如果所有组没有匹配的，会返回空元组()，此时给定参数不起作用，详见下面示例

```python
import re
m = re.match(r"(\d+)\.(\d+)", "24.1632")
m.groups()
'''
m.groups()
('24', '1632')
'''


m = re.match(r"(\d+)\.?(\d+)?", "24")
>>> m.groups()      # Second group defaults to None.
('24', None)
>>> m.groups('0')   # Now, the second group defaults to '0'.
('24', '0')


# 返回空元祖的情况
m = re.match(r"aa(\d*)\.?(\d*)?", "aa")
m.groups()
('', '')
m.groups(1)
('', '')

```

#### 1.3 groupdict(default=None)

未参与匹配的分组value为空串

```python
import re
m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
m.groupdict()
{'first_name': 'Malcolm', 'last_name': 'Reynolds'}

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w*)", "Malcolm ")
m.groupdict()
{'first_name': 'Malcolm', 'last_name': ''}

```

### 2. 常用正则匹配例子

#### 2.1 匹配所有单词

```python
import re

s="my love you not because of who you are, but because of who i am when i am with you"

content=re.findall(r" *(\w+)",s)
# 或者
content=re.findall(r"\b\w+\b",s)
```

#### 2.2 (?:)

在分组前加上?:不会产生分组

示例

```python
import re
patt = '\w+@(?:qq|gmail)\.com'
s = 'my email is 631707329@qq.com'
r = re.findall(patt, s)
# ['631707329@qq.com']

patt = '\w+@(qq|gmail)\.com'
r = re.findall(patt, s)
# ['qq']
```



#### 2.3 匹配IPv4地址

```python
import re
s1=s2="""192.168.1.150\n0.0.0.0\n255.255.255.255\n17.16.52.100\n172.6.0.001\n400.400.999.888\n001.022.003.000\n257.257.255.256"""

regex2=re.compile(r'(?:(?:(?:25[0-5])|(?:24[0-9])|(?:1\d{2})|(?:[1-9][0-9])|(?:[0-9]))\.){3}(?:(?:25[0-5])|(?:1\d{2})|(?:[1-9][0-9])|(?:[0-9]\b))')
t=regex2.findall(s1)
print(t)
# ['192.168.1.150', '0.0.0.0', '255.255.255.255', '17.16.52.100']
```



#### 2.4 匹配邮箱

```python
import re

s4="""
test@hot-mail.com
v-ip@magedu.com
web.manager@magedu.com.cn
super.user@google.com
a@w-a-com
"""

patt = r'.*@(?:.*\.)+(?:com|cn)'
cont = re.findall(patt, s4)
print(cont)
# ['test@hot-mail.com', 'v-ip@magedu.com', 'web.manager@magedu.com.cn', 'super.user@google.com']
```



### 3 注意事项

#### 3.1 \b 边界的使用

由于该符号属于特殊字符与asc码冲突，使用时在模式字符串前加上r,其他特使字符类似

```python
import re
patt = r'\b\w+\b'
re.findall(patt, '')
```

