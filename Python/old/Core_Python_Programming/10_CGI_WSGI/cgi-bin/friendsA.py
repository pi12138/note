#!/usr/bin/env python3
import cgi


reshtml = """Content-Type: text/html\n
<html>
    <head>
        <title>Friends CGI Demo(dynamic screen)</title>
    </head>
    <body>
        <h3>Friend list for: <i>{}</i></h3>
        Your name is: <b>{}</b>
        You have <b>{}</b> friends.
    </body>
</html>
"""

form = cgi.FieldStorage()
who = form['person'].value
howmany = form['howmany'].value

print(reshtml.format(who, who, howmany))