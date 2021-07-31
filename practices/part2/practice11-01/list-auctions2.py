
# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

# The Grinder 3.11
# HTTP script recorded by TCPProxy at Mar 18, 2013 7:36:32 PM

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
    NVPair('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:10.f0.12) Gecko/20130108 Firefox/10.0.12'),
    NVPair('Accept-Language', 'en-us,en;q=0.5'), ]

headers0= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://host01:7011/SimpleAuctionWebAppDb2/ListServlet;jsessionid=pJ1_ARKuTkLdf3CUjA9QdC7loA3mDcZIJDh85BNRiyTRD8vORvYy!-406544328'), ]

headers1= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://host01:7011/SimpleAuctionWebAppDb2/'), ]

headers2= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://host01:7011/SimpleAuctionWebAppDb2/ListServlet'), ]

headers3= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://host01:7011/SimpleAuctionWebAppDb2/ListServlet'), ]

url0 = 'http://host01:7011'

request101 = createRequest(Test(101, 'GET index.jsp'), url0)

request201 = createRequest(Test(201, 'GET styles.css'), url0)

request301 = createRequest(Test(301, 'GET ListServlet'), url0)

request401 = createRequest(Test(401, 'GET AuctionImageServlet'), url0, headers0)

request501 = createRequest(Test(501, 'GET AuctionImageServlet'), url0, headers0)

request601 = createRequest(Test(601, 'GET AuctionImageServlet'), url0, headers0)

request701 = createRequest(Test(701, 'GET AuctionImageServlet'), url0, headers0)

request801 = createRequest(Test(801, 'GET AuctionImageServlet'), url0, headers0)

request901 = createRequest(Test(901, 'GET AuctionImageServlet'), url0, headers0)

request1001 = createRequest(Test(1001, 'GET AuctionImageServlet'), url0, headers0)

request1101 = createRequest(Test(1101, 'GET AuctionImageServlet'), url0, headers0)

request1201 = createRequest(Test(1201, 'GET DetailServlet'), url0)

request1301 = createRequest(Test(1301, 'GET AuctionImageServlet'), url0)

request1401 = createRequest(Test(1401, 'GET /'), url0)

request1501 = createRequest(Test(1501, 'GET ListServlet'), url0, headers1)

request1601 = createRequest(Test(1601, 'GET AuctionImageServlet'), url0, headers2)

request1701 = createRequest(Test(1701, 'GET AuctionImageServlet'), url0, headers2)

request1801 = createRequest(Test(1801, 'GET AuctionImageServlet'), url0, headers2)

request1901 = createRequest(Test(1901, 'GET AuctionImageServlet'), url0, headers2)

request2001 = createRequest(Test(2001, 'GET AuctionImageServlet'), url0, headers2)

request2101 = createRequest(Test(2101, 'GET AuctionImageServlet'), url0, headers2)

request2201 = createRequest(Test(2201, 'GET AuctionImageServlet'), url0, headers2)

request2301 = createRequest(Test(2301, 'GET AuctionImageServlet'), url0, headers2)

request2401 = createRequest(Test(2401, 'GET DetailServlet'), url0, headers3)

request2501 = createRequest(Test(2501, 'GET AuctionImageServlet'), url0)

request2601 = createRequest(Test(2601, 'GET /'), url0)

request2701 = createRequest(Test(2701, 'GET ListServlet'), url0, headers1)

request2801 = createRequest(Test(2801, 'GET AuctionImageServlet'), url0, headers2)

request2901 = createRequest(Test(2901, 'GET AuctionImageServlet'), url0, headers2)

request3001 = createRequest(Test(3001, 'GET AuctionImageServlet'), url0, headers2)

request3101 = createRequest(Test(3101, 'GET AuctionImageServlet'), url0, headers2)

request3201 = createRequest(Test(3201, 'GET AuctionImageServlet'), url0, headers2)

request3301 = createRequest(Test(3301, 'GET AuctionImageServlet'), url0, headers2)

request3401 = createRequest(Test(3401, 'GET AuctionImageServlet'), url0, headers2)

request3501 = createRequest(Test(3501, 'GET AuctionImageServlet'), url0, headers2)

