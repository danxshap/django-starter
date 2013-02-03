from settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Django-storages S3 settings
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY', '') 
AWS_STORAGE_BUCKET_NAME = 'django_starter'
AWS_S3_SECURE_URLS = False
AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_AUTH = False

# Custom storage class that combines pipeline, S3, and staticfiles (for versioning)
STATICFILES_STORAGE = 'custom_storages.S3PipelineStorage'

# Pipeline compressors
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.cssmin.CssminCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'
PIPELINE_DISABLE_WRAPPER = True
