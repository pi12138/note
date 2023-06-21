#!/usr/bin/env python3

import cgi


header = "Content-Type: text/html\n\n"

formhtml = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Friends CGI Demo (static screen)</title>
</head>
<body>
    <h3>Friend list for: <i>New USER</i></h3>
    <form action="/cgi-bin/friendsA.py">
        <b>Enter your name:</b>
        <input type="text" name="person" id="" value="NEW USER" size="15">
        <p>
            <b>How many friends do you have?</b>
            <input type="radio" name="howmany" value="0" checked> 0
            <input type="radio" name="howmany" value="10" checked> 10
            <input type="radio" name="howmany" value="25" checked> 25
            <input type="radio" name="howmany" value="50" checked> 50
            <input type="radio" name="howmany" value="100" checked> 100
        </p>
        <input type="submit">
    </form>
</body>
</html>
"""

def showForm():
    print(header + formhtml)


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

def doResults(who, howmany):
    print(header + reshtml.format(who, who, howmany))

def process():
    form = cgi.FieldStorage()
    if 'person' in form:
        who = form['person'].value
    else:
        who = "New User"

    if 'howmany' in form:
        howmany = form['howmany'].value
    else:
        howmany = 0
    
    if 'action' in form:
        doResults(who, howmany)
    else:
        showForm()


if __name__ == "__main__":
    process()