def eval_strint(s, base=2):
    assert type(s) is str
    assert 2 <= base <= 36
    #
    # YOUR CODE HERE
    #
    return int(s, base)

def eval_strfrac(s, base=2):
    assert is_valid_strfrac(s, base), "'{}' contains invalid digits for a base-{} number.".format(s, base)
    
    #
    # YOUR CODE HERE
    #
    if "." in s:
        integer, decimal = s.split(".")
        decimal = decimal.lower()
    else:
        integer = s
        decimal = "0"
    integer = float(int(integer, base))
    index = -1
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    for i in decimal:
        integer = integer + (base**index)*digits.find(i)
        index = index -1
    return float(integer)
    
def fp_bin(v):
    assert type(v) is float
#
# YOUR CODE HERE
#
    if v < 0:
        s_sign = "-"
    else:
        s_sign = "+"
    num = v.hex().split("x")[1].split("p")[0].replace(".","")
    exp = int(v.hex().split("x")[1].split("p")[-1])
    binary_num = str(bin(int(num, 16))[2:])
    binary_num = binary_num.ljust(53, '0')
    binary_num =  binary_num[:1] + '.' + binary_num[1:]
    return (s_sign, binary_num, exp)

def eval_fp(sign, significand, exponent, base=2):
    assert sign in ['+', '-'], "Sign bit must be '+' or '-', not '{}'.".format(sign)
    assert is_valid_strfrac(significand, base), "Invalid significand for base-{}: '{}'".format(base, significand)
    assert type(exponent) is int

    #
    # YOUR CODE HERE
    #
    if '.' in significand and exponent != 0:
        significand = significand.replace(".", "")
    if exponent > 0:
        significand = significand[0:exponent+1] + "." + significand[exponent+1:]
    elif exponent < 0 :
        significand  = "0" + "." + "0" * (abs(exponent)-1) + significand[0:]
    num = eval_strfrac(significand, base)
    return float((sign + str(num)))

def add_fp_bin(u, v, signif_bits):
    u_sign, u_signif, u_exp = u
    v_sign, v_signif, v_exp = v
    
    # You may assume normalized inputs at the given precision, `signif_bits`.
    assert u_signif[:2] == '1.' and len(u_signif) == (signif_bits+1)
    assert v_signif[:2] == '1.' and len(v_signif) == (signif_bits+1)
    
    #
    # YOUR CODE HERE
    #
    u = eval_fp(u_sign, u_signif, u_exp)
    v = eval_fp(v_sign, v_signif, v_exp)
    sum = u + v
    sign, signif, expo = fp_bin(sum)
    signif = signif[0:signif_bits+1]
    return (sign, signif, expo)


count = 0
for i in N:
    x = [0.1] * i
    t[count] = alg_sum(x)
    count = count + 1
    
print(t)


def alg_sum_accurate(x):
    s = 0.
    x=sorted(x)
    for x_i in x: # x_0, x_1, \ldots, x_{n-1}
        s += x_i
    return s
    