# # def max(x,y):
# #     return x if x > y else y
#
# #######
# # print(max(1,2))
#
# def f1():
#     def f2():
#         def f3():
#             print('from f3')
#         f3()
#     f2()
#
# f1()
# # f3() #报错，为何？请看下一小节
#
# ########
# max=1
# def f1():
#     max=2
#     def f2():
#         max=3
#         print(max)
#     f2()
# f1()
# print(max)
#
#
#

gcount = 0

def global_test():
    global gcount
    gcount+=1
    print (gcount)
global_test()