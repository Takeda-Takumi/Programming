k = int(input())

k_bit = bin(k)

k_bit_str = str(k_bit)

answer = ""
for i in range(2, len(k_bit_str)):
    if(k_bit_str[i] == "1"):
        answer = answer + "2"
    else:
        answer = answer + "0"

print(answer)

# tmp = k
# ans = ""
# while tmp != 0:
#     if(tmp%2 == 1):
#         ans = ans + "2"
#     else:
#         ans = ans + "0"
#     tmp = tmp / 2

# print(ans[::-1])


