def odd_even(arr):
    if arr[0] == 'S':
        output = ""
        if arr[2] == 'Odd':
            string = arr[1]
            for i in range(len(string)):
                if i % 2 == 0:
                    output+=string[i]
        elif arr[2] == 'Even':
            string = arr[1]
            for i in range(len(string)):
                if i % 2 == 1:
                    output+=string[i]
        return output
    elif arr[0] == 'L':
        output = []
        if arr[2] == 'Odd':
            string = arr[1].split()
            for i in range(len(string)):
                if i % 2 == 0:
                    output.append(string[i])
        elif arr[2] == 'Even':
            string = arr[1].split()
            for i in range(len(string)):
                if i % 2 == 1:
                    output.append(string[i])
        return output
        


print('*** Odd Even ***')
input_list = input('Enter Input : ').split(',')
print(odd_even(input_list))