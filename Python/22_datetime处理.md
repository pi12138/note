# datetime

## 时间转字符串

- datetime.strftime('%Y-%m-%d %H:%M:%S')

## 字符串转时间

- datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')

## 带时区数据

- UTC时间转字符串
	- datetime_obj.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
	
- UTC时间字符串转datetime
	- datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=pytz.UTC)
	
## datetime获取UTC时间

- datetime.datetime.now(tz=pytz.UTC)
