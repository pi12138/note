from io import StringIO
import formatter
from html.parser import HTMLParser
import http.client
import os
import sys
import urllib.request
from urllib.parse import urlparse, urljoin


class Retriever(object):
    __slots__ = ('url', 'file')
    
    def __init__(self, url):
        self.url, self.file = self.get_file(url)

    def get_file(self, url, default='index.html'):
        """Create usable local filename from URL"""
        parsed = urlparse(url)
        host = parsed.netloc.split('@')[-1].split(':')[0]
        filepath = '{}{}'.format(host, parsed.path)

        if not os.path.splitext(parsed.path)[1]:
            filepath = os.path.join(filepath, default)
        
        linkdir = os.path.dirname(filepath)
        if not os.path.isdir(linkdir):
            if os.path.exists(linkdir):
                os.unlink(linkdir)
            os.makedirs(linkdir)
        return url, filepath

    def download(self):
        """
        Download URL to specific named file
        """
        try:
            retval = urllib.request.urlretrieve(self.url, self.file)
        except (IOError, http.client.InvalidURL) as e:
            retval = (('*** ERROR: bad URL "{}": {}'.format(self.url, e)))

        return retval

    def parse_links(self):
        """
        parse out the links found in downloaded HTML file
        """
        f = open(self.file, 'r')
        data = f.read()
        f.close()

        parser = HTMLParser(formatter.AbstractFormatter(formatter.DumbWriter(StringIO())))
        parser.feed(data)
        parser.close()

        return parser.anchorlist

    
class Crawler(object):
    count = 0

    def __init__(self, url):
        self.q = [url]
        self.seen = set()
        parsed = urlparse(url)
        host = parsed.netloc.split('@')[-1].split(':')[0]
        self.dom = '.'.join(host.split('.')[-2:])

    def get_page(self, url, media=False):
        """
        Download page & parse links, add to queue of nec
        """
        r = Retriever(url)
        fname = r.download()[0]
        if fname[0] == '*':
            print('{} ...skipping parse'.format(fname))
            return 

        Crawler.count += 1
        print('\n({})'.format(Crawler.count))
        print('URL: {}'.format(url))
        print('FILE: {}'.format(fname))

        self.seen.add(url)
        ftype = os.path.splitext(fname)[1]
        if ftype not in ('.htm', '.html'):
            return

        for link in r.parse_links():
            if link.startswith('mailto:'):
                print('... discarded, mailto link')
                continue
            
            if not media:
                ftype = os.path.splitext(link)[1]
                if ftype in ('.mp3', '.mp4', '.m4v', '.wav'):
                    print('... discarded, media file')
                    continue
            
            if not link.startswith('http://'):
                link = urljoin(url, link)
            print('* {}'.format(link))
        
            if link not in self.seen:
                if self.dom not in link:
                    print('... discarded, not in domain')
                else:
                    if link not in self.q:
                        self.q.append(link)
                        print('... new, added to Q')
                    else:
                        print('... discard, already in Q')
            else:
                print('... discarded, already processed')

    def go(self, media=False):
        """
        Process nex page in queue (if any)
        """
        while self.q:
            url = self.q.pop()
            self.get_page(url, media)


def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        try:
            url = input('Enter starting URL: ')
        except (KeyboardInterrupt, EOFError):
            url = ''

    if not url:
        return
    if not url.startswith('http://') and not url.startswith('ftp://'):
        url = 'http://{}/'.format(url)

    robot = Crawler(url)
    robot.go()


if __name__ == "__main__":
    main()