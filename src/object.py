#! /usr/bin/env python
#! -*- encoding: utf-8 -*-

class Zhangjl(object):
    '''
    this is a test of Object
    test for __dict__
    '''

    def __init__(self, name, birth):
        self.__dict__['_name'] = name
        self.__dict__['_birth'] = birth

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        else:
            return None

    def __setattr__(self, name, value):
        if name in self.__dict__:
            self.__dict__[name] = value

if '__main__' == __name__:
    zjl = Zhangjl('zhangjl', '1988-10-22')
    print 'name: %s, birth: %s' % (zjl._name, zjl._birth)
