#!/usr/bin/env python
import os
import sys

if__name__ == "__main__":
     os.environ.setdeflault("DJANGO_SETTINGS_MODULE" , "blog.setting")

     from django.core.management import execute_from_command_line

     execute_from_command_line(sys.argv)