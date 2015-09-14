__author__ = 'wwh'

#一个可迭代的对象，获取其中指定的元素

#求平均值函数
def avg(mid):
    sum = 0
    for i in range(len(mid)):
        print(i,mid[i])
        sum += mid[i]
    return sum/(i+1)

#去除首尾元素求平均值
def drop_first_last(grades):
    # *号是可变参数,表示一个元组
    # **号也是可变参数,表示键值
    first, *middle, last = grades
    print(type(middle))
    return avg(middle)

if __name__ == '__main__':
    #任意可迭代的元素都可以分解为单独的变量
    t = (1,2,3)
    x,y,z = t
    print(x,y,z)
    s = 'hello'
    a,b,c,d,e = s
    print(a,b,c,d,e)
    #给出一组成绩，求其平均值
    student_grade = [88,99,100,65,78,66]
    print(drop_first_last(student_grade))
