# The Grinder 3.11
# HTTP script recorded by TCPProxy at Nov 27, 2013 11:39:59 AM

from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPPluginControl, HTTPRequest
from HTTPClient import NVPair
connectionDefaults = HTTPPluginControl.getConnectionDefaults()
httpUtilities = HTTPPluginControl.getHTTPUtilities()

# To use a proxy server, uncomment the next line and set the host and port.
# connectionDefaults.setProxyServer("localhost", 8001)

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
    NVPair('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.12) Gecko/20130108 Firefox/10.0.12'),
    NVPair('Accept-Language', 'en-us,en;q=0.5'), ]

headers0= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'), ]

headers1= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://host01.example.com:7011/benefits/welcome.html'), ]

url0 = 'http://host01.example.com:7011'

request101 = createRequest(Test(101, 'GET benefits'), url0, headers0)

request102 = createRequest(Test(102, 'GET /'), url0, headers0)

request103 = createRequest(Test(103, 'GET styles.css'), url0)

request104 = createRequest(Test(104, 'GET favicon.ico'), url0)

request105 = createRequest(Test(105, 'GET favicon.ico'), url0, headers0)

request201 = createRequest(Test(201, 'POST servlet'), url0)

request301 = createRequest(Test(301, 'GET welcome.html'), url0)

request401 = createRequest(Test(401, 'POST servlet'), url0, headers1)

request501 = createRequest(Test(501, 'POST servlet'), url0, headers1)

request601 = createRequest(Test(601, 'POST servlet'), url0, headers1)

request701 = createRequest(Test(701, 'POST servlet'), url0, headers1)

request801 = createRequest(Test(801, 'POST servlet'), url0, headers1)

request901 = createRequest(Test(901, 'POST servlet'), url0, headers1)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """GET benefits (requests 101-105)."""
    
    # Expecting 302 'Moved Temporarily'
    result = request101.GET('/benefits')

    grinder.sleep(12)
    request102.GET('/benefits/')

    grinder.sleep(116)
    request103.GET('/benefits/css/styles.css', None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://host01.example.com:7011/benefits/'), ))

    grinder.sleep(111)
    request104.GET('/favicon.ico', None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'), ))

    request105.GET('/favicon.ico')

    return result

  def page2(self):
    """POST servlet (request 201)."""
    result = request201.POST('/benefits/servlet',
      ( NVPair('benefit', 'holiday'),
        NVPair('benefit', 'health'),
        NVPair('benefit', 'vision'),
        NVPair('benefit', 'dental'), ),
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://host01.example.com:7011/benefits/'),
        NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))

    return result

  def page3(self):
    """GET welcome.html (request 301)."""
    result = request301.GET('/benefits/welcome.html', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://host01.example.com:7011/benefits/servlet'), ))

    return result

  def page4(self):
    """POST servlet (request 401)."""
    result = request401.POST('/benefits/servlet',
      ( NVPair('benefit', 'holiday'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))

    return result

  def page5(self):
    """POST servlet (request 501)."""
    result = request501.POST('/benefits/servlet',
      ( NVPair('benefit', 'dental'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))

    return result

  def page6(self):
    """POST servlet (request 601)."""
    result = request601.POST('/benefits/servlet',
      ( NVPair('benefit', 'vision'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))

    return result

  def page7(self):
    """POST servlet (request 701)."""
    result = request701.POST('/benefits/servlet',
      ( NVPair('benefit', 'health'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))

    return result

  def page8(self):
    """POST servlet (request 801)."""
    result = request801.POST('/benefits/servlet',
      ( NVPair('benefit', 'holiday'),
        NVPair('benefit', 'health'),
        NVPair('benefit', 'vision'),
        NVPair('benefit', 'dental'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))

    return result

  def page9(self):
    """POST servlet (request 901)."""
    result = request901.POST('/benefits/servlet',
      '',
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))

    return result

  def __call__(self):
    """Called for every run performed by the worker thread."""
    self.page1()      # GET benefits (requests 101-105)

    grinder.sleep(7430)
    self.page2()      # POST servlet (request 201)

    grinder.sleep(8855)
    self.page3()      # GET welcome.html (request 301)

    grinder.sleep(2748)
    self.page4()      # POST servlet (request 401)

    grinder.sleep(5965)
    self.page5()      # POST servlet (request 501)

    grinder.sleep(3752)
    self.page6()      # POST servlet (request 601)

    grinder.sleep(4243)
    self.page7()      # POST servlet (request 701)

    grinder.sleep(6227)
    self.page8()      # POST servlet (request 801)

    grinder.sleep(6518)
    self.page9()      # POST servlet (request 901)


# Instrument page methods.
Test(100, 'Page 1').record(TestRunner.page1)
Test(200, 'Page 2').record(TestRunner.page2)
Test(300, 'Page 3').record(TestRunner.page3)
Test(400, 'Page 4').record(TestRunner.page4)
Test(500, 'Page 5').record(TestRunner.page5)
Test(600, 'Page 6').record(TestRunner.page6)
Test(700, 'Page 7').record(TestRunner.page7)
Test(800, 'Page 8').record(TestRunner.page8)
Test(900, 'Page 9').record(TestRunner.page9)
