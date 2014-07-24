""" Deployment of your moerae project.
"""

from fabric.api import *

env.hosts = ['youhosthere']
env.user = "youruser"

def update_moerae_project():
    """ Updates the remote moerae project.
    """
    with cd('your/moerae/directory'):
        run('git pull')
        with prefix('source your/env/directory/bin/activate'):
            run('pip install -r requirement.txt')
            run('python manage.py syncdb')
#            run('python manage.py migrate') # if you use south
            run('python manage.py collectstatic --noinput')

def restart_webserver():
    """ Restarts remote nginx and uwsgi.
    """
    sudo("service uwsgi restart")
    sudo("/etc/init.d/nginx restart")

def deploy():
    """ Deploy Moerae Project.
    """
    update_moerae_project()
    restart_webserver()
