# coding = utf-8

# Brainf*ck in Python

__doc__ = '''Brainf*ck in python
Python 中的 Brainf*ck

P.S. I'm not very good at English, and some of the content is translated by machine,
     please ignore the grammar mistake.

class BF: A Brainf*ck compiler.
      BF.__init__(io): Init the compiler.
      BF.reset(): Reset the memory of compiler.
      BF.execute(code, warn): Execute BF code.
      BF.debug(code, on, warn): Execute BF code by returning a iterable object that returns the pointer
                          and memory of each steps(stop on "on").
function hello_world(): Print "Hello world!" to screen and turn small letter to big letter.
function bf(code, io): A fast way to call Brainf*ck compiler.
function ook_to_bf(code): A function turn Ook! to Brainf*ck.
function visible_debug(code, sleep, on, bf, warn): A extend of BF.debug, it's also an example.
class CharIO, IntIO: The examples of custom IO.

[类]BF: 一个Brainf*ck编译机
    BF.__init__(io): 初始化编译机
    BF.reset(): 重置编译机内存
    BF.execute(code): 执行BF代码
    BF.debug(code, on): 返回一个可迭代对象，返回执行代码中每步(在"on"上停顿)的指针与内存情况
[函数]hello_world(): 将“Hello world!”输出到屏幕，并将小写字母转为大写
[函数]bf(code, io): 一个用于快速调用Brainf*ck编译器的函数
[函数]ook_to_bf(code): 一个将Ook!转为Brainf*ck的函数
[函数]visible_debug(code, sleep, on, bf, warn): BF.debug的扩展，也是使用它的一个例子
[类] CharIO, IntIO: 自定义IO的示例

Brainf*ck Syntax:
Char Meaning
  >  Increment the pointer.
  <  Decrement the pointer.
  +  Increment the byte at the pointer.
  -  Decrement the byte at the pointer.
  .  Output the byte at the pointer.
  ,  Input a byte and store it in the byte at the pointer.
  [  Jump forward past the matching ] if the byte at the pointer is zero.
  ]  Jump backward to the matching [ unless the byte at the pointer is zero.
For more information, see [Wikipedia - Brainfuck] https://en.wikipedia.org/wiki/Brainfuck

Brainf*ck 语法:
字符 含义
  >  指针加一
  <  指针减一
  +  指针指向的字节的值加一
  -  指针指向的字节的值减一
  .  输出指针指向的单元内容
  ,  输入内容到指针指向的单元
  [  如果指针指向的单元值为零，向后跳转到对应的]指令的次一指令处
  ]  如果指针指向的单元值不为零，向前跳转到对应的[指令的次一指令处
更多见[百度百科-Brainfuck]https://baike.baidu.com/item/Brainfuck/1152785?fr=aladdin

Ook! Syntax | Ook! 语法:
    Ook!   | Short Ook! | Brainf*ck
 Ook. Ook? |     . ?    |     >
 Ook? Ook. |     ? .    |     <
 Ook. Ook. |     . .    |     +
 Ook! Ook! |     ! !    |     -
 Ook. Ook! |     . !    |     ,
 Ook! Ook. |     ! .    |     .
 Ook! Ook? |     ! ?    |     [
 Ook? Ook! |     ? !    |     ]


Think about using an extended compiler in ebrainfuck.py.
It has more methods, more simple and readable syntax!
考虑使用在 ebrainfuck.py 文件中的扩展的Brainf*ck编译器，
它有更多的方法，更简单、更可读的语法!'''

################################################################################
# Nothing to do at this time, have a rest!
################################################################################

import re
import sys
import time


class CharIO:
    cache = []

    def input(self):
        if len(self.cache) == 0:
            i = input('')
            if not i:
                i = '\n'
            i = list(i)
            for a in i:
                self.cache.append(ord(a))
        return self.cache.pop(0)

    @staticmethod
    def output(c):
        sys.stdout.write(chr(c))

    def reset(self):
        self.cache = []


class IntIO:
    cache = []

    def input(self):
        if len(self.cache) == 0:
            i = input('')
            i = ','.join('\t'.join(i.split(' ')).split('\t')).split(',')
            for a in i:
                self.cache.append(int(a))
        return self.cache.pop(0)

    @staticmethod
    def output(i):
        print(i, end=' ')

    def reset(self):
        self.cache = []


