# `Django设置Log`

- 设置控制台可以看到

  ```python
  LOGGING = {
      'version': 1,
      'disable_existing_loggers': False,
      'formatters': {
          'simple': {
              'format': '[%(asctime)s] %(message)s'
          },
      },
      'handlers': {
          'console': {
              'level': 'DEBUG',
              'class': 'logging.StreamHandler',
              'formatter': 'simple'
          },
      },
      'loggers': {
          'django': {
              'handlers': ['console'],
              'level': 'DEBUG',
          },
      },
  }
  ```

- 设置写入文件

  ```python
  LOGGING = {
      'version': 1,
      'disable_existing_loggers': False,
      'handlers': {
          'file': {
              'level': 'DEBUG',
              'class': 'logging.FileHandler',
              'filename': 'debug.log',
          },
      },
      'loggers': {
          'django': {
              'handlers': ['file'],
              'level': 'DEBUG',
              'propagate': True,
          },
      },
  }
  ```

  