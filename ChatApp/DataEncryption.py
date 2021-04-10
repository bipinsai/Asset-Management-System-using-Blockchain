PC1 = [
   57, 49, 41, 33, 25, 17,  9,
    1, 58, 50, 42, 34, 26, 18,
   10,  2, 59, 51, 43, 35, 27,
   19, 11,  3, 60, 52, 44, 36,
   63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
   14,  6, 61, 53, 45, 37, 29,
   21, 13,  5, 28, 20, 12,  4
];
PC2 = [
    14, 17, 11, 24,  1,  5,
    3, 28, 15,  6, 21, 10,
    23, 19, 12,  4, 26,  8,
    16,  7, 27, 20, 13,  2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
];
IP= [
    58, 50, 42, 34, 26, 18, 10,  2,
    60, 52, 44, 36, 28, 20, 12,  4,
    62, 54, 46, 38, 30, 22, 14,  6,
    64, 56, 48, 40, 32, 24, 16,  8,
    57, 49, 41, 33, 25, 17,  9,  1,
    59, 51, 43, 35, 27, 19, 11,  3,
    61, 53, 45, 37, 29, 21, 13,  5,
    63, 55, 47, 39, 31, 23, 15,  7
];
 
Expansion = [
    32,  1,  2,  3,  4,  5,  4,  5,
     6,  7,  8,  9,  8,  9, 10, 11,
    12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21,
    22, 23, 24, 25, 24, 25, 26, 27,
    28, 29, 28, 29, 30, 31, 32,  1]

