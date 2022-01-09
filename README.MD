# Brainf*ck Docs
Brainf*ck文档

> _P.S. I'm not very good at English, and some content
is translated by machine,please ignore the grammar
mistake. If you have advice for translation, please
open an issue with tag "translate advice"_

## Why this?
为什么用这个?

This version of Brainf*ck has many advantages:
1. Support for basic Brainf*uck syntax
2. Have a non-static memory system
3. Have some enhancement syntax(TODO)
4. Have a debug method and a debugger
5. ... ...

这个版本的Brainf*ck有很多优点:
1. 支持基础Brainf*ck语法
2. 有非静态内存系统
3. 有增强语法(TODO)
4. 有调试模式以及一个调试器
5. 中文文档，对中国程序员相当友好
6. ... ...

## Brainf*ck syntax
Brainf*ck语法
### Basic Syntax
基础语法

| Char |                                 Meaning                                 |
|:----:|:-----------------------------------------------------------------------:|
|  \>  |                         Increment the pointer.                          |
|  <   |                         Decrement the pointer.                          |
|  +   |                   Increment the byte at the pointer.                    |
|  -   |                   Decrement the byte at the pointer.                    |
|  .   |                     Output the byte at the pointer.                     |
|  ,   |          Input a byte and store it in the byte at the pointer.          |
|  [   |  Jump forward past the matching ] if the byte at the pointer is zero.   |
|  ]   | Jump backward to the matching [ unless the byte at the pointer is zero. |

For more information, see [Wikipedia - Brainfuck] https://en.wikipedia.org/wiki/Brainfuck

| 字符  |               含义                |
|:---:|:-------------------------------:|
| \>  |              指针加一               |
|  <  |              指针减一               |
|  +  |           指针指向的字节的值加一           |
|  -  |           指针指向的字节的值减一           |
|  .  |           输出指针指向的单元内容           |
|  ,  |          输入内容到指针指向的单元           |
|  [  | 如果指针指向的单元值为零，向后跳转到对应的]指令的次一指令处  |
|  ]  | 如果指针指向的单元值不为零，向前跳转到对应的[指令的次一指令处 |

更多见[百度百科-Brainfuck]https://baike.baidu.com/item/Brainfuck/1152785?fr=aladdin
### Enhancement Syntax _(TODO)_
增强语法 _(TODO)_

|   Char    |                        Meaning                        |
|:---------:|:-----------------------------------------------------:|
|     ^     |             Jump out of the loop.(break)              |
|     v     |      Return to the start of the loop.(continue)       |
|  (?A:B)   |     Do A if the current value isn't 0, else do B.     |
|  &#124;   |  Insert a cell after current and move pointer to it.  |
|     x     | Delete current cell and move pointer to the left one. |
|   (.A)    |                 Output the char "A".                  |
|   (,A)    |           Make current cell value be int A.           |
|  ($A:B)   |     Define a function called "A", with process B.     |
|   (@A)    |                   Call function "A"                   |
|     !     |          Breakpoint(enable at debug methods)          |
| +(-/>/<)A |               Execute +(-/>/<) A times.               |

|    字符     |         含义         |
|:---------:|:------------------:|
|     ^     |    退出循环(break)     |
|     v     |   重返循环(continue)   |
|  (?A:B)   | 如果当前值不为0，执行A，否则执行B |
|  &#124;   | 在当前格后插入一格，并移至新插入的格 |
|     x     |    删除当前格，并移至左侧格    |
|   (.A)    |      输出字符“A”       |
|   (,A)    |   给当前格赋值为A(int值)   |
|  ($A:B)   |   将过程B定义为名叫A的函数    |
|   (@A)    |       调用函数A        |
|     !     |    断点(在调试模式启用)     |
| +(-/>/<)A |  执行 +(-/>/<) A 次.  |

### Ook! Syntax
Ook!语法

|   Ook!    | (Short) Ook! | Brainf*ck |
|:---------:|:------------:|:---------:|
| Ook. Ook? |     . ?      |     >     |
| Ook? Ook. |     ? .      |     <     |
| Ook. Ook. |     . .      |     +     |
| Ook! Ook! |     ! !      |     -     |
| Ook. Ook! |     . !      |     ,     |
| Ook! Ook. |     ! .      |     .     |
| Ook! Ook? |     ! ?      |     [     |
| Ook? Ook! |     ? !      |     ]     |


## function tree
功能树
```
brainfuck.py
|
|-Class BF
| |-__init__(io)
| |-execute(code, warn)
| |-debug(code, on, warn)
| \-reset()
|
|-Class CharIO/IntIO
| |-input()
| |-output(i)
| \-reset()
|
|-function visible_debug(code, sleep, bf, on, warn)
|-function bf(code, io)
|-function ook_to_bf(code)
\-function hello_world()

e_brainfuck.py
\- TODO ... ...
```
## Docs
文档

### [class] BF(builtins.object)
```
class BF(builtins.object)
 |  BF(io='char')
 |  __init__(self, io='char')
 |  Init a Brainf*ck Compiler
 |  io: 'char', 'int' or a class like CharIO or IntIO. The input and output type or class
 |      'char': Your input will be read one character at a time,
 |              converted to "int" for operation, and reverted to a character
 |              for output. You can enter more than one character at a time
 |              without entering a separator. But because the character is entered
 |              into "sys.stdin" when you press Enter, you need to end it with Enter.
 |              (Equals to call "io = CharIO")
 |              Note: The last Enter will not be entered into the Brainf*ck compiler.
 |      'int':  Your input will be read as an "int" and the output will be a numeric
 |              value (not a character). You can enter multiple values at once,
 |              but separated by spaces, tabs, or English (half-corner) commas.
 |              Because the character is entered into "sys.stdin" when you press Enter,
 |              you need to use Enter to represent the end of the entry.
 |              (Equals to call "io = IntIO")
 |              Note: The last Enter will not be entered into the Brainf*ck compiler,
 |                    please end with a specific number (like 0, -1) if necessary.
 |      class:  The class must have three function -- input, output and reset.
 |              When the compiler encounters ',', it will call input function to get the input,
 |              which should return an 'int' representing the input value.
 |              When the compiler encounters '.', the output function will be called
 |              for output with an "int" parameter.
 |              When BF.reset is called, it will call reset function to reset the input cache.
 |              The effect depends on the functions you customize, which can be defined with reference to
 |              the 'IntIO' and 'CharIO' class in this module.
 |  初始化Brainf*ck编译器
 |  io: 'char'、'int'或 类似CharIO、IntIO的class 输入、输出类型或类
 |      'char': 你的输入将被一个字符一个字符的读取，并转化为“int”进行操作，
 |              输出时重新转为一个字符。你一次性可以输入多个字符，不需要输入分隔符。
 |              但因为当你按下回车时字符才被输入到“sys.stdin”，
 |              所以你需要用回车代表输入结束。
 |              (等同于调用"io = CharIO")
 |              注意：最后一个回车不会被输入进Brainf*ck编译器。
 |      'int':  你的输入将作为“int”读取，输出时将输出数值(不是字符)。
 |              你一次性可以输入多个值，但需要用空格、制表符或英文(半角)逗号分开。
 |              因为当你按下回车时字符才被输入到“sys.stdin”，
 |              所以你需要用回车代表输入结束。
 |              (等同于调用"io = IntIO")
 |              注意：最后一个回车不会被输入进Brainf*ck编译器，
 |                    (如果需要)请用特定数值代表结束。
 |      class:  这是一个有input, output和reset方法的类。
 |              当编译器遇到 “,” 时将会调用input函数来获取输入，
 |              它应该返回一个代表输入值的“int”；
 |              当编译器遇到“.”时将会调用output函数来进行输出，调用时带上一个“int”参数。
 |              当BF.reset被调用时，将会调用reset函数来刷新输入列表(即cache)。
 |              具体效果取决于自定义的这个类，定义可参照本模块中的"CharIO","IntIO"类
 |  
 |  debug(self, code, on=None, warn=True)
 |      A method like BF.execute but return an iterable object about memory and seek on each step.
 |      一个类似于BF.execute的函数，但会返回每一步的内存和指针情况。
 |      [code, warn] The same as BF.execute
 |      [on] Stop on which chars. For example, use "on=['[', '!']"
 |           to stop on the starts of all loops("[") and custom breakpoint("!").
 |           (None equals to call "on = ['+', '-', '>', '<', ',']")
 |      [code, warn] 与BF.execute相同
 |      [on] 在哪些字符上停顿。举个栗子，调用"on=['[', '!']"在每个循环的开始("[")和自定义断点("!")上停顿。
 |           (None等同于调用"on = ['+', '-', '>', '<', ',']")
 |  
 |  execute(self, code, warn=True)
 |      Execute the code with the compiler.
 |      code: The code that are executed.
 |      warn: A Boolen. The compiler will send you a warnning if you don't reset it
 |            before you call it to run another code when the value is True.
 |            For some case like executing a code part by part, set this value False
 |            to prevent the compiler raising a Warnning.
 |      执行代码
 |      code: 要执行的代码
 |      warn: 一个布尔值。当值为True时，如果在调用它运行另一个代码之前未重置它，
 |            编译器将发出警告。对于某些情况，如逐部分执行代码，请将此值设置为False
 |            来防止编译器发出警告。
 |  
 |  reset(self)
 |      Reset the memory of the compiler.
 |      重置编译器的内存
 |  
```
### [function] visible_debug()
```
visible_debug(code, sleep=0.3, on=None, bf=None, warn=True)
    Extending function BF.debug
    将BF.debug扩展
    [code, on, warn] The same as BF.debug
    [sleep] The time to sleep per step. (<0 means control by press Enter)
    [bf] Use custom compiler. (None means create a new one)
    [code, on, warn] 与BF.debug相同
    [sleep] 每一步的休眠时间(<0意味着人工控制)
    [bf] 使用自定义编译器(None代表新建一个)
```
### [function] bf()
```
bf(code, io='char')
    A fast way to call Brainf*ck compiler
    一个用于快速调用Brainf*ck编译器的函数
```
### [function] ook_to_bf()
```
ook_to_bf(code)
    A function turn Ook! to Brainf*ck
    一个将Ook!转为Brainf*ck的函数
```
### [function] hello_world()
```
hello_world()
    A hello world demo
    一个hello world示例
```
