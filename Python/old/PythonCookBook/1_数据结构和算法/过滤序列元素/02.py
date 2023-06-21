'''
有时候，过滤规则比较复杂，不能简单的在列表推导或者生成器表达式中表达出
来。比如，假设过滤的时候需要处理一些异常或者其他复杂情况。这时候你可以将过滤
代码放到一个函数中，然后使用内建的 filter() 函数。示例如下：

'''

values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def Is_Int(values):
    try:
        v = int(values)
        # print(v)
        return True 
    except Exception as e:
        # print(e)
        return False

int_values = list(filter(Is_Int, values))
print(int_values)

# filter() 函数创建了一个迭代器，因此如果你想得到一个列表的话，就得像示例
# 那样使用 list() 去转换。
