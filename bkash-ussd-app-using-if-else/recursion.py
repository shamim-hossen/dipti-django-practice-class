'''print factorial 1,2,6,24,120'''
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         result = n*fact(n-1)
#         print(result)
#         return result
# fact(5)






'''print factorial reversly 120,24,6,2,1'''
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# def printfact(n):
#     for i in range(n, 0, -1):
#         print(fact(i))


# print(printfact(5))


'''print number '''
def sum(n):
    if n>0:
        sum(n-1)
        print(n)


sum(10)

