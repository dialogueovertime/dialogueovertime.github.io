import sys
sys.path.insert(0,'/vagrant/src')

from dotblog import create_app
application = create_app()