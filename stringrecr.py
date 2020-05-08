"""
string -  i/p-a1b2
o/p - a1b2 ,a1B2, A1b2, A1B2
"""


def create_parameter(inp_str, cur_str, out_arr):
    cur_str = " "
    while cur_str is not None:
        if cur_str == inp_str:
            out_arr.append(cur_str)
            print(out_arr)
        else:

            cur_str = ch.lower() + ch.upper()
            create_parameter(inp_str, cur_str+1, out_arr)
    return


inp_str = "ABC"
n = len(inp_str)
a = list(inp_str)
