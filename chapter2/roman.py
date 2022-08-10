table = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
table2 = {'1000':'M', '900':'CM', '500':'D', '400':'CD', '100':'C', '90':'XC', '50':'L', '40':'XL', '10':'X', '9':'IX', '5':'V', '4':'IV', '1':'I'}
class translator:

    def deciToRoman(self, num):
        val_list = table2.keys()
        val_list = list(map(int, val_list))
        num_str = str(num)
        num_list = []
        for i in reversed(range(len(num_str))):
            num_list.append(int(num_str[len(num_str)-i-1]) * 10**i)
        
        out = []
        for n in range(len(num_list)):
            temp = num_list[n]
            for v in range(len(val_list)):
                if val_list[v] > temp:
                    continue
                elif val_list[v] == temp:
                    out.append(table2[str(val_list[v])])
                    break
                else:
                    while True:
                        if temp - val_list[v] < 0:
                            break
                        temp -= val_list[v]
                        out.append(table2[str(val_list[v])])
        out_str = ""
        for i in out:
            out_str+=i
        return out_str

    def romanToDeci(self, s):
        string = []
        for ss in s:
            string.append(ss)
        string2 = []
        i=0
        while i < len(string)-1:
            if table[string[i]] < table[string[i+1]]:
                string2.append(string[i]+string[i+1])
                i+=1
            else:
                string2.append(string[i])
            i+=1
        string2.append(string[-1])
        num = 0
        for s in string2:
            num += table[s]
        return num
        ### Enter Your Code Here ###

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))
