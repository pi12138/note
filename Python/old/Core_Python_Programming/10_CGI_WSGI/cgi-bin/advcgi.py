#!/usr/bin/env python3

from cgi import FieldStorage
from os import environ
from io import StringIO
from urllib.parse import quote, unquote


class AdvCGI(object):
    header = 'Content-Type: text/html\n\n'
    url = '/cgi-bin/advcgi.py'

    form_html = """
    <html>
        <head>
            <title>Advanced CGI Demo</title>
        </head>
        <body>
            <h2>Advanced CGI Demo Form</h2> 
            <form action="{}" method="POST" enctype="multipart/form-data">
                <h3>My Cookie Setting</h3>
                <code><b>CPPuser = {}</b></code>
                <h3>Enter Cookie value <br>
                <input type="text" name='cookie' value="{}"> (<i>optional</i>)
                </h3>
                <h3>
                    Enter your name <br>
                    <input type="text" name='person' value="{}"> (<i>required</i>)
                </h3>
                <h3>
                    What languages can you program in ? (<i>at least one required</i>)
                </h3>
                {}
                <h3>Enter file to upload <small>(max size 4K)</small></h3>
                <input type="file" name="upfile" value="{}" size="45">
                <p> <input type="submit" value="submit">
            </form>
        </body>
    </html>
    """

    lang_set = ('Python', 'Ruby', 'Java', 'C++', 'PHP', 'C', 'JavaScript')
    lang_item = '<input type="checkbox" name="lang" value="{}" {}> {}\n'

    def getCPPCookies(self):
        if 'HTTP_COOKIE' in environ:
            cookies = [x.strip() for x in environ['HTTP_COOKIE'].split(';')]
            for eachCookie in cookies:
                if len(eachCookie) > 6 and eachCookie[:3] == 'CPP':
                    tag = eachCookie[3:7]
                    try:
                        self.cookies[tag] = eval(unquote(eachCookie[8:]))
                    except (NameError, SyntaxError):
                        self.cookies[tag] = unquote(eachCookie[8:])

            if 'info' not in self.cookies:
                self.cookies['info'] = ''
            if 'user' not in self.cookies:
                self.cookies['user'] = ''
        else:
            self.cookies['info'] = self.cookies['user'] = ''

        if self.cookies['info'] != '':
            self.who, lang_str, self.fn = self.cookies['info'].split(':')
            self.langs = lang_str.split(',')
        else:
            self.who = self.fn = ' '
            self.langs = ['Python']

    def showForm(self):
        self.getCPPCookies()

        lang_str = []
        for eachLang in AdvCGI.lang_set:
            lang_str.append(AdvCGI.lang_item.format(eachLang, 'CHECKED' if eachLang in self.langs else "", eachLang))
        
        if not ('user' in self.cookies and self.cookies['user']):
            cookStatus = '<i>(cookie has not been set yet)<i>'
            userCook = ''
        else:
            userCook = cookStatus = self.cookies['user']

        print('{}{}'.format(AdvCGI.header, AdvCGI.form_html.format(AdvCGI.url, cookStatus, userCook, self.who, ''.join(lang_str), self.fn)))

    err_html = """
    <html>
        <head>
            <title>Advanced CGi Demo</title>
        </head>
        <body>
            <h3>ERROR</h3>
            <b>{}</b>
            <form action="">
                <input type="button" value="back" onclick="window.history.back()">
            </form>
        </body>
    </html>    
    """     

    def showError(self):
        print(AdvCGI.header + AdvCGI.err_html.format(self.error))

    res_html = """
    <html>
        <head>
            <title>Advanced CGi Demo</title>
        </head>
        <body>
            <h2>Your Uploaded Data</h2>
            <h3>Your cookie value is: <b>{}</b></h3>
            <h3>Your name is: <b>{}</b></h3>
            <h3>You can program in the following languages: </h3>
            <ul>{}</ul>
            <h3>Your uploded file...
                <br>
                Name: <i>{}</i><br>
                Contents:
            </h3>
            <pre>{}</pre>
            Click <a href="{}"><b>here</b></a> to return to form.
        </body>
    </html>    
    """

    def setCPPCookies(self):
        for eachCookie in self.cookies.keys():
            print('Set-Cookie: CPP{}={}; path=/'.format(eachCookie, quote(self.cookies[eachCookie])))

    def doResults(self):
        MAXBYTES = 4096
        lang_list = ''.join('<li>{}<br>'.format(eachLang for eachLang in self.langs))
        filedata = self.fp.read(MAXBYTES)
        if len(filedata) == MAXBYTES and self.fp.read():
            filedata = '{}{}'.format(filedata, '... <b><i>(file truncated due to size)</i></b>')
        self.fp.close()

        if filedata == "":
            filedata = '<b><i>(file not given or uplaod error)</i></b>'
        filename = self.fn

        if not ('user' in self.cookies and self.cookies['user']):
            cookStatus = '<i>(cookie has not been set yet)</i>'
            userCook = ''
        else:
            userCook = cookStatus = self.cookies['user']

        self.cookies['info'] = ':'.join((self.who, ','.join(self.langs), filename))
        self.setCPPCookies()

        print('{}{}'.format(AdvCGI.header, AdvCGI.res_html.format(cookStatus, self.who, lang_list, filename, filedata, AdvCGI.url)))

    def go(self):
        self.cookies = {}
        self.error = ''
        form = FieldStorage()

        if not form.keys():
            self.showForm()
            return
        
        if 'person' in form:
            self.who = form['person'].value.strip().title()
            if self.who == '':
                self.error = 'Your name is required. (blank)'
        else:
            self.error = 'Your name is required. (missing)'

        self.cookies['user'] = unquote(form['cookies'].value.strip()) if 'cookies' in form else ''
        
        if 'lang' in form:
            lang_data = form['lang']
            if isinstance(lang_data, list):
                self.langs = [eachLang.value for eachLang in lang_data]
            else:
                self.langs = [lang_data.value]
        else:
            self.error = 'At least one language required'

        if 'upfile' in form:
            upfile = form['upfile']
            self.fn = upfile.filename or ''
            if upfile.file:
                self.fp = upfile.file
            else:
                self.fp = StringIO('(no data)')
        else:
            self.fp = StringIO('(no file)')
            self.fn = ''

        if not self.error:
            self.doResults()
        else:
            self.showError()


if __name__ == "__main__":
    page = AdvCGI()
    page.go()