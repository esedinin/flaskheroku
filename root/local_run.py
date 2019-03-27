#run server loclay

#important variable app from root/app.py file
from root.app import app


if __name__ == '__main__':
    app.debug = True
    app.run()