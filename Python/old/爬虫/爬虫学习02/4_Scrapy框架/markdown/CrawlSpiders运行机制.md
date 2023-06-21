# `crawlspiders`运行机制

1. 调度器从`start_urls`中取出第一个需要下载的url，入队列，然后下载器从队列中取出url发送请求，获取responses网页的内容
2. 通过该responses内容，按照 LinkExtractor 的提取规则，提取出符合规则的列表，将该列表传给 Rule
3. 调度器将 Rule 中符合规则的列表入队列，然后下载器再从队列中取出url发送请求，然后得到的 responses 交给 Rule 中定义的回调函数 callback 处理
4. 重复2，3操作，直到符合规则的 url 被提取完毕。
5. 入队列的 url 会有去重操作，这样可以保证不会对重复的 url 发送请求。

