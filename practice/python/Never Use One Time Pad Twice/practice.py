def binary_to_text(binary_str):
    binary_str = binary_str.replace(' ', '').replace(
        '0x', '').replace('\t', '').replace('\n', '')
    return ''.join(chr(int(binary_str[i * 8:i * 8 + 8], 2)) for i in range(len(binary_str) // 8))


d1 = {'0': "0000", '1': "0001", '2': "0010", '3': "0011", '4': "0100", '5': "0101", '6': "0110", '7': "0111",
      '8': "1000", '9': "1001", 'A': "1010", 'B': "1011", 'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}
d2 = {
    "01000001": "A",
    "01000010": "B",
    "01000011": "C",
    "01000100": "D",
    "01000101": "E",
    "01000110": "F",
    "01000111": "G",
    "01001000": "H",
    "01001001": "I",
    "01001010": "J",
    "01001011": "K",
    "01001100": "L",
    "01001101": "M",
    "01001110": "N",
    "01001111": "O",
    "01010000": "P",
    "01010001": "Q",
    "01010010": "R",
    "01010011": "S",
    "01010100": "T",
    "01010101": "U",
    "01010110": "V",
    "01010111": "W",
    "01011000": "X",
    "01011001": "Y",
    "01011010": "Z",
    "01100001": "a",
    "01100010": "b",
    "01100011": "c",
    "01100100": "d",
    "01100101": "e",
    "01100110": "f",
    "01100111": "g",
    "01101000": "h",
    "01101001": "i",
    "01101010": "j",
    "01101011": "k",
    "01101100": "l",
    "01101101": "m",
    "01101110": "n",
    "01101111": "o",
    "01110000": "p",
    "01110001": "q",
    "01110010": "r",
    "01110011": "s",
    "01110100": "t",
    "01110101": "u",
    "01110110": "v",
    "01110111": "w",
    "01111000": "x",
    "01111001": "y",
    "01111010": "z",
    "00100000": " ",
    "00101100": ",",
    "00101110": ".",
    "00100001": "!",
    "00111111": "?",
    "00100010": "\""
}
d3 = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F",
}


def text_XOR_text(num1, num2):
    # 将两个整数转换为二进制字符串
    bin_str1 = ''
    bin_str2 = ''
    min_len = min(len(num1), len(num2))
    for i in range(min_len):
        bin_str1 += d1.get(num1[i])
    for i in range(min_len):
        bin_str2 += d1.get(num2[i])

    # 逐位进行XOR操作
    xor_result = ''
    for i in range(min_len*4):
        xor_result += str(int(bin_str1[i]) ^ int(bin_str2[i]))
    # print(xor_result)
    # ascii_str=binary_to_text(xor_result)
    # print(ascii_str)
    substrings = [xor_result[i:i+8] for i in range(0, len(xor_result), 8)]

    # 逐一印出子字串
    ascii_str = ''
    for substring in substrings:
        ascii_str += d2.get(substring, "*")
    # print(ascii_str)
    return ascii_str


def guess_key(Cm, Gm, hint):
    # 将两个整数转换为二进制字符串
    bin_str1 = ''
    bin_str2 = ''
    min_len = min(len(Cm), len(Gm))
    for i in range(min_len):
        bin_str1 += d1.get(Cm[i])
    for i in range(min_len):
        bin_str2 += d1.get(Gm[i])
    # 逐位进行XOR操作
    xor_result = ''
    for i in range(min_len*4):
        xor_result += str(int(bin_str1[i]) ^ int(bin_str2[i]))
    substrings = [xor_result[i:i+4] for i in range(0, len(xor_result), 4)]

    # 逐一印出子字串
    ascii_str = ''
    i = 0
    for substring in substrings:
        if (hint[i] == '1'):
            ascii_str += d3.get(substring)
        else:
            ascii_str += '*'
        i = i + 1

    print(ascii_str)
    return ascii_str


oriM = "49742069732074686520627261696e2c20746865206c6974746c6520677261792063656c6c73206f6e207768696368206f6e65206d7573742072656c792e204f6e65206d757374207365656b207468652074727574682077697468696e206e6f7420776974686f7574"
ctext1 = '285E8FD00FFC101CE3666990664E22F3A47CE8E31DCA59AB0737DC943F5728C18C040788C461A85C896B82AED11D9F3B62A56C1F684BDAA431853C6B7403CE37885E5260928CAECD27CACBAB99EAC3BA75C1D47FA6703447105B0864516C88E44A547C61DC6343178983B1A9A3C42F6861C5C2C9FE36BCEE00C2E141971F544B9E0A5DDF7AEC6C9682'
ctext2 = '3D5A86D01FFB0914F8666988335136ECF033F8A64DD559B1162CDD9B2E467AC98E041287C42FAE549E74DBEFD319CD3D37A66F5B3C4CCAF0629020396C0F8334895E177FC790BCCD2ACACAF988EACD'
ctext3 = '32599ED001E10B14AA7C609D280338EEB57CF9E35ED559B1532CDC95371367DAC2541293D220AA58DB6E88AEC010812035AB6853790D'
ctext4 = '3259CA9805FA1114F87C67DC334D33E9A33FE5F058D559A1532EDC93295C66DBC24912998123A81D8E749EEA8D5C832030EA6B516503DEF4329D3A78634C8B758A421B6E8FDFAD8425C99FE59EEA87FB7A98D77EAD37635C1C41082A516D81F84E1C6D6A8C7B4A1CC885BDA7A9813C3C29D0D98CBC36B7E40E'
ctext5 = '3259CAB304E71710E76966DC2B5624F4F03AE3E148D559E51A30938E325628DB964B01998F'
ctext6 = '3259CA910FED1015EF667CDC2B5624F4F039FCE34F8754A01F2E938E325628CC87501683D528BB58D72795E1D35C803A31BE2A577903DAF2278373716C598B759C445278899EB98E26D0D1FF9AED8FBE3BD1D565B639374610464D334D6D84F90D4C7A7D8A725852DD9EF4AAA2812F216ECCC5C7'
ctext7 = '285E8FD008EB0D14E97C618A23033FE9BD2FEFEA5B8751B0002A9394354728CB8D491E89D561B9559E2798FCC8118861'
ctext8 = '285E8FD008EB0D14E97C618A23033EF3F03EE5F353C31CB11C7ED79F395F69DA8704128ED861AE518E6288AED614842C2AEA625A3C4EDEFD62953A6A6E4098308F04'
ctext9 = '285E8FD01FE71D14E1616B97664C31A0A434EFA659C248A0102ADA8C3F1F28DC8A4153B7C035BE52952BDBE3D40F996F2CA57E1F7F4CD1E727903F396B5D8138DD5E1A68C78DBF8C2DC0CDAB9AE19AFB6FD0D464A438375C5F5F052D466CC7E14C4F7B32887F591DDC96BCE8AFC82E6864CDDF8DA673B1E95383E4438C0D5D43D719579172E7238CD987ABE396E84A84BEAF23C930DF247F44BF531FEC08B140162E5F1D87836121790DDDABED5A0448965E6B670074B8C9C2C6A5B5305554B4518C757C19FCAA3D4FCD7E1EB1'
ctext10 = '2841839E4CEC0B1EFE606D8E350F77E1BE38AAE252D25EA9162D939D3F5D6DDA83481F998D61A0488873DBE0CE08CD2E32BA6F5E6E03CAEA2E94206A2D588B75954B0468C79DBF882785DBFE97F6C3AB69DDCB70B135270F19471F64516C82FC03'
test1 = '6865206973206120636F6F6C20626F79'
test2 = '00000000000000000000000000000000'
key1 = '****EA****8E******08******6A**8CD0******3D************FA********E2******ED**CD**B507**********4F******3F********42********21EE3A****72********ED********FB**AB**1B**********43************04****793C**************FF'
key2 = '******F0****************466E******5C****3D****************7708****24****E441**********8E******1B42****3F**6B**84**********23EE******72********ED******8B****E3************50**********44********6A******FC******A9**'
key3 = '******F0************************D0****86******************66******24****E4******BE**FB******ED**********1C6C****42****19**2F**14********E7****ED************ED'
key4 = '******F0********8A********23**CE**5C************73********33****E2**************FB4E**8E******00**********2D'
key5 = '****EA****************FC**6D**C9****************73********7C****E2******A1****3DAE******AD7C**00**CA******23**************6C**55**********FF********BF******A7DB**B8********43******************6E3C****************'
key6 = '****EA93**************FC**76**D4D0************C5****B3****7608**********AF'
key7 = '****EAB1**************FC**76**D4D0********A7********B3****7608**********F5******F707******7C********0A****23********53****79**55****72**********************AF**1B******************6D**********2D************72****'
key8 = '******F0******************23**C9**********A7********B3****6708**********F541****BE07**********41'
key9 = '******F0******************23****D0**********3C****5E**************24****F841****AE42**8E******0C**CA****1C6E****42********60******24'
key10 = '******F0****************466C**80******86******************3F08******7397E0******B50BFB********4F******3F**6C**********19******18FD******E7************8B****BADB****************7F**********E7**6C****12************'
key11 = '********6C****************2F57C1****8A**************B3****7D************AD41******53FB******ED0E**********23************0D78**55********E7********A5********E3****************2F******44********23'
key = '7C36EAF06C8E79718A0808FC46235780D05C8A863DA73CC5735EB3FA5A3308A8E22473E0A141CD3DFB07FB8EA17CED4F42CA0A3F1C230084420053190D78EE55FD247200E7FF00ED00A5BF8BFB00E3DB1BB800000050432F7F006D440004E700233C0012FC000072A9FF'
Cmessage = '3542CA991FAE0D19EF286A8E274A39ACF028E2E31DCB55B10732D6DA3D4169D1C247168CCD32ED5295278CE6C81F856F2DA46F1F7156CCF0628336757401CE1A934F5260928CAECD3AC0DAE0DBFB8BBE3BCCC964B7386358165C052D4B2489FE591C7F7B887F4407DDDF'
# It is the brain, the little gray cells on which one mu*t *elyy Onk *us* *eek *he t*d*h wi*hiK n*z *it*Dut
my_list = []
my_list.append(text_XOR_text(key, ctext1))
my_list.append(text_XOR_text(key, ctext2))
my_list.append(text_XOR_text(key, ctext3))
my_list.append(text_XOR_text(key, ctext4))
my_list.append(text_XOR_text(key, ctext5))
my_list.append(text_XOR_text(key, ctext6))
my_list.append(text_XOR_text(key, ctext7))
my_list.append(text_XOR_text(key, ctext8))
my_list.append(text_XOR_text(key, ctext9))
my_list.append(text_XOR_text(key, ctext10))
for j in range(len(my_list)):
    print(j, my_list[j])

mes = ''
hint = []
k_list = []
for i in range(106):
    c = '*'
    flag = 0
    for j in range(len(my_list)):
        if i >= len(my_list[j]):
            continue
        if flag == 0 and my_list[j][i] != '*':
            c = my_list[j][i]
            flag = 1
        if flag == 1 and my_list[j][i] != '*' and my_list[j][i] != c:
            flag = 2
            mes += '20'
            hint.append('1')
            hint.append('1')
            continue
    if flag != 2:
        mes += '00'
        hint.append('0')
        hint.append('0')


ans = text_XOR_text(Cmessage, key)
print(ans)
