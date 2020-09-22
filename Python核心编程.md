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