request3601 = createRequest(Test(3601, 'GET DetailServlet'), url0, headers3)

request3701 = createRequest(Test(3701, 'GET AuctionImageServlet'), url0)

request3801 = createRequest(Test(3801, 'GET /'), url0)

request3901 = createRequest(Test(3901, 'GET ListServlet'), url0, headers1)

request4001 = createRequest(Test(4001, 'GET AuctionImageServlet'), url0, headers2)

request4101 = createRequest(Test(4101, 'GET AuctionImageServlet'), url0, headers2)

request4201 = createRequest(Test(4201, 'GET AuctionImageServlet'), url0, headers2)

request4301 = createRequest(Test(4301, 'GET AuctionImageServlet'), url0, headers2)

request4401 = createRequest(Test(4401, 'GET AuctionImageServlet'), url0, headers2)

request4501 = createRequest(Test(4501, 'GET AuctionImageServlet'), url0, headers2)

request4601 = createRequest(Test(4601, 'GET AuctionImageServlet'), url0, headers2)

request4701 = createRequest(Test(4701, 'GET AuctionImageServlet'), url0, headers2)

request4801 = createRequest(Test(4801, 'GET DetailServlet'), url0, headers3)

request4901 = createRequest(Test(4901, 'GET AuctionImageServlet'), url0)

