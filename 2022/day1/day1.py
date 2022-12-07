def main():
    number = calculate(get_input())
    print("Top 1: ", max(number))
    top3 = top3f(number, 3)
    print("Top 3: ", sum(top3))

def get_input():
    with open('inputday1.txt') as f:
        lines = f.readlines()
        return lines

def convert_int(x):
     try:
         return int(x)
     except ValueError:
         return x

def calculate(input):
    result = []
    for line in input:
        numbers = (line.rstrip('\n'))
        result.append(numbers)
    newlist = [convert_int(x) for x in result]
    l_new = []
    start_i = 0
    for i in range(len(newlist)):
        if (newlist[i]==''):
            l_new.append(newlist[start_i:i])
            start_i = i+1
    l_new.append(newlist[start_i:i+1])
    numbers = []
    for l in l_new:
        numbers.append(sum(l))
    return numbers

def top3f(list1, N):
    final_list = []
    for i in range(0, N):
        max1 = 0  
        for j in range(len(list1)):    
            if list1[j] > max1:
                max1 = list1[j];          
        list1.remove(max1);
        final_list.append(max1)      
    return final_list


main()