def visible_debug(code, sleep=0.3, on=None, bf=None, warn=True):
    """Extending function BF.debug 将BF.debug扩展
    (Use help() for more information 使用help()获取更多信息)
    [code, on, warn] The same as BF.debug
    [sleep] The time to sleep per step. (<0 means control by press Enter)
    [bf] Use custom compiler. (None means create a new one)
    [code, on, warn] 与BF.debug相同
    [sleep] 每一步的休眠时间(<0意味着人工控制)
    [bf] 使用自定义编译器(None代表新建一个)"""
    if on is None:
        on = ['+', '-', '>', '<', ',']
    if bf is None:
        bf = BF()
    print('=' * 80)
    print('Start debugging.')
    code = re.sub("[^+\->\[\]<,.\n]", '', code)
    lines = code.split('\n')
    for (s, m, l, c) in bf.debug(code, on, warn):
        o = '|'
        for (ind, v) in enumerate(m):
            if s == ind:
                o += '>'
            else:
                o += ' '
            o += str(v)
            if s == ind:
                o += '<'
            else:
                o += ' '
            o += '|'
        print(' ' * (c + 1), 'v', sep='')
        print(lines[l][:c], lines[l][c], lines[l][(c + 1):])
        print(' ' * (c + 1), '^', sep='')
        print('+', '-' * (len(o) - 2), '+', sep='')
        print(o)
        print('+', '-' * (len(o) - 2), '+', sep='')
        if sleep >= 0:
            time.sleep(sleep)
        else:
            input('Press Enter to Continue ......')
    print('Finish debugging.')


