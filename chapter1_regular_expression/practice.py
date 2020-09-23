import re

# s="i love you not because of who you are, but because of who i am when i am with you"
#
# content=re.findall(r"\b\w+\b",s)

# 2、匹配一行文字中的所有开头的数字内容

# import re
#
# s = "i love you not because 12sd 34er 56df e4 54434"
# content = re.findall(r'\b\d',s)

# 3、匹配一行文字中的所有开头的数字内容或数字内容
# s = "123sdf"
# m = re.match('\w+', s)

# 4、 只匹配包含字母和数字的行

# coding=utf-8


# import re
#
# s = "i love you not because\n12sd 34er 56\ndf e4 54434"
# content = re.findall('.*\n|.*', s, re.M)
#
# import re
# patt = '\w+@(qq|gmail)\.com'
# s = 'my email is 631707329@qq.com'
# r = re.findall(patt, s)

# 1、匹配一个0-9之间任意数字(3位数)

# import re
# s1=s2="""192.168.1.150\n0.0.0.0\n255.255.255.255\n17.16.52.100\n172.6.0.001\n400.400.999.888\n001.022.003.000\n257.257.255.256"""
#
# regex2=re.compile(r'(?:(?:(?:25[0-5])|(?:24[0-9])|(?:1\d{2})|(?:[1-9][0-9])|(?:[0-9]))\.){3}(?:(?:25[0-5])|(?:1\d{2})|(?:[1-9][0-9])|(?:[0-9]\b))')
# t=regex2.findall(s1)
# print(t)


# # 3、选出含有ftp的链接，且文件类型是gz或者xz的文件名
#
# s3="""
# ftp://ftp.astrom.com/pub/file/file-5.14.tar.gz
# ftp://ftp.gmplib.org/pub/gmp-5.1.0/gmp-5.1.00tar.xz
# ftp://ftp.gmplib.org/pub/gmp-5.1.0/gmp-5.1.00tar.xd
# ftp://ftp.vim,org/pub/vim/unix/vim-7.3.tar.ba2
# http://anduin.linuxfromscratch.org/sources/LFS/lfs-packages/conglomeration//iana-etc/iana-etc-2.30.tar.bz2
# http://anduin.linuxfromscratch.org/sources/other/udev-lfs-205-1.tar.bz2
# http://download.savannah.gnu.org/releases/libpipeline/libpipeline-1.2.4.tar.gz
# http://download.savannah.gnu.org/releases/man-db/man-db-2.6.5.tar,xz
# http://download.savannah.gnu.org/releases/sysvinit/sysvinit-2.88dsf.tar.bz2
# http://ftp.altlinux.org/pub/people/legion/kbd-1.15.5.tar.gz
# http://mirror.hust.edu.cn/gnu/antoconf/autoconf-2.69.tar.gz
# http://mirror.hust.edu.cn/gnu/antomake/automake-2.69.tar.gz
# """
#
# patt = r'(?:ftp://(?:\w+\.){1,2}\w+(?:/.+)+)\.(?:gz|xz)'
# cont = re.findall(patt, s3)
# print(cont)

# 4、匹配邮箱

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