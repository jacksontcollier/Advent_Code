#!/usr/bin/env python3

from day11 import Password

orig_passwd = Password('vzbxkghb')
first_passwd = Password(orig_passwd.get_next_password())
print("First answer = %s" % first_passwd.get_string())
first_passwd.increment()
print("Second answer = %s" % first_passwd.get_next_password())