SBox = [
     [
     [14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
     [ 0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
     [ 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
     [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13],
     ],
 
     [
     [15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10],
     [ 3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5],
     [ 0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15],
     [13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9],
     ],
 
     [
     [10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8],
     [13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1],
     [13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7],
     [ 1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12],
     ],
 
     [
     [ 7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15],
     [13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9],
     [10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4],
     [ 3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14],
     ],
 
     [
     [ 2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9],
     [14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6],
     [ 4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14],
     [11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3],
     ],
 
     [
     [12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11],
     [10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8],
     [ 9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6],
     [ 4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13],
     ],
 
     [
     [ 4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1],
     [13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6],
     [ 1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2],
     [ 6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12],
     ],
 
     [
     [13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7],
     [ 1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2],
     [ 7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8],
     [ 2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11],
     ],
];
 
PBox = [
      16,  7, 20, 21, 29, 12, 28, 17,
       1, 15, 23, 26,  5, 18, 31, 10,
       2,  8, 24, 14, 32, 27,  3,  9,
      19, 13, 30,  6, 22, 11,  4, 25
];
def leftShitOne (s):
    tempS = ""
    # DEBUG
    # print(s[0])
    # print(s)
    # print(s[2])
    # temp = s[0]
    for i in range(0, len(s)-1):
        tempS += s[i+1]
    # DEBUG
    # print(tempS)
    tempS +=s[0:1]
    # s2 = ""
    return tempS

def leftShiftTwo(s):
    return leftShitOne(leftShitOne(s))

def hexToBinary(s):
    dict1 ={}
    dict1['0']= "0000"
    dict1['1']= "0001"
    dict1['2']= "0010"
    dict1['3']= "0011"
    dict1['4']= "0100"
    dict1['5']= "0101"
    dict1['6']= "0110"
    dict1['7']= "0111"
    dict1['8']= "1000"
    dict1['9']= "1001"
    dict1['A']= "1010"
    dict1['B']= "1011"
    dict1['C']= "1100"
    dict1['D']= "1101"
    dict1['E']= "1110"
    dict1['F']= "1111" 
    dict1['a']= "1010"
    dict1['b']= "1011"
    dict1['c']= "1100"
    dict1['d']= "1101"
    dict1['e']= "1110"
    dict1['f']= "1111"

    binary = ""
    for i in range(len(s)):
        c = s[i]
        binary +=dict1[c]
    # print(binary)
    return binary

def binaryToHex(s):
    dict1 = {}
    dict1["0000"] = '0'
    dict1["0001"] = '1'
    dict1["0010"] = '2'
    dict1["0011"] = '3'
    dict1["0100"] = '4'
    dict1["0101"] = '5'
    dict1["0110"] = '6'
    dict1["0111"] = '7'
    dict1["1000"] = '8'
    dict1["1001"] = '9'
    dict1["1010"] = 'A'
    dict1["1011"] = 'B'
    dict1["1100"] = 'C'
    dict1["1101"] = 'D'
    dict1["1110"] = 'E'
    dict1["1111"] = 'F'

    hex = ""
    for i in range(0, len(s), 4):
        # DEBUG
        # print(s[i:4])
        # print(f"hex {hex}")
        hex += dict1[s[i:i + 4]]
    # print(hex)
    return hex

def xor_strings(a, b):
    result = ""
    for i in range(0, len(b)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result

# if "__name__" == "__main__":
# Shit Amount (Iteration -> Amount)
def DES(pl):
    shift_amount = {}
    shift_amount[1] = 1
    shift_amount[2] = 1
    shift_amount[3] = 2
    shift_amount[4] = 2
    shift_amount[5] = 2
    shift_amount[6] = 2
    shift_amount[7] = 2
    shift_amount[8] = 2
    shift_amount[9] = 1
    shift_amount[10] = 2
    shift_amount[11] = 2
    shift_amount[12] = 2
    shift_amount[13] = 2
    shift_amount[14] = 2
    shift_amount[15] = 2
    shift_amount[16] = 1
    # Helper Data
    FourBitToDecimal = {}
    FourBitToDecimal["0000"] = 0;
    FourBitToDecimal["0001"] = 1;
    FourBitToDecimal["0010"] = 2;
    FourBitToDecimal["0011"] = 3;
    FourBitToDecimal["0100"] = 4;
    FourBitToDecimal["0101"] = 5;
    FourBitToDecimal["0110"] = 6;
    FourBitToDecimal["0111"] = 7;
    FourBitToDecimal["1000"] = 8;
    FourBitToDecimal["1001"] = 9;
    FourBitToDecimal["1010"] = 10;
    FourBitToDecimal["1011"] = 11;
    FourBitToDecimal["1100"] = 12;
    FourBitToDecimal["1101"] = 13;
    FourBitToDecimal["1110"] = 14;
    FourBitToDecimal["1111"] = 15;
    DecimalToFourBit = {}
    DecimalToFourBit[0] = "0000";
    DecimalToFourBit[1] = "0001";
    DecimalToFourBit[2] = "0010";
    DecimalToFourBit[3] = "0011";
    DecimalToFourBit[4] = "0100";
    DecimalToFourBit[5] = "0101";
    DecimalToFourBit[6] = "0110";
    DecimalToFourBit[7] = "0111";
    DecimalToFourBit[8] = "1000";
    DecimalToFourBit[9] = "1001";
    DecimalToFourBit[10] = "1010";
    DecimalToFourBit[11] = "1011";
    DecimalToFourBit[12] = "1100";
    DecimalToFourBit[13] = "1101";
    DecimalToFourBit[14] = "1110"; 
    DecimalToFourBit[15] = "1111";

    plain_text = pl

    key_word = "133457799BBCDFF1"
    # convert hex to binary
    plain_text = hexToBinary(plain_text)
    key_word = hexToBinary(key_word)
    # Generate 56 bit DES key from 64 bit key word using PC1 table
    # print(plain_text)
    # print(key_word)
    key = ""
    for i in range(56):
        key += key_word[PC1[i] - 1]
    # print(key)
    # Generate round keys
    left = key[0:28]
    right = key[28:56]
    # print(left)
    # print(right)
    first_key = ""
    for i in range(1, 17):
        round_key = ""
        if shift_amount[i] == 1:
            left = leftShitOne(left)
            right = leftShitOne(right)
        else:
            left = leftShiftTwo(left)
            right = leftShiftTwo(right)
        combined = left + right
        # print(combined)
        for j in range(48):
            # DEBUG
            # print(j)
            round_key += combined[PC2[j] - 1]
        if i == 1:
            first_key = round_key
        # binaryToHex(round_key)
        # print(binaryToHex(round_key))

    # Calculating L1 = R0 and R1 = L0 ^ F(R0, K1)
    # 1. PT(64) -> IP(PT) (64) using IP table
    IP_Msg = ""
    for i in range(64):
        IP_Msg += plain_text[IP[i] - 1]
    # print(IP_Msg)
    L0 = IP_Msg[0:32]
    R0 = IP_Msg[32:64]
    # 2. L1 = R0
    L1 = R0
    # 3. Calculating F(R0, K1)
    # Round Function STARTS
    expand_R0 = ""
    for i in range(48):
        expand_R0 += R0[Expansion[i] - 1]
    # print(expand_R0)
    intermediate = xor_strings(first_key, expand_R0)
    # print(intermediate)
    # intermediate (48 bit) passes through 8 S-boxes to get 32 bit quantity
    # Each 6 bit of the 48 bit will be use to lookup the corresponding S-box for the 4-bit number.
    s_box_ind = 0
    result = ""
    for i in range(0, 48, 6):
        # DEBUG
        # originally i:6
        six_bit = intermediate[i:i+6]
        row_str = ""
        row_str += six_bit[0]
        row_str += six_bit[5]
        row = -1
        col = -1
        if row_str == "00":
            row = 0
        elif row_str == "01":
            row = 1
        elif row_str == "10":
            row = 2
        elif row_str == "11":
            row = 3
        # DEBUG
        # originally 1:4
        col = FourBitToDecimal[six_bit[1:5]]
        # S_Box[row][col] expressed in 4 bit is the compressed value
        result += DecimalToFourBit[SBox[s_box_ind][row][col]]
        s_box_ind+=1
        
    round_function = ""
    for i in range(32):
        round_function += result[PBox[i] - 1]
    # Round Function ENDS
    R1 = xor_strings(L0, round_function)
    cipherText = binaryToHex(L1)+binaryToHex(R1);
    return cipherText
