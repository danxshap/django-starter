import boto
from fabric.api import task, local

import collectstatic_settings

@task
def deploy_production():
    collectstatic()
    local('git push heroku master')

@task
def python_deploy_production():
    local('git push heroku master')

@task
def collectstatic(ignore_admin=True):
    # Delete existing files (not admin)
    s3 = boto.connect_s3()
    bucket = s3.get_bucket(collectstatic_settings.AWS_STORAGE_BUCKET_NAME)
    bucketListResultSet = bucket.list()
    bucket.delete_keys([key.name for key in bucketListResultSet if not key.name.startswith('admin/')])
    
    ignore_flag = '--ignore=admin' if ignore_admin != 'False' else '' 
    
    # Ignore admin
    local('python manage.py collectstatic --noinput {0} --settings=collectstatic_settings'
        .format(ignore_flag))
