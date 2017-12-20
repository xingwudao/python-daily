#!/anaconda/bin/python

from progress.bar import Bar


'''Bar是进度条中的基础类
基本上已经能够满足进度要求了，当然也可以基于它派生出一些自己的奇葩需求。
Bar的初始化参数有：
1. 进度条说明
2. 进度条填充字符，你可以用任意slogan作为进度条字符，比如中文，默认是#
3. 进度条最大值

包里面预定义了几种Bar：
ChargingBar
FillingSquaresBar
FillingCirclesBar
IncrementalBar
PixelBar
ShadyBar
 
都是针对预先知道执行步数的进度显示情况，显示风格不同
'''
print('Bar demo.\n\n')

max_range = 10000
bar = Bar('Processing', fill = '刀', max=max_range)
for i in range(max_range):
    # Do some work
    bar.next()
bar.finish()

'''自定义一种Bar
'''

class MyBar(Bar):
    message = 'mybar is working'
    fill = '刀'
    suffix = '%(percent).1f%% - %(eta)ds'

max_range = 100000
mybar = MyBar(max = max_range)
for i in range(max_range):
    mybar.next()
mybar.finish()


'''不知道到进度终点的执行步数时用spinner类
呈现的就不是进度条，而是一个等待的字符标识

包里面预定义了几种Spinner：
Spinner
PieSpinner
MoonSpinner
LineSpinner
PixelSpinner
'''
from progress.spinner import Spinner

print('Spinner demo.\n\n')
max_range = 10000
spinner = Spinner('Computing.')
while max_range > 0:
    max_range -= 1
    spinner.next()

spinner.finish()
