# The Grinder 3.11
# HTTP script recorded by TCPProxy at Nov 8, 2013 8:22:29 AM

from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPPluginControl, HTTPRequest
from HTTPClient import NVPair
connectionDefaults = HTTPPluginControl.getConnectionDefaults()
httpUtilities = HTTPPluginControl.getHTTPUtilities()

# To use a proxy server, uncomment the next line and set the host and port.
# connectionDefaults.setProxyServer("host01.example.com", 8001)

def createRequest(test, url, headers=None):
    """Create an instrumented HTTPRequest."""
    request = HTTPRequest(url=url)
    if headers: request.headers=headers
    test.record(request, HTTPRequest.getHttpMethodFilter())
    return request

# These definitions at the top level of the file are evaluated once,
# when the worker process is started.

connectionDefaults.defaultHeaders = \
  [ NVPair('Accept-Encoding', 'gzip, deflate'),
    NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.12) Gecko/20130108 Firefox/10.0.12'),
    NVPair('Accept-Language', 'en-us,en;q=0.5'), ]

url0 = 'http://host01.example.com:7777'

request101 = createRequest(Test(101, 'GET dispatch'), url0)

request201 = createRequest(Test(201, 'GET dispatch'), url0)

request301 = createRequest(Test(301, 'GET dispatch'), url0)

request401 = createRequest(Test(401, 'GET dispatch'), url0)

request501 = createRequest(Test(501, 'GET dispatch'), url0)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """GET dispatch (request 101)."""
    self.token_operation = \
      'browse'
    result = request101.GET('/supplies/dispatch' +
      '?operation=' +
      self.token_operation, None,
      ( NVPair('Referer', 'http://host01.example.com:7777/supplies/'), ))

    return result

  def page2(self):
    """GET dispatch (request 201)."""
    self.token_operation = \
      'addItem'
    self.token_sku = \
      '1'
    result = request201.GET('/supplies/dispatch' +
      '?operation=' +
      self.token_operation +
      '&sku=' +
      self.token_sku, None,
      ( NVPair('Referer', 'http://host01.example.com:7777/supplies/dispatch?operation=browse'), ))

    return result

  def page3(self):
    """GET dispatch (request 301)."""
    self.token_sku = \
      '2'
    result = request301.GET('/supplies/dispatch' +
      '?operation=' +
      self.token_operation +
      '&sku=' +
      self.token_sku, None,
      ( NVPair('Referer', 'http://host01.example.com:7777/supplies/dispatch?operation=addItem&sku=1'), ))

    return result

  def page4(self):
    """GET dispatch (request 401)."""
    self.token_sku = \
      '3'
    result = request401.GET('/supplies/dispatch' +
      '?operation=' +
      self.token_operation +
      '&sku=' +
      self.token_sku, None,
      ( NVPair('Referer', 'http://host01.example.com:7777/supplies/dispatch?operation=addItem&sku=2'), ))

    return result

  def page5(self):
    """GET dispatch (request 501)."""
    self.token_sku = \
      '16'
    result = request501.GET('/supplies/dispatch' +
      '?operation=' +
      self.token_operation +
      '&sku=' +
      self.token_sku, None,
      ( NVPair('Referer', 'http://host01.example.com:7777/supplies/dispatch?operation=addItem&sku=3'), ))

    return result

  def __call__(self):
    """Called for every run performed by the worker thread."""
    self.page1()      # GET dispatch (request 101)

    grinder.sleep(3244)
    self.page2()      # GET dispatch (request 201)

    grinder.sleep(1986)
    self.page3()      # GET dispatch (request 301)

    grinder.sleep(2933)
    self.page4()      # GET dispatch (request 401)

    grinder.sleep(3183)
    self.page5()      # GET dispatch (request 501)


# Instrument page methods.
Test(100, 'Page 1').record(TestRunner.page1)
Test(200, 'Page 2').record(TestRunner.page2)
Test(300, 'Page 3').record(TestRunner.page3)
Test(400, 'Page 4').record(TestRunner.page4)
Test(500, 'Page 5').record(TestRunner.page5)
