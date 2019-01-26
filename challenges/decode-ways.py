"""
#7
Facebook

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

"""

# allMessages = []

# def decode(parsed, remaining):
#     if remaining == "":
#         if parsed not in allMessages:
#             allMessages.append(parsed)
#         else:
#             print(parsed)
#         return

#     singleDigit = int(remaining[0])
#     if singleDigit in range(1,27):
#         decode(parsed+[singleDigit], remaining[1:])

#     if len(remaining)>1:
#         twoDigits = int(remaining[0:2])
#         if twoDigits in range(1,27):
#             decode(parsed+[twoDigits], remaining[2:])

 def decode(L):
    if len(L) == 0:
        return 1
    oneDigit = decode(L[1:]) if int(L[:1]) in range(1, 27) else 0
    twoDigit = 0
    if (len(L) > 1):
        twoDigit = decode(L[2:]) if int(L[:2]) in range(1, 27) else 0
    return oneDigit + twoDigit           
 
if __name__ == "__main__":
    message = input().strip()
    print(decodeAgain(message))
#     decode([], message)
#     print(len(allMessages))
