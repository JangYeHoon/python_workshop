class ClassTest:
    class_variable = 10

    def __init__(self, instance_v):
        self.instance_v = instance_v

c1 = ClassTest(10)
c2 = ClassTest(10)

c1.instance_v += 1
c2.instance_v += 1
print("{} c1.instance_v, {} c2.instance_v ".format(c1.instance_v, c2.instance_v))

# ClassTest.class_variable += 1
c1.class_variable +=1 
print("{} c1.class_variable".format(ClassTest.class_variable))
# ClassTest.class_variable += 1
c2.class_variable += 1
ClassTest.class_variable += 1
print("{} c2.class_variable".format(ClassTest.class_variable))
print("{} c1.class_variable, {} c2.class_variable ".format(c1.class_variable, c2.class_variable))