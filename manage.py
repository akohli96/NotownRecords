#!/usr/bin/env python
import os
import sys
import django.conf as conf
if __name__ == "__main__":

    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file)))
    #print "IN MANAGE"
    #print BASE_DIR
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notown.settings")
    try:
        from django.core.management import execute_from_command_line
        print "HELLO FROM MANAGE"
        print conf.settings.DATABASES
        if 'SQLITE' in os.environ:
            print "FOUND SQLITE FROM MANAGE"
            
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