class BF:
    """Init a Brainf*ck Compiler (Use help for more info.使用help获取更多信息)
io: 'char', 'int' or a class like CharIO or IntIO. The input and output type or class
    'char': Your input will be read one character at a time,
            converted to "int" for operation, and reverted to a character
            for output. You can enter more than one character at a time
            without entering a separator. But because the character is entered
            into "sys.stdin" when you press Enter, you need to end it with Enter.
            (Equals to call "io = CharIO")
            Note: The last Enter will not be entered into the Brainf*ck compiler.
    'int':  Your input will be read as an "int" and the output will be a numeric
            value (not a character). You can enter multiple values at once,
            but separated by spaces, tabs, or English (half-corner) commas.
            Because the character is entered into "sys.stdin" when you press Enter,
            you need to use Enter to represent the end of the entry.
            (Equals to call "io = IntIO")
            Note: The last Enter will not be entered into the Brainf*ck compiler,
                  please end with a specific number (like 0, -1) if necessary.
    class:  The class must have three function -- input, output and reset.
            When the compiler encounters ',', it will call input function to get the input,
            which should return an 'int' representing the input value.
            When the compiler encounters '.', the output function will be called
            for output with an "int" parameter.
            When BF.reset is called, it will call reset function to reset the input cache.
            The effect depends on the functions you customize, which can be defined with reference to
            the 'IntIO' and 'CharIO' class in this module.
初始化Brainf*ck编译器
io: 'char'、'int'或 类似CharIO、IntIO的class 输入、输出类型或类
    'char': 你的输入将被一个字符一个字符的读取，并转化为“int”进行操作，
            输出时重新转为一个字符。你一次性可以输入多个字符，不需要输入分隔符。
            但因为当你按下回车时字符才被输入到“sys.stdin”，
            所以你需要用回车代表输入结束。
            (等同于调用"io = CharIO")
            注意：最后一个回车不会被输入进Brainf*ck编译器。
    'int':  你的输入将作为“int”读取，输出时将输出数值(不是字符)。
            你一次性可以输入多个值，但需要用空格、制表符或英文(半角)逗号分开。
            因为当你按下回车时字符才被输入到“sys.stdin”，
            所以你需要用回车代表输入结束。
            (等同于调用"io = IntIO")
            注意：最后一个回车不会被输入进Brainf*ck编译器，
                  (如果需要)请用特定数值代表结束。
    class:  这是一个有input, output和reset方法的类。
            当编译器遇到 “,” 时将会调用input函数来获取输入，
            它应该返回一个代表输入值的“int”；
            当编译器遇到“.”时将会调用output函数来进行输出，调用时带上一个“int”参数。
            当BF.reset被调用时，将会调用reset函数来刷新输入列表(即cache)。
            具体效果取决于自定义的这个类，定义可参照本模块中的"CharIO","IntIO"类"""
    memory = [0]
    seek = 0
    io = None

    def __init__(self, io='char'):
        if io == 'int':
            self.io = IntIO()
        elif io == 'char':
            self.io = CharIO()
        else:
            try:
                self.io = io()
                if 'input' not in dir(self.io) or 'output' not in dir(self.io) or 'reset' not in dir(self.io):
                    raise ValueError
            except Exception:
                raise ValueError(
                    "io needs to be 'char', 'int' or a class like IntIO or CharIO in this .\n"
                    "值错误：io需要为'char'、'int'或类似IntIO或CharIO的类。")
        self.memory = [0]
        self.seek = 0

    def reset(self):
        """Reset the memory of the compiler.
重置编译器的内存"""
        self.memory = [0]
        self.seek = 0
        self.io.reset()

    def execute(self, code, warn=True):
        """ (Use help for more info.使用help获取更多信息)
Execute the code with the compiler.
code: The code that are executed.
warn: A Boolen. The compiler will send you a warnning if you don't reset it
      before you call it to run another code when the value is True.
      For some case like executing a code part by part, set this value False
      to prevent the compiler raising a Warnning.
执行代码
code: 要执行的代码
warn: 一个布尔值。当值为True时，如果在调用它运行另一个代码之前未重置它，
      编译器将发出警告。对于某些情况，如逐部分执行代码，请将此值设置为False
      来防止编译器发出警告。"""
        if self.memory != [0] and warn:
            raise Warning('''You are executing another code before reset the compiler.
Solutions:
1. Reset this compiler before you using it again.
2. Use another compiler to execute.
3. Add "warn=True" when you call the compiler
警告：你在重置编译器前准备用它执行另一串代码。
解决方案：
1.再次使用此编译器之前，将其重置。
2.使用另一个编译器执行。
3.在调用编译器时添加“warn=True”选项''')
        column = [len(i) for i in code.split('\n')]
        clist = list(code)
        index = 0
        back = False
        passing = False
        count = 0
        col = 0
        line = 0
        ncol = 0
        nline = 0
        while True:
            if index == len(clist):
                break
            c = clist[index]
            # print(c, back, passing, index, line, col, sep='\t')
            if back:
                if c == '[':
                    count -= 1
                elif c == ']':
                    count += 1
                if count == 0:
                    back = False
                    index += 1
                    col = ncol + 1
                    line = nline
                    continue
                elif index == 0:
                    raise SyntaxError(
                        "Fail to finding the matching '[' of ']' at line %s column %s\n"
                        "语法错误：在寻找与第%s行第%s列的']'匹配的'['时出错" % (line + 1, col + 1, line + 1, col + 1))
                else:
                    index -= 1
                    if c == '\n':
                        nline -= 1
                        ncol = column[nline] - 1
                    else:
                        ncol -= 1
                    continue
            elif passing:
                if c == ']':
                    count -= 1
                elif c == '[':
                    count += 1
                if count == 0:
                    passing = False
                    index += 1
                    col = ncol + 1
                    line = nline
                    continue
                elif index == len(clist) - 1:
                    raise SyntaxError(
                        "Fail to finding the matching ']' of '[' at line %s column %s\n"
                        "语法错误：在寻找与第%s行第%s列的'['匹配的']'时出错" % (line + 1, col + 1, line + 1, col + 1))
                else:
                    index += 1
                    if c == '\n':
                        nline += 1
                        ncol = 0
                    else:
                        ncol += 1
                    continue
            elif c == '\n':
                col = 0
                line += 1
                index += 1
                continue
            elif c not in ('+', '-', '>', '<', ',', '.', '[', ']'):
                col += 1
                index += 1
                continue
            elif c == '+':
                self.memory[self.seek] += 1
                col += 1
                index += 1
                continue
            elif c == '-':
                self.memory[self.seek] -= 1
                col += 1
                index += 1
                continue
            elif c == '>':
                self.seek += 1
                if self.seek == len(self.memory):
                    self.memory.append(0)
                col += 1
                index += 1
                continue
            elif c == '<':
                self.seek -= 1
                if self.seek == -1:
                    self.memory.insert(0, 0)
                    self.seek += 1
                index += 1
                col += 1
            elif c == '[':
                if self.memory[self.seek] == 0:
                    passing = True
                    count = 1
                    ncol = col + 1
                    nline = line
                    index += 1
                    continue
                else:
                    index += 1
                    col += 1
                    continue
            elif c == ']':
                if self.memory[self.seek] != 0:
                    back = True
                    count = 1
                    ncol = col - 1
                    nline = line
                    index -= 1
                    continue
                else:
                    index += 1
                    col += 1
                    continue
            elif c == ',':
                self.memory[self.seek] = self.io.input()
                index += 1
                col += 1
                continue
            elif c == '.':
                self.io.output(self.memory[self.seek])
                index += 1
                col += 1
                continue

    def debug(self, code, on=None, warn=True):
        """A method like BF.execute but return an iterable object about memory and seek on each step.
        一个类似于BF.execute的函数，但会返回每一步的内存和指针情况。
        (Use help() for more information 使用help()获取更多信息)
        [code, warn] The same as BF.execute
        [on] Stop on which chars. For example, use "on=['[', '!']"
             to stop on the starts of all loops("[") and custom breakpoint("!").
             (None equals to call "on = ['+', '-', '>', '<', ',']")
        [code, warn] 与BF.execute相同
        [on] 在哪些字符上停顿。举个栗子，调用"on=['[', '!']"在每个循环的开始("[")和自定义断点("!")上停顿。
             (None等同于调用"on = ['+', '-', '>', '<', ',']")
        """
        if on is None:
            on = ['+', '-', '>', '<', ',']
        if self.memory != [0] and warn:
            raise Warning('''You are executing another code before reset the compiler.
Solutions:
1. Reset this compiler before you using it again.
2. Use another compiler to execute.
3. Add "warn=True" when you call the compiler
警告：你在重置编译器前准备用它执行另一串代码。
解决方案：
1.再次使用此编译器之前，将其重置。
2.使用另一个编译器执行。
3.在调用编译器时添加“warn=True”选项''')
        column = [len(i) for i in code.split('\n')]
        clist = list(code)
        index = 0
        back = False
        passing = False
        count = 0
        col = 0
        line = 0
        ncol = 0
        nline = 0
        c = None
        while True:
            if index == len(clist):
                break
            if not passing and not back and c in on:
                yield self.seek, self.memory, line, (col - 1)
            c = clist[index]
            # print(c, back, passing, index, line, col, sep='\t')
            if back:
                if c == '[':
                    count -= 1
                elif c == ']':
                    count += 1
                if count == 0:
                    back = False
                    index += 1
                    col = ncol + 1
                    line = nline
                    continue
                elif index == 0:
                    raise SyntaxError(
                        "Fail to finding the matching '[' of ']' at line %s column %s\n"
                        "语法错误：在寻找与第%s行第%s列的']'匹配的'['时出错" % (line + 1, col + 1, line + 1, col + 1))
                else:
                    index -= 1
                    if c == '\n':
                        nline -= 1
                        ncol = column[nline] - 1
                    else:
                        ncol -= 1
                    continue
            elif passing:
                if c == ']':
                    count -= 1
                elif c == '[':
                    count += 1
                if count == 0:
                    passing = False
                    index += 1
                    col = ncol + 1
                    line = nline
                    continue
                elif index == len(clist) - 1:
                    raise SyntaxError(
                        "Fail to finding the matching ']' of '[' at line %s column %s\n"
                        "语法错误：在寻找与第%s行第%s列的'['匹配的']'时出错" % (line + 1, col + 1, line + 1, col + 1))
                else:
                    index += 1
                    if c == '\n':
                        nline += 1
                        ncol = 0
                    else:
                        ncol += 1
                    continue
            elif c == '\n':
                col = 0
                line += 1
                index += 1
                continue
            elif c not in ('+', '-', '>', '<', ',', '.', '[', ']'):
                col += 1
                index += 1
                continue
            elif c == '+':
                self.memory[self.seek] += 1
                col += 1
                index += 1
                continue
            elif c == '-':
                self.memory[self.seek] -= 1
                col += 1
                index += 1
                continue
            elif c == '>':
                self.seek += 1
                if self.seek == len(self.memory):
                    self.memory.append(0)
                col += 1
                index += 1
                continue
            elif c == '<':
                self.seek -= 1
                if self.seek == -1:
                    self.memory.insert(0, 0)
                    self.seek += 1
                index += 1
                col += 1
            elif c == '[':
                if self.memory[self.seek] == 0:
                    passing = True
                    count = 1
                    ncol = col + 1
                    nline = line
                    index += 1
                    continue
                else:
                    index += 1
                    col += 1
                    continue
            elif c == ']':
                if self.memory[self.seek] != 0:
                    back = True
                    count = 1
                    ncol = col - 1
                    nline = line
                    index -= 1
                    continue
                else:
                    index += 1
                    col += 1
                    continue
            elif c == ',':
                self.memory[self.seek] = self.io.input()
                index += 1
                col += 1
                continue
            elif c == '.':
                self.io.output(self.memory[self.seek])
                index += 1
                col += 1
                continue


def bf(code, io='char'):
    """A fast way to call Brainf*ck compiler
一个用于快速调用Brainf*ck编译器的函数"""
    bf = BF(io)
    bf.execute(code)


def ook_to_bf(code):
    """A function turn Ook! to Brainf*ck
一个将Ook!转为Brainf*ck的函数"""
    bfcode = []
    letter1 = ''
    got_one = False
    line1 = 1
    column1 = 0
    line2 = 1
    column2 = 0
    for c in code:
        if not got_one:
            column1 += 1
        column2 += 1
        if c in ('.', '?', '!'):
            if got_one:
                if letter1 == '.':
                    if c == '?':
                        bfcode.append('>')
                    elif c == '.':
                        bfcode.append('+')
                    elif c == '!':
                        bfcode.append(',')
                elif letter1 == '?':
                    if c == '.':
                        bfcode.append('<')
                    elif c == '!':
                        bfcode.append(']')
                    elif c == '?':
                        raise SyntaxError(
                            "Unknow syntax:'??' at line %s column %s and line %s column %s\n"
                            "语法错误：未知的语法“??”在第%s列第%s行和第%s列第%s行" % (line1, column1, line2, column2,
                                                                  line1, column1, line2, column2))
                elif letter1 == '!':
                    if c == '?':
                        bfcode.append('[')
                    elif c == '.':
                        bfcode.append('.')
                    elif c == '!':
                        bfcode.append('-')
                got_one = False
            else:
                got_one = True
                letter1 = c
        elif c == '\n':
            if not got_one:
                line1 += 1
                column1 = 0
            line2 += 1
            column2 = 0
    if got_one:
        raise SyntaxError("Unmatched letter '%s' at line %s column %s.\n"
                          "语法错误：未匹配的符号“%s”在第%s行第%s列" % (letter1, line1, column1, letter1, line1, column1)
                          )
    bfcode = ''.join(bfcode)
    return bfcode


def hello_world():
    """A hello world demo
一个hello world示例"""
    bf = BF()
    # Output:Hello world!
    bf.execute(
        '''
+++++ +++[- >++++ ++++< ]>+++ +++++ .           H
<+++ ++[-> +++++ <]>++ ++.                      e
++ +++++.                                       l
.                                               l
+++ .                                           o
<+++ +++++ [->-- ----- -<]>- ----- ----- ----. ( )
<++++ +++++ [->+++++++ ++<]> +++++ +.           w
--- ----- .                                     o
+++.                                            r
----- -.                                        l
--- ----- .                                     d
<+++ +++++ [->------- -<]>- --.                 !
<'''
    )
    bf.reset()
    # Output:\nSmall letter to big letter(use Enter to escape)\n
    bf.execute('''+++++ +++++.-[ ->+++ +++++ +<]>+ +.<++ +++[- >++++ +<]>+ .<+++ [->-- -<]>-
--.<+ ++[-> +++<] >++.. <++++ ++++[ ->--- ----- <]>-- ----- ----- .<+++
+++++ [->++ +++++ +<]>+ +++++ +++++ +.--- ----. <+++[ ->+++ <]>++ ++++.
.<+++ [->-- -<]>- ----- .<+++ [->++ +<]>+ +++.< +++++ ++++[ ->--- -----
-<]>- .<+++ +++++ +[->+ +++++ +++<] >+++. ----- .<+++ +++++ [->-- -----
-<]>- ----- ----- ----. <++++ ++++[ ->+++ +++++ <]>++ .++++ +++.- -.<++
+++++ +[->- ----- --<]> ----- --.<+ +++++ ++[-> +++++ +++<] >++++ +++++
+++.- ----- -.<++ +[->+ ++<]> +++++ +..<+ ++[-> ---<] >---- --.<+ ++[->
+++<] >++++ .<+++ +++++ [->-- ----- -<]>- ----- ----. <++++ ++++[ ->+++
+++++ <]>++ +++++ +++++ +.--. <+++[ ->--- <]>-- ---.< +++++ +++[- >----
----< ]>--- --.<+ +++++ [->++ ++++< ]>+.< +++++ +[->+ +++++ <]>++ +++.+
+++++ .<+++ [->-- -<]>- ----- .<+++ [->++ +<]>+ +++.< +++++ ++++[ ->---
----- -<]>- .<+++ +++++ +[->+ +++++ +++<] >+++. ----- .<+++ +++++ [->--
----- -<]>- ----- ----- ----. <++++ ++++[ ->+++ +++++ <]>++ +++.< +++[-
>+++< ]>+++ ++.<+ +++[- >---- <]>.- -.<++ +[->+ ++<]> +++++ +.<++ +[->-
--<]> --.<+ +++++ +[->- ----- -<]>- ----- ----- .<[-]++++++++++.''')
    bf.reset()
    # Function:a->A
    bf.execute(',----------[----------------------.[-]++++++++++.,----------]')
