"""
string -  i/p-a1b2
o/p - a1b2 ,a1B2, A1b2, A1B2
"""


def create_parameter(inp_str, cur_str, out_arr):
    print(inp_str.lower())
    out_arr = []
    if(inp_str == cur_str):
        return
    else:
        for i in range(inp_str)
