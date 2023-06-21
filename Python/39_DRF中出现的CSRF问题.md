# Django rest framework 中出现的csrf问题

- 使用django-rest-framework时，前端通过ajax方式发送patch请求出现 csrf 问题

```error
CSRF Failed: CSRF token missing or incorrect
```

- 这个不是跨域问题，而是django的用户验证机制导致的

## 解决方式

- 在请求头中添加`X-CSRFToken`
- 值为 cookie 中的csrftoken

```JavaScript
function getCookie(name){
    /* 获取cookie中的csrftoken */
    var name = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++){
        var c = ca[i].trim();
        if (c.indexOf(name)==0) return c.substring(name.length,c.length);
    }
    return "";
}
```