request5001 = createRequest(Test(5001, 'GET /'), url0)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """GET index.jsp (request 101)."""
    result = request101.GET('/SimpleAuctionWebAppDb2/index.jsp', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'), ))
    self.token_jsessionid = \
      httpUtilities.valueFromBodyURI('jsessionid') # 'pJ1_ARKuTkLdf3CUjA9QdC7loA3mDcZIJDh85BNR...'

    return result

  def page2(self):
    """GET styles.css (request 201)."""
    result = request201.GET('/SimpleAuctionWebAppDb2/res/styles.css;jsessionid=' +
      self.token_jsessionid, None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://host01:7011/SimpleAuctionWebAppDb2/index.jsp'), ))

    return result

  def page3(self):
    """GET ListServlet (request 301)."""
    result = request301.GET('/SimpleAuctionWebAppDb2/ListServlet;jsessionid=' +
      self.token_jsessionid, None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://host01:7011/SimpleAuctionWebAppDb2/index.jsp'), ))
    # 8 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '1'

    return result

  def page4(self):
    """GET AuctionImageServlet (request 401)."""
    self.token_imageId = \
      '1'
    self.token_mode = \
      'thumb'
    result = request401.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page5(self):
    """GET AuctionImageServlet (request 501)."""
    self.token_imageId = \
      '2'
    result = request501.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page6(self):
    """GET AuctionImageServlet (request 601)."""
    self.token_imageId = \
      '3'
    result = request601.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page7(self):
    """GET AuctionImageServlet (request 701)."""
    self.token_imageId = \
      '6'
    result = request701.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page8(self):
    """GET AuctionImageServlet (request 801)."""
    self.token_imageId = \
      '7'
    result = request801.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page9(self):
    """GET AuctionImageServlet (request 901)."""
    self.token_imageId = \
      '0'
    result = request901.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page10(self):
    """GET AuctionImageServlet (request 1001)."""
    self.token_imageId = \
      '5'
    result = request1001.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page11(self):
    """GET AuctionImageServlet (request 1101)."""
    self.token_imageId = \
      '4'
    result = request1101.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page12(self):
    """GET DetailServlet (request 1201)."""
    result = request1201.GET('/SimpleAuctionWebAppDb2/DetailServlet' +
      '?id=' +
      self.token_id, None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://host01:7011/SimpleAuctionWebAppDb2/ListServlet;jsessionid=pJ1_ARKuTkLdf3CUjA9QdC7loA3mDcZIJDh85BNRiyTRD8vORvYy!-406544328'), ))

    return result

  def page13(self):
    """GET AuctionImageServlet (request 1301)."""
    self.token_imageId = \
      '1'
    result = request1301.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId, None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://host01:7011/SimpleAuctionWebAppDb2/DetailServlet?id=1'), ))

    return result

  def page14(self):
    """GET / (request 1401)."""
    result = request1401.GET('/SimpleAuctionWebAppDb2/', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://host01:7011/SimpleAuctionWebAppDb2/DetailServlet?id=1'), ))

    return result

  def page15(self):
    """GET ListServlet (request 1501)."""
    result = request1501.GET('/SimpleAuctionWebAppDb2/ListServlet')
    # 7 different values for token_id found in response; the first matched
    # the last known value of token_id - don't update the variable.

    return result

  def page16(self):
    """GET AuctionImageServlet (request 1601)."""
    self.token_imageId = \
      '0'
    result = request1601.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page17(self):
    """GET AuctionImageServlet (request 1701)."""
    self.token_imageId = \
      '2'
    result = request1701.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page18(self):
    """GET AuctionImageServlet (request 1801)."""
    result = request1801.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page19(self):
    """GET AuctionImageServlet (request 1901)."""
    self.token_imageId = \
      '6'
    result = request1901.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page20(self):
    """GET AuctionImageServlet (request 2001)."""
    self.token_imageId = \
      '7'
    result = request2001.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page21(self):
    """GET AuctionImageServlet (request 2101)."""
    self.token_imageId = \
      '5'
    result = request2101.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page22(self):
    """GET AuctionImageServlet (request 2201)."""
    self.token_imageId = \
      '4'
    result = request2201.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page23(self):
    """GET AuctionImageServlet (request 2301)."""
    self.token_imageId = \
      '3'
    result = request2301.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page24(self):
    """GET DetailServlet (request 2401)."""
    self.token_id = \
      '2'
    result = request2401.GET('/SimpleAuctionWebAppDb2/DetailServlet' +
      '?id=' +
      self.token_id)

    return result

  def page25(self):
    """GET AuctionImageServlet (request 2501)."""
    self.token_imageId = \
      '2'
    result = request2501.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId, None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://host01:7011/SimpleAuctionWebAppDb2/DetailServlet?id=2'), ))

    return result

  def page26(self):
    """GET / (request 2601)."""
    result = request2601.GET('/SimpleAuctionWebAppDb2/', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://host01:7011/SimpleAuctionWebAppDb2/DetailServlet?id=2'), ))

    return result

  def page27(self):
    """GET ListServlet (request 2701)."""
    result = request2701.GET('/SimpleAuctionWebAppDb2/ListServlet')
    # 8 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '1'

    return result

  def page28(self):
    """GET AuctionImageServlet (request 2801)."""
    result = request2801.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page29(self):
    """GET AuctionImageServlet (request 2901)."""
    self.token_imageId = \
      '1'
    result = request2901.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page30(self):
    """GET AuctionImageServlet (request 3001)."""
    self.token_imageId = \
      '3'
    result = request3001.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page31(self):
    """GET AuctionImageServlet (request 3101)."""
    self.token_imageId = \
      '5'
    result = request3101.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page32(self):
    """GET AuctionImageServlet (request 3201)."""
    self.token_imageId = \
      '4'
    result = request3201.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page33(self):
    """GET AuctionImageServlet (request 3301)."""
    self.token_imageId = \
      '6'
    result = request3301.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page34(self):
    """GET AuctionImageServlet (request 3401)."""
    self.token_imageId = \
      '7'
    result = request3401.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page35(self):
    """GET AuctionImageServlet (request 3501)."""
    self.token_imageId = \
      '0'
    result = request3501.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page36(self):
    """GET DetailServlet (request 3601)."""
    self.token_id = \
      '3'
    result = request3601.GET('/SimpleAuctionWebAppDb2/DetailServlet' +
      '?id=' +
      self.token_id)

    return result

  def page37(self):
    """GET AuctionImageServlet (request 3701)."""
    self.token_imageId = \
      '3'
    result = request3701.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId, None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://host01:7011/SimpleAuctionWebAppDb2/DetailServlet?id=3'), ))

    return result

  def page38(self):
    """GET / (request 3801)."""
    result = request3801.GET('/SimpleAuctionWebAppDb2/', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://host01:7011/SimpleAuctionWebAppDb2/DetailServlet?id=3'), ))

    return result

  def page39(self):
    """GET ListServlet (request 3901)."""
    result = request3901.GET('/SimpleAuctionWebAppDb2/ListServlet')
    # 8 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '1'

    return result

  def page40(self):
    """GET AuctionImageServlet (request 4001)."""
    result = request4001.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page41(self):
    """GET AuctionImageServlet (request 4101)."""
    self.token_imageId = \
      '0'
    result = request4101.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page42(self):
    """GET AuctionImageServlet (request 4201)."""
    self.token_imageId = \
      '4'
    result = request4201.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page43(self):
    """GET AuctionImageServlet (request 4301)."""
    self.token_imageId = \
      '1'
    result = request4301.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page44(self):
    """GET AuctionImageServlet (request 4401)."""
    self.token_imageId = \
      '2'
    result = request4401.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page45(self):
    """GET AuctionImageServlet (request 4501)."""
    self.token_imageId = \
      '5'
    result = request4501.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page46(self):
    """GET AuctionImageServlet (request 4601)."""
    self.token_imageId = \
      '7'
    result = request4601.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page47(self):
    """GET AuctionImageServlet (request 4701)."""
    self.token_imageId = \
      '6'
    result = request4701.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page48(self):
    """GET DetailServlet (request 4801)."""
    self.token_id = \
      '4'
    result = request4801.GET('/SimpleAuctionWebAppDb2/DetailServlet' +
      '?id=' +
      self.token_id)

    return result

  def page49(self):
    """GET AuctionImageServlet (request 4901)."""
    self.token_imageId = \
      '4'
    result = request4901.GET('/SimpleAuctionWebAppDb2/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId, None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://host01:7011/SimpleAuctionWebAppDb2/DetailServlet?id=4'), ))

    return result

  def page50(self):
    """GET / (request 5001)."""
    result = request5001.GET('/SimpleAuctionWebAppDb2/', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://host01:7011/SimpleAuctionWebAppDb2/DetailServlet?id=4'), ))

    return result

  def __call__(self):
    """Called for every run performed by the worker thread."""
    self.page1()      # GET index.jsp (request 101)

    grinder.sleep(76)
    self.page2()      # GET styles.css (request 201)

    grinder.sleep(3333)
    self.page3()      # GET ListServlet (request 301)

    grinder.sleep(76)
    self.page4()      # GET AuctionImageServlet (request 401)
    self.page5()      # GET AuctionImageServlet (request 501)

    grinder.sleep(44)
    self.page6()      # GET AuctionImageServlet (request 601)
    self.page7()      # GET AuctionImageServlet (request 701)
    self.page8()      # GET AuctionImageServlet (request 801)
    self.page9()      # GET AuctionImageServlet (request 901)
    self.page10()     # GET AuctionImageServlet (request 1001)
    self.page11()     # GET AuctionImageServlet (request 1101)

    grinder.sleep(3436)
    self.page12()     # GET DetailServlet (request 1201)

    grinder.sleep(16)
    self.page13()     # GET AuctionImageServlet (request 1301)

    grinder.sleep(3391)
    self.page14()     # GET / (request 1401)

    grinder.sleep(1720)
    self.page15()     # GET ListServlet (request 1501)

    grinder.sleep(31)
    self.page16()     # GET AuctionImageServlet (request 1601)
    self.page17()     # GET AuctionImageServlet (request 1701)
    self.page18()     # GET AuctionImageServlet (request 1801)
    self.page19()     # GET AuctionImageServlet (request 1901)
    self.page20()     # GET AuctionImageServlet (request 2001)
    self.page21()     # GET AuctionImageServlet (request 2101)
    self.page22()     # GET AuctionImageServlet (request 2201)
    self.page23()     # GET AuctionImageServlet (request 2301)

    grinder.sleep(635)
    self.page24()     # GET DetailServlet (request 2401)

    grinder.sleep(138)
    self.page25()     # GET AuctionImageServlet (request 2501)

    grinder.sleep(2013)
    self.page26()     # GET / (request 2601)

    grinder.sleep(2826)
    self.page27()     # GET ListServlet (request 2701)

    grinder.sleep(13)
    self.page28()     # GET AuctionImageServlet (request 2801)
    self.page29()     # GET AuctionImageServlet (request 2901)
    self.page30()     # GET AuctionImageServlet (request 3001)
    self.page31()     # GET AuctionImageServlet (request 3101)
    self.page32()     # GET AuctionImageServlet (request 3201)
    self.page33()     # GET AuctionImageServlet (request 3301)
    self.page34()     # GET AuctionImageServlet (request 3401)
    self.page35()     # GET AuctionImageServlet (request 3501)

    grinder.sleep(1500)
    self.page36()     # GET DetailServlet (request 3601)

    grinder.sleep(20)
    self.page37()     # GET AuctionImageServlet (request 3701)

    grinder.sleep(2831)
    self.page38()     # GET / (request 3801)

    grinder.sleep(1665)
    self.page39()     # GET ListServlet (request 3901)

    grinder.sleep(16)
    self.page40()     # GET AuctionImageServlet (request 4001)
    self.page41()     # GET AuctionImageServlet (request 4101)
    self.page42()     # GET AuctionImageServlet (request 4201)
    self.page43()     # GET AuctionImageServlet (request 4301)
    self.page44()     # GET AuctionImageServlet (request 4401)
    self.page45()     # GET AuctionImageServlet (request 4501)
    self.page46()     # GET AuctionImageServlet (request 4601)
    self.page47()     # GET AuctionImageServlet (request 4701)

    grinder.sleep(1384)
    self.page48()     # GET DetailServlet (request 4801)

    grinder.sleep(38)
    self.page49()     # GET AuctionImageServlet (request 4901)

    grinder.sleep(6942)
    self.page50()     # GET / (request 5001)


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
Test(1000, 'Page 10').record(TestRunner.page10)
Test(1100, 'Page 11').record(TestRunner.page11)
Test(1200, 'Page 12').record(TestRunner.page12)
Test(1300, 'Page 13').record(TestRunner.page13)
Test(1400, 'Page 14').record(TestRunner.page14)
Test(1500, 'Page 15').record(TestRunner.page15)
Test(1600, 'Page 16').record(TestRunner.page16)
Test(1700, 'Page 17').record(TestRunner.page17)
Test(1800, 'Page 18').record(TestRunner.page18)
Test(1900, 'Page 19').record(TestRunner.page19)
Test(2000, 'Page 20').record(TestRunner.page20)
Test(2100, 'Page 21').record(TestRunner.page21)
Test(2200, 'Page 22').record(TestRunner.page22)
Test(2300, 'Page 23').record(TestRunner.page23)
Test(2400, 'Page 24').record(TestRunner.page24)
Test(2500, 'Page 25').record(TestRunner.page25)
Test(2600, 'Page 26').record(TestRunner.page26)
Test(2700, 'Page 27').record(TestRunner.page27)
Test(2800, 'Page 28').record(TestRunner.page28)
Test(2900, 'Page 29').record(TestRunner.page29)
Test(3000, 'Page 30').record(TestRunner.page30)
Test(3100, 'Page 31').record(TestRunner.page31)
Test(3200, 'Page 32').record(TestRunner.page32)
Test(3300, 'Page 33').record(TestRunner.page33)
Test(3400, 'Page 34').record(TestRunner.page34)
Test(3500, 'Page 35').record(TestRunner.page35)
Test(3600, 'Page 36').record(TestRunner.page36)
Test(3700, 'Page 37').record(TestRunner.page37)
Test(3800, 'Page 38').record(TestRunner.page38)
Test(3900, 'Page 39').record(TestRunner.page39)
Test(4000, 'Page 40').record(TestRunner.page40)
Test(4100, 'Page 41').record(TestRunner.page41)
Test(4200, 'Page 42').record(TestRunner.page42)
Test(4300, 'Page 43').record(TestRunner.page43)
Test(4400, 'Page 44').record(TestRunner.page44)
Test(4500, 'Page 45').record(TestRunner.page45)
Test(4600, 'Page 46').record(TestRunner.page46)
Test(4700, 'Page 47').record(TestRunner.page47)
Test(4800, 'Page 48').record(TestRunner.page48)
Test(4900, 'Page 49').record(TestRunner.page49)
Test(5000, 'Page 50').record(TestRunner.page50)
