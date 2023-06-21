# Request和Response

## DRF的Request对象

1. `.data`: DRF 请求对象的 `data` 属性包含了所有的上传对象，甚至包括文件对象！也就是说，我们可以只通过访问 `resquest.data` 就能得到所有的上传数据，包括 `PUT` 请求的！还支持多种数据上传格式，前端不仅可以以 form 的形式上传，还可以以 `json` 等众多其它形式上传数据！
2. `.query_params`: `query_params` 属性包含了所有的 URL 参数，不仅仅是 GET 请求的参数，任何请求方法 URL 参数都会被解析到这里。
3. `.user`: 和原生的 `user` 属性作用相同。
4. `.auth`： 包含额外的认证信息。

## DRF的Response对象

1. `data`: 被序列化之后的数据。将被用作响应数据传给前端。
2. `status`: 状态码。
3. `headers`: 响应头。
4. `content_type`: 响应类型。一般不需要我们手动设置这个字段。