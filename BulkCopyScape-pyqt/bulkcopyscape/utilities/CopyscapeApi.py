import sys
import urllib
if sys.hexversion < 0x02050000:
    import elementtree.ElementTree as CopyscapeTree
else:
    import xml.etree.ElementTree as CopyscapeTree
isPython2 = sys.hexversion < 0x03000000
if isPython2:
    import urllib2
else:
    import urllib.request
    import urllib.error


class CopyscapeApi(object):
    @property
    def uname(self):
        return self._uname

    @uname.setter
    def uname(self, val):
        self._uname = val

    @property
    def apiKey(self):
        return self._apiKey

    @apiKey.setter
    def apiKey(self, val):
        self._apiKey = val

    def __init__(self):
        self._copyscapeUrl = "http://www.copyscape.com/api/"

    # B. Functions for you to use (all accounts)
    def copyscape_api_url_search_internet(self, url, full=0):
        return self.copyscape_api_url_search(url, full, 'csearch')

    def copyscape_api_text_search_internet(self, text, encoding, full=0):
        return self.copyscape_api_text_search(text, encoding, full, 'csearch')

    def copyscape_api_check_balance(self):
        return self.copyscape_api_call('balance')

    # C. Functions for you to use (only accounts with private index enabled)
    def copyscape_api_url_search_private(self, url, full=0):
        return self.copyscape_api_url_search(url, full, 'psearch')

    def copyscape_api_url_search_internet_and_private(self, url, full=0):
        return self.copyscape_api_url_search(url, full, 'cpsearch')

    def copyscape_api_text_search_private(self, text, encoding, full=0):
        return self.copyscape_api_text_search(text, encoding, full, 'psearch')

    def copyscape_api_text_search_internet_and_private(self, text, encoding, full=0):
        return self.copyscape_api_text_search(text, encoding, full, 'cpsearch')

    def copyscape_api_url_add_to_private(self, url, id=None):
        params = {}
        params['q'] = url
        if id is not None:
            params['i'] = id

        return self.copyscape_api_call('pindexadd', params)

    def copyscape_api_text_add_to_private(self, text, encoding, title=None, id=None):
        params = {}
        params['e'] = encoding
        if title is not None:
            params['a'] = title
        if id != None:
            params['i'] = id

        return self.copyscape_api_call('pindexadd', params, text)

    def copyscape_api_delete_from_private(self, handle):
        params = {}
        if handle is None:
            params['h'] = ''
        else:
            params['h'] = handle

        return self.copyscape_api_call('pindexdel', params)

    # D. Functions used internally
    def copyscape_api_url_search(self, url, full=0, operation='csearch'):
        params = {}
        params['q'] = url
        params['c'] = str(full)

        return self.copyscape_api_call(operation, params)

    def copyscape_api_text_search(self, text, encoding, full=0, operation='csearch'):
        params = {}
        params['e'] = encoding
        params['c'] = str(full)

        return self.copyscape_api_call(operation, params, text)

    def copyscape_api_call(self, operation, params={}, postdata=None):
        urlparams = {}
        urlparams['u'] = self._uname
        urlparams['k'] = self._apiKey
        urlparams['o'] = operation
        urlparams.update(params)

        uri = self._copyscapeUrl + '?'

        request = None
        if isPython2:
            uri += urllib.urlencode(urlparams)
            if postdata is None:
                request = urllib2.Request(uri)
            else:
                request = urllib2.Request(uri, postdata.encode("UTF-8"))
        else:
            uri += urllib.parse.urlencode(urlparams)
            if postdata is None:
                request = urllib.request.Request(uri)
            else:
                request = urllib.request.Request(uri, postdata.encode("UTF-8"))

        try:
            response = None
            if isPython2:
                response = urllib2.urlopen(request)
            else:
                response = urllib.request.urlopen(request)
            res = response.read()
            return res
        except Exception:
            e = sys.exc_info()[1]
            print(e.args[0])

        return None

    def copyscape_title_wrap(self, title):
        return title + ":"

    def copyscape_node_wrap(self, element):
        return self.copyscape_node_recurse(element)

    def copyscape_node_recurse(self, element, depth=0):
        ret = ""
        if element is None:
            return ret

        ret += "\t" * depth + " " + element.tag + ": "
        if element.text is not None:
            ret += element.text.strip()
        ret += "\n"
        for child in element:
            ret += self.copyscape_node_recurse(child, depth + 1)

        return ret