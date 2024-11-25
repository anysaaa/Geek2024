import dis
# 示例字节码
bytecode ='''
  1           0 LOAD_CONST               0 ('SYC{MD5(input)}')
              2 STORE_NAME               0 (flag)

  2           4 LOAD_NAME                1 (print)
              6 LOAD_CONST               1 ('Please input0:')
              8 CALL_FUNCTION            1
             10 POP_TOP

  3          12 LOAD_CONST               2 ('')
             14 STORE_NAME               2 (input0)

  6          16 LOAD_CONST               3 (<code object test2 at 0x00000245D4F44B30, file "program.py", line 6>)
             18 LOAD_CONST               4 ('test2')
             20 MAKE_FUNCTION            0
             22 STORE_NAME               3 (test2)

 14          24 LOAD_CONST               5 (<code object test at 0x00000245D4F44BE0, file "program.py", line 14>)
             26 LOAD_CONST               6 ('test')
             28 MAKE_FUNCTION            0
             30 STORE_NAME               4 (test)

 28          32 LOAD_CONST               7 (13)
             34 STORE_NAME               5 (a)

 29          36 LOAD_CONST               8 (14)
             38 STORE_NAME               6 (b)

 30          40 LOAD_NAME                5 (a)
             42 LOAD_NAME                6 (b)
             44 LOAD_NAME                5 (a)
             46 BINARY_ADD
             48 BINARY_XOR
             50 STORE_NAME               7 (c)

 31          52 LOAD_NAME                6 (b)
             54 LOAD_CONST               9 (100)
             56 BINARY_MULTIPLY
             58 STORE_NAME               8 (d)

 32          60 LOAD_NAME                5 (a)
             62 LOAD_NAME                6 (b)
             64 BINARY_XOR
             66 STORE_NAME               9 (e)

 33          68 LOAD_NAME                8 (d)
             70 LOAD_NAME                7 (c)
             72 LOAD_CONST              10 (4)
             74 BINARY_MULTIPLY
             76 BINARY_SUBTRACT
             78 LOAD_NAME                9 (e)
             80 BINARY_ADD
             82 LOAD_CONST              11 (1)
             84 BINARY_SUBTRACT
             86 STORE_NAME              10 (m)

 35          88 LOAD_NAME               10 (m)
             90 LOAD_CONST              12 (26)
             92 BINARY_MODULO
             94 STORE_NAME              11 (r)

 37          96 LOAD_NAME                4 (test)
             98 LOAD_NAME                2 (input0)
            100 LOAD_NAME               11 (r)
            102 CALL_FUNCTION            2
            104 STORE_NAME              12 (cipher1)

 38         106 LOAD_NAME                3 (test2)
            108 LOAD_NAME               12 (cipher1)
            110 CALL_FUNCTION            1
            112 STORE_NAME              13 (cipher2)

 39         114 LOAD_CONST              13 (-1)
            116 LOAD_CONST              14 (-36)
            118 LOAD_CONST              12 (26)
            120 LOAD_CONST              15 (-5)
            122 LOAD_CONST               8 (14)
            124 LOAD_CONST              16 (41)
            126 LOAD_CONST              17 (6)
            128 LOAD_CONST              18 (-9)
            130 LOAD_CONST              19 (60)
            132 LOAD_CONST              20 (29)
            134 LOAD_CONST              21 (-28)
            136 LOAD_CONST              22 (17)
            138 LOAD_CONST              23 (21)
            140 LOAD_CONST              24 (7)
            142 LOAD_CONST              25 (35)
            144 LOAD_CONST              26 (38)
            146 LOAD_CONST              12 (26)
            148 LOAD_CONST              27 (48)
            150 BUILD_LIST              18
            152 STORE_NAME              14 (num)

 40         154 LOAD_NAME               15 (range)
            156 LOAD_CONST              28 (18)
            158 CALL_FUNCTION            1
            160 GET_ITER
        >>  162 FOR_ITER                38 (to 202)
            164 STORE_NAME              16 (i)

 41         166 LOAD_NAME               13 (cipher2)
            168 LOAD_NAME               16 (i)
            170 BINARY_SUBSCR
            172 LOAD_NAME               14 (num)
            174 LOAD_NAME               16 (i)
            176 BINARY_SUBSCR
            178 COMPARE_OP               3 (!=)
            180 POP_JUMP_IF_FALSE      192

 42         182 LOAD_NAME                1 (print)
            184 LOAD_CONST              29 ('wrong!')
            186 CALL_FUNCTION            1
            188 POP_TOP
            190 JUMP_ABSOLUTE          162

 44     >>  192 LOAD_NAME                1 (print)
            194 LOAD_CONST              30 ('Rrrright!')
            196 CALL_FUNCTION            1
            198 POP_TOP
            200 JUMP_ABSOLUTE          162
        >>  202 LOAD_CONST              31 (None)
            204 RETURN_VALUE

Disassembly of <code object test2 at 0x00000245D4F44B30, file "program.py", line 6>:
  7           0 LOAD_CONST               1 ('SYC')
              2 STORE_FAST               1 (key)

  8           4 LOAD_CONST               2 (18)
              6 STORE_FAST               2 (length)

  9           8 BUILD_LIST               0
             10 STORE_FAST               3 (cipher)

 10          12 LOAD_GLOBAL              0 (range)
             14 LOAD_FAST                2 (length)
             16 CALL_FUNCTION            1
             18 GET_ITER
        >>   20 FOR_ITER                48 (to 70)
             22 STORE_FAST               4 (i)

 11          24 LOAD_FAST                3 (cipher)
             26 LOAD_METHOD              1 (append)
             28 LOAD_GLOBAL              2 (ord)
             30 LOAD_FAST                0 (s2)
             32 LOAD_FAST                4 (i)
             34 BINARY_SUBSCR
             36 CALL_FUNCTION            1
             38 LOAD_FAST                4 (i)
             40 BINARY_XOR
             42 LOAD_GLOBAL              2 (ord)
             44 LOAD_FAST                1 (key)
             46 LOAD_FAST                4 (i)
             48 LOAD_CONST               3 (3)
             50 BINARY_MODULO
             52 BINARY_SUBSCR
             54 CALL_FUNCTION            1
             56 UNARY_INVERT
             58 LOAD_CONST               4 (1)
             60 BINARY_ADD
             62 BINARY_ADD
             64 CALL_METHOD              1
             66 POP_TOP
             68 JUMP_ABSOLUTE           20

 12     >>   70 LOAD_FAST                3 (cipher)
             72 RETURN_VALUE

Disassembly of <code object test at 0x00000245D4F44BE0, file "program.py", line 14>:
 15           0 BUILD_LIST               0
              2 STORE_FAST               2 (result)

 16           4 LOAD_FAST                0 (s)
              6 GET_ITER
        >>    8 FOR_ITER               218 (to 228)
             10 STORE_FAST               3 (i)

 17          12 LOAD_CONST               1 ('A')
             14 LOAD_FAST                3 (i)
             16 DUP_TOP
             18 ROT_THREE
             20 COMPARE_OP               1 (<=)
             22 POP_JUMP_IF_FALSE       32
             24 LOAD_CONST               2 ('Z')
             26 COMPARE_OP               1 (<=)
             28 POP_JUMP_IF_FALSE       80
             30 JUMP_FORWARD             4 (to 36)
        >>   32 POP_TOP
             34 JUMP_FORWARD            44 (to 80)

 18     >>   36 LOAD_FAST                2 (result)
             38 LOAD_METHOD              0 (append)
             40 LOAD_GLOBAL              1 (chr)
             42 LOAD_GLOBAL              2 (ord)
             44 LOAD_FAST                3 (i)
             46 CALL_FUNCTION            1
             48 LOAD_GLOBAL              2 (ord)
             50 LOAD_CONST               1 ('A')
             52 CALL_FUNCTION            1
             54 BINARY_SUBTRACT
             56 LOAD_FAST                1 (R)
             58 BINARY_ADD
             60 LOAD_CONST               3 (26)
             62 BINARY_MODULO
             64 LOAD_GLOBAL              2 (ord)
             66 LOAD_CONST               1 ('A')
             68 CALL_FUNCTION            1
             70 BINARY_ADD
             72 CALL_FUNCTION            1
             74 CALL_METHOD              1
             76 POP_TOP
             78 JUMP_ABSOLUTE            8

 19     >>   80 LOAD_CONST               4 ('a')
             82 LOAD_FAST                3 (i)
             84 DUP_TOP
             86 ROT_THREE
             88 COMPARE_OP               1 (<=)
             90 POP_JUMP_IF_FALSE      100
             92 LOAD_CONST               5 ('z')
             94 COMPARE_OP               1 (<=)
             96 POP_JUMP_IF_FALSE      148
             98 JUMP_FORWARD             4 (to 104)
        >>  100 POP_TOP
            102 JUMP_FORWARD            44 (to 148)

 20     >>  104 LOAD_FAST                2 (result)
            106 LOAD_METHOD              0 (append)
            108 LOAD_GLOBAL              1 (chr)
            110 LOAD_GLOBAL              2 (ord)
            112 LOAD_FAST                3 (i)
            114 CALL_FUNCTION            1
            116 LOAD_GLOBAL              2 (ord)
            118 LOAD_CONST               4 ('a')
            120 CALL_FUNCTION            1
            122 BINARY_SUBTRACT
            124 LOAD_FAST                1 (R)
            126 BINARY_ADD
            128 LOAD_CONST               3 (26)
            130 BINARY_MODULO
            132 LOAD_GLOBAL              2 (ord)
            134 LOAD_CONST               4 ('a')
            136 CALL_FUNCTION            1
            138 BINARY_ADD
            140 CALL_FUNCTION            1
            142 CALL_METHOD              1
            144 POP_TOP
            146 JUMP_ABSOLUTE            8

 21     >>  148 LOAD_CONST               6 ('0')
            150 LOAD_FAST                3 (i)
            152 DUP_TOP
            154 ROT_THREE
            156 COMPARE_OP               1 (<=)
            158 POP_JUMP_IF_FALSE      168
            160 LOAD_CONST               7 ('9')
            162 COMPARE_OP               1 (<=)
            164 POP_JUMP_IF_FALSE      216
            166 JUMP_FORWARD             4 (to 172)
        >>  168 POP_TOP
            170 JUMP_FORWARD            44 (to 216)

 22     >>  172 LOAD_FAST                2 (result)
            174 LOAD_METHOD              0 (append)
            176 LOAD_GLOBAL              1 (chr)
            178 LOAD_GLOBAL              2 (ord)
            180 LOAD_FAST                3 (i)
            182 CALL_FUNCTION            1
            184 LOAD_GLOBAL              2 (ord)
            186 LOAD_CONST               6 ('0')
            188 CALL_FUNCTION            1
            190 BINARY_SUBTRACT
            192 LOAD_FAST                1 (R)
            194 BINARY_ADD
            196 LOAD_CONST               8 (10)
            198 BINARY_MODULO
            200 LOAD_GLOBAL              2 (ord)
            202 LOAD_CONST               6 ('0')
            204 CALL_FUNCTION            1
            206 BINARY_ADD
            208 CALL_FUNCTION            1
            210 CALL_METHOD              1
            212 POP_TOP
            214 JUMP_ABSOLUTE            8

 24     >>  216 LOAD_FAST                2 (result)
            218 LOAD_METHOD              0 (append)
            220 LOAD_FAST                3 (i)
            222 CALL_METHOD              1
            224 POP_TOP
            226 JUMP_ABSOLUTE            8

 25     >>  228 LOAD_CONST               9 ('')
            230 LOAD_METHOD              3 (join)
            232 LOAD_FAST                2 (result)
            234 CALL_METHOD              1
            236 RETURN_VALUE

'''
def parse_bytecode(bytecode):
    lines = bytecode.strip().split('\n')
    parsed = []
    for line in lines:
        parts = line.split()
        if len(parts) >= 4 and parts[1].isdigit():
            offset = int(parts[1])
            opname = parts[2]
            arg = parts[3] if len(parts) > 3 else None
            argval = ' '.join(parts[4:]) if len(parts) > 4 else None
            parsed.append((offset, opname, arg, argval))
    return parsed

