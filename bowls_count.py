'''
* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
'''
# n = 3
# s = 6
# n = 4
# s2 = s + n


n = 6
#TODO count how many bowls do we have?


def bowls_sequence(n):
    return (1 + n) * n / 2
    #print(bowl)


def bowls_loop_1(n):
    summ = 0
    for num in range(1, n + 1, 1):
        summ += num
    return summ

def bowls_loop_2(n):
    total_sum = 0
    for i in range(n, -1, -1):
        total_sum += i
        #print("Sum of counts:", total_sum)
    return total_sum

def bowls_recursive(n):
    if n == 1:
        return 1
    else:
        s = bowls_recursive(n-1) + n
        return s

# def bowls_loop_3(n):
#     for i in range(n):
#         1 + i
#     return
n = 5
print('Sum using sequence: {}'.format(bowls_sequence(n)))
print('Sum using loop 1: {}'.format(bowls_loop_1(n)))
print('Sum using loop 2: {}'.format(bowls_loop_2(n)))
print('Sum using recursion: {}'.format(bowls_recursive(n)))
#print(bowls_sequence(n))


