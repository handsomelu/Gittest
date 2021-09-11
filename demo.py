# from python.demo1 import Demo1
# # from testing import demo2
# # # from testing.demo2 import Demo2
# #
# # from testing.demo2 import *
# # # Demo1()
# # # # Demo2()
# # # print(demo2.f())
# # f()



from testing.demo2 import *   #from xxx.py import *，若直接放在__all__中，其他文本
                            # 可直接使用该方法
print(hello)
print(f())


from testing import demo2      #from xxx.py import xxx。未放入__all__中，则导入后需加前缀demo2.xxx
print(demo2.hello)



'''

git init  
'''