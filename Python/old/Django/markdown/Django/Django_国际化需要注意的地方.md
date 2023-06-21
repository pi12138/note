# django国际化可能会出现的问题

## djangojs.mo无效

- 需要在settings文件中配置`LOCALE_PATHS`

    ```Python
    LOCALE_PATHS = (
        os.path.join(PROJECT_PATH, 'locale'),
        os.path.join(PROJECT_PATH, 'centers/locale'),
        os.path.join(PROJECT_PATH, 'hq/locale'),
    )
    ```

- 将需要执行国际化的app添加进去

## django国际化是如何找到翻译文件的

1. 先查询settings文件中的LOCALE_PATHS
2. 在查询INSTALLED_APPS中的每个app是否存在locale文件夹
3. 最后查询django/conf/locale提供的

