#! /usr/bin/env python
#! -*- encoding: utf-8 -*-
import sys
from datetime import datetime, timedelta

import base

import tornado
from tornado.options import define, options

define('config', type = str, help = 'path to config file',
        callback = lambda path: tornado.options.parse_config_file(path, final = False))

define('passwd', type = str)
define('test', type = int, default = 0, help = 'switch: is test')
define('name', type = str, default = 'zhangjl', help = 'username')

'''
    python src/options.py -zl=0:2 -dt='2015-02-19 15:00:00' -bl=1 -td='10d 4h'
'''

define('zl', type = int, default = range(0,2), multiple = True, help = 'range of 0 to 1')
define('dt', type = datetime, default = datetime.today(), help = 'date time')
define('bl', type = bool, default = False, help = 'test bool type')
define('td', type = timedelta, help = 'test time delta')

print tornado.options.parse_command_line()

'''
如果此时参数中传递了xxx，则会报错
define('xxx', type = str, default = 'xxx', help = 'test parse_command_line method')
'''

for name, value in options.items():
    if name in ('log_file_num_backups', 'logging', 'help', 'log_to_stderr', 'log_file_max_size', 'log_file_prefix'):
        continue
    print "%s: %s" % (name, value)

frame = sys._getframe(0)
print frame.f_code.co_filename
