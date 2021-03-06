django-starter
==============

## Setup Local Environment
1.  Make new project directory, copy files, go there, and rename django project subdirectory
    ```
    mkdir /sites/<PROJECT_NAME>
    cp -r /sites/django-starter/ /sites/<PROJECT_NAME>
    cd /sites/<PROJECT_NAME>
    mv starter <PROJECT_NAME>
    ```

2.  Delete django-starter git repo

    ```
    rm -rf .git
    ```

3.  Create and activate a new virtualenv (requires virtualenv-wrapper)

    ```
    mkvirtualenv <PROJECT_NAME>
    workon <PROJECT_NAME>
    ```

4.  Install requirements

    ```
    pip install -r requirements.txt
    ```

5.  Create a database

    ```
    psql -U postgres
    postgres=# CREATE DATABASE <PROJECT_DB_NAME>;
    ```

6.  In settings.py, change name in `DATABASES` under dev section and update `TEMPLATE_DIRS` to be `/sites/<PROJECT_NAME>/<PROJECT_NAME>/templates`

7.  Initially sync database (creates user/session tables, etc...)

    ```
    python manage.py syncdb`
    ```

## Setup Production Environment
1.  Create S3 bucket on aws.amazon.com

2.  In settings.py, update `STATIC_URL` and `AWS_STORAGE_BUCKET_NAME`

3.  In collectstatic_settings.py, update `AWS_STORAGE_BUCKET_NAME`

4.  Open bash_profile and add AWS variables (for calling collectstatic and uploading to S3)
    
    ```
    vim ~/.bash_profile

    AWS_ACCESS_KEY_ID=<aws id>
    AWS_SECRET_ACCESS_KEY=<aws secret>

    source ~/.bash_profile
    ```

5.  Deploy static files
    
    ```
    fab collectstatic:ignore_admin=False
    ```

6.  Update path to manage.py in Procfile (replace `starter/` with `<PROJECT_NAME>/manage.py`)

7.  Create Heroku app

    ```
    cd /sites/<PROJECT_NAME>
    git init
    git add .
    git commit -m "first commit"
    heroku apps:create <PROJECT_NAME>
    ```

8.  Add Heroku configuration variables

    ```
    heroku config:add I_AM_HEROKU=1 DJANGO_SECRET_KEY=<some crazy string> AWS_ACCESS_KEY_ID=<aws key> AWS_SECRET_ACCESS_KEY=<aws secret>
    ```

9.  Deploy Django app to Heroku

    ```
    git push heroku master
    ```

10.  Run syncdb on Heroku

    ```
    heroku run python <PROJECT_NAME>/manage.py syncdb
    ```