# 将字节码转换成 Python 代码
def bytecode_to_source(parsed):
    source_lines = []
    indent_level = 0

    for offset, opname, arg, argval in parsed:
        if opname == 'LOAD_CONST':
            source_lines.append(f"const_{arg} = {repr(argval)}")
        elif opname == 'STORE_NAME':
            source_lines.append(f"{arg} = const_{arg}")
        elif opname == 'LOAD_NAME':
            source_lines.append(f"load_{arg}()")
        elif opname == 'CALL_FUNCTION':
            source_lines.append(f"call_function({arg})")
        elif opname == 'POP_TOP':
            source_lines.append("pop_top()")
        elif opname == 'FOR_ITER':
            source_lines.append(f"for i in range({arg}):")
            indent_level += 1
        elif opname == 'BINARY_SUBSCR':
            source_lines.append(f"binary_subscr()")
        elif opname == 'COMPARE_OP':
            source_lines.append(f"compare_op({argval})")
        elif opname == 'POP_JUMP_IF_FALSE':
            source_lines.append(f"if not condition: break")
        elif opname == 'JUMP_ABSOLUTE':
            source_lines.append(f"continue")
        elif opname == 'RETURN_VALUE':
            source_lines.append(f"return_value()")
        else:
            source_lines.append(f"# {opname} {arg} {argval}")

        if opname == 'FOR_ITER':
            indent_level -= 1

    return '\n'.join(['    ' * indent_level + line for line in source_lines])

# 解析并转换字节码
parsed_bytecode = parse_bytecode(bytecode)
source_code = bytecode_to_source(parsed_bytecode)

print(source_code)