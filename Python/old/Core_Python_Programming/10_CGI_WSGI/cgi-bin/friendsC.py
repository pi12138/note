#!/usr/bin/env python3

import cgi
from urllib.parse import quote_plus


header = 'Content-Type: text/html\n\n'
url = '/cgi-bin/friendsC.py'

err_html = """
    <html>
        <head>
            <title>Friends CGI Demo</title>
        </head>
        <body>
            <h3>Error</h3>
            <b>{}</b>
            <form>
                <input type="button" value="back" onclick="window.history.back()">
            </form>
        </body>
    </html>
"""

def showError(error_str):
    print(header + err_html.format(error_str))

formhtml = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Friends CGI Demo (static screen)</title>
</head>
<body>
    <h3>Friend list for: <i>{}</i></h3>
    <form action="{}">
        <b>Enter your name:</b>
        <input type="hidden" name="action" value="edit">
        <input type="text" name="person" id="" value="{}" size="15">
        <p>
            <b>How many friends do you have?</b>
            {}
        </p>
        <input type="submit">
    </form>
</body>
</html>
"""

fradio = '<input type="radio" name="howmany" value="{}" {}> {}\n'

def showForm(who, howmany):
    friends = []
    for i in (0, 10, 25, 50, 100):
        checked = ''
        if str(i) == howmany:
            checked = 'CHECKED'
        friends.append(fradio.format(str(i), checked, str(i)))
    print('{}{}'.format(header, formhtml.format(who, url, who, ''.join(friends))))

reshtml = """Content-Type: text/html\n
<html>
    <head>
        <title>Friends CGI Demo(dynamic screen)</title>
    </head>
    <body>
        <h3>Friend list for: <i>{}</i></h3>
        Your name is: <b>{}</b>
        You have <b>{}</b> friends.
        <p>Click <a href="{}">here</a> to edit you data again.
    </body>
</html>
"""

def doResults(who, howmany):
    newurl = url + "?action=reedit&person={}&howmany={}".format(quote_plus(who), howmany)
    print(header + reshtml.format(who, who, howmany, newurl))

def process():
    error = ''
    form = cgi.FieldStorage()

    if 'person' in form:
        who = form['person'].value.title()
    else:
        who = "New User"

    if 'howmany' in form:
        howmany = form['howmany'].value
    else:
        if 'action' in form and form['action'].value == 'edit':
            error = 'Please select number of friends'
        else:
            howmany = 0

    if not error:
        if 'action' in form and form['action'].value != 'reedit':
            doResults(who, howmany)
        else:
            showForm(who, howmany)
    else:
        showError(error)


if __name__ == "__main__":
    process()