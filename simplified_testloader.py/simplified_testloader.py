#!/usr/bin/env python
# coding: utf-8

# In[1]:


module = __import__("__main__")


# In[2]:


dir(module)


# In[12]:


import unittest

class MyTestCase(unittest.TestCase):
    def test_1(self):
        print("in MyTestCase::test_1")
    def test_2(self):
        print("in MyTestCase::test_2")



# In[13]:


def loadTests():
    module = __import__("__main__")
    tests = list()
    for field in dir(module):

        attr = getattr(module, field)
        if isinstance(attr, type) and issubclass(attr, unittest.TestCase):
            tests.append(attr)

    return tests

def runTests(tests):
    for testcase in tests:
        obj = testcase()
        for field in  sorted(dir(obj)):
            attr = getattr(obj, field)
            if field.startswith("test") and callable(attr):
                attr()
tests = loadTests()
runTests(tests)


# In[ ]:




