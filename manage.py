from application import *
from flask_script import Server

manage.add_command('runserver',Server(host='0.0.0.0',port='6000',use_debugger=True,use_reloader=True))

def main():

    manage.run()

if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()