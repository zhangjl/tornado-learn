import sys

def one():
    two()

def two():
    three()

def three():
    for num in range(3):
        frame = sys._getframe(num)
        show_frame(num, frame)

def show_frame(num, frame):
    print frame
    print "  frame     = sys._getframe(%s)" % num
    print "  function  = %s()" % frame.f_code.co_name
    print "  file/line = %s:%s" % (frame.f_code.co_filename, frame.f_lineno)
    print "  back file/line = %s:%s" % (frame.f_back.f_code.co_filename, frame.f_back.f_lineno)

def test():
    frame = sys._getframe(1)
    show_frame(1, frame)

def aFunction():
    a = 1
    b = 'hello'
    c = (12, 3.45)
    test()
    d = "This won't show up in the frame"

class Test(object):
    a = 1
    b = 'hello'
    c = (12, 3.45)
    test()
    d = "This won't show up in the frame"

if '__main__' == __name__:
    one()
    aFunction()
