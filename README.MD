# Brainf*ck Docs
Brainf*ck文档

_P.S. I'm not very good at English, and some content
is translated by machine,please ignore the grammar
mistake. If you have advice for translation, please
open an issue with tag "translate advice"_

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
```
## Docs
文档

### [class] BF(builtins.object)
```
class BF(builtins.object)
 |  BF(io='char')
 |  
 |  Init a Brainf*ck Compiler (Use help for more info.使用help获取更多信息)
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
 |  Methods defined here:
 |  
 |  __init__(self, io='char')
 |  
 |  debug(self, code, on=None, warn=True)
 |      A method like BF.execute but return an iterable object about memory and seek on each step.
 |      一个类似于BF.execute的函数，但会返回每一步的内存和指针情况。
 |      (Use help() for more information 使用help()获取更多信息)
 |      [code, warn] The same as BF.execute
 |      [on] Stop on which chars. For example, use "on=['[', '!']"
 |           to stop on the starts of all loops("[") and custom breakpoint("!").
 |           (None equals to call "on = ['+', '-', '>', '<', ',']")
 |      [code, warn] 与BF.execute相同
 |      [on] 在哪些字符上停顿。举个栗子，调用"on=['[', '!']"在每个循环的开始("[")和自定义断点("!")上停顿。
 |           (None等同于调用"on = ['+', '-', '>', '<', ',']")
 |  
 |  execute(self, code, warn=True)
 |      (Use help for more info.使用help获取更多信息)
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
