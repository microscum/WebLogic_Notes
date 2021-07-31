# The Grinder 3.11
# HTTP script recorded by TCPProxy at Nov 18, 2013 4:06:51 AM

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
    NVPair('Referer', 'http://192.0.2.11:7777/SimpleAuctionWebAppDb/SetupServlet'), ]

headers2= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://192.0.2.11:7777/SimpleAuctionWebAppDb/'), ]

headers3= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://192.0.2.11:7777/SimpleAuctionWebAppDb/ListServlet'), ]

headers4= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://192.0.2.11:7777/SimpleAuctionWebAppDb/ListServlet'), ]

headers5= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://192.0.2.11:7777/SimpleAuctionWebAppDb/DetailServlet?id=88'), ]

headers6= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://192.0.2.11:7777/SimpleAuctionWebAppDb/DetailServlet?id=88'), ]

headers7= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://192.0.2.11:7777/SimpleAuctionWebAppDb/setup.jsp'), ]

url0 = 'http://host01.example.com:7001'
url1 = 'http://192.0.2.11:7777'

request101 = createRequest(Test(101, 'GET console'), url0, headers0)

request102 = createRequest(Test(102, 'GET /'), url0, headers0)

request103 = createRequest(Test(103, 'GET LoginForm.jsp'), url0, headers0)

request201 = createRequest(Test(201, 'GET index.jsp'), url1, headers0)

request301 = createRequest(Test(301, 'GET styles.css'), url1)

request401 = createRequest(Test(401, 'GET setup.jsp'), url1)

request501 = createRequest(Test(501, 'GET SetupServlet'), url1)

request601 = createRequest(Test(601, 'GET /'), url1, headers1)

request701 = createRequest(Test(701, 'GET ListServlet'), url1, headers2)

request801 = createRequest(Test(801, 'GET AuctionImageServlet'), url1, headers3)

request901 = createRequest(Test(901, 'GET AuctionImageServlet'), url1, headers3)

request1001 = createRequest(Test(1001, 'GET AuctionImageServlet'), url1, headers3)

request1101 = createRequest(Test(1101, 'GET AuctionImageServlet'), url1, headers3)

request1201 = createRequest(Test(1201, 'GET AuctionImageServlet'), url1, headers3)

request1301 = createRequest(Test(1301, 'GET AuctionImageServlet'), url1, headers3)

request1401 = createRequest(Test(1401, 'GET AuctionImageServlet'), url1, headers3)

request1501 = createRequest(Test(1501, 'GET AuctionImageServlet'), url1, headers3)

request1601 = createRequest(Test(1601, 'GET DetailServlet'), url1, headers4)

request1701 = createRequest(Test(1701, 'GET AuctionImageServlet'), url1)

request1801 = createRequest(Test(1801, 'GET ListServlet'), url1)

request1901 = createRequest(Test(1901, 'GET AuctionImageServlet'), url1, headers3)

request2001 = createRequest(Test(2001, 'GET AuctionImageServlet'), url1, headers3)

request2101 = createRequest(Test(2101, 'GET AuctionImageServlet'), url1, headers3)

request2201 = createRequest(Test(2201, 'GET AuctionImageServlet'), url1, headers3)

request2301 = createRequest(Test(2301, 'GET AuctionImageServlet'), url1, headers3)

request2401 = createRequest(Test(2401, 'GET AuctionImageServlet'), url1, headers3)

request2501 = createRequest(Test(2501, 'GET AuctionImageServlet'), url1, headers3)

request2601 = createRequest(Test(2601, 'GET AuctionImageServlet'), url1, headers3)

request2701 = createRequest(Test(2701, 'GET DetailServlet'), url1, headers4)

request2801 = createRequest(Test(2801, 'GET AuctionImageServlet'), url1, headers5)

request2901 = createRequest(Test(2901, 'GET ListServlet'), url1, headers6)

request3001 = createRequest(Test(3001, 'GET AuctionImageServlet'), url1, headers3)

request3101 = createRequest(Test(3101, 'GET AuctionImageServlet'), url1, headers3)

request3201 = createRequest(Test(3201, 'GET AuctionImageServlet'), url1, headers3)

request3301 = createRequest(Test(3301, 'GET AuctionImageServlet'), url1, headers3)

request3401 = createRequest(Test(3401, 'GET AuctionImageServlet'), url1, headers3)

request3501 = createRequest(Test(3501, 'GET AuctionImageServlet'), url1, headers3)

request3601 = createRequest(Test(3601, 'GET AuctionImageServlet'), url1, headers3)

request3701 = createRequest(Test(3701, 'GET AuctionImageServlet'), url1, headers3)

request3801 = createRequest(Test(3801, 'GET DetailServlet'), url1, headers4)

request3901 = createRequest(Test(3901, 'GET AuctionImageServlet'), url1)

request4001 = createRequest(Test(4001, 'GET /'), url1)

request4101 = createRequest(Test(4101, 'GET setup.jsp'), url1, headers2)

request4201 = createRequest(Test(4201, 'GET SetupServlet'), url1, headers7)

request4301 = createRequest(Test(4301, 'GET /'), url1, headers1)

request4401 = createRequest(Test(4401, 'GET ListServlet'), url1, headers2)

request4501 = createRequest(Test(4501, 'GET AuctionImageServlet'), url1, headers3)

request4601 = createRequest(Test(4601, 'GET AuctionImageServlet'), url1, headers3)

request4701 = createRequest(Test(4701, 'GET AuctionImageServlet'), url1, headers3)

request4801 = createRequest(Test(4801, 'GET AuctionImageServlet'), url1, headers3)

request4901 = createRequest(Test(4901, 'GET AuctionImageServlet'), url1, headers3)

request5001 = createRequest(Test(5001, 'GET AuctionImageServlet'), url1, headers3)

request5101 = createRequest(Test(5101, 'GET AuctionImageServlet'), url1, headers3)

request5201 = createRequest(Test(5201, 'GET AuctionImageServlet'), url1, headers3)

request5301 = createRequest(Test(5301, 'GET AuctionImageServlet'), url1, headers3)

request5401 = createRequest(Test(5401, 'GET AuctionImageServlet'), url1, headers3)

request5501 = createRequest(Test(5501, 'GET AuctionImageServlet'), url1, headers3)

request5601 = createRequest(Test(5601, 'GET AuctionImageServlet'), url1, headers3)

request5701 = createRequest(Test(5701, 'GET AuctionImageServlet'), url1, headers3)

request5801 = createRequest(Test(5801, 'GET AuctionImageServlet'), url1, headers3)

request5901 = createRequest(Test(5901, 'GET AuctionImageServlet'), url1, headers3)

request6001 = createRequest(Test(6001, 'GET DetailServlet'), url1, headers4)

request6101 = createRequest(Test(6101, 'GET AuctionImageServlet'), url1)

request6201 = createRequest(Test(6201, 'GET ListServlet'), url1)

request6301 = createRequest(Test(6301, 'GET AuctionImageServlet'), url1, headers3)

request6401 = createRequest(Test(6401, 'GET AuctionImageServlet'), url1, headers3)

request6501 = createRequest(Test(6501, 'GET AuctionImageServlet'), url1, headers3)

request6601 = createRequest(Test(6601, 'GET AuctionImageServlet'), url1, headers3)

request6701 = createRequest(Test(6701, 'GET AuctionImageServlet'), url1, headers3)

request6801 = createRequest(Test(6801, 'GET AuctionImageServlet'), url1, headers3)

request6901 = createRequest(Test(6901, 'GET AuctionImageServlet'), url1, headers3)

request7001 = createRequest(Test(7001, 'GET AuctionImageServlet'), url1, headers3)

request7101 = createRequest(Test(7101, 'GET AuctionImageServlet'), url1, headers3)

request7201 = createRequest(Test(7201, 'GET AuctionImageServlet'), url1, headers3)

request7301 = createRequest(Test(7301, 'GET AuctionImageServlet'), url1, headers3)

request7401 = createRequest(Test(7401, 'GET AuctionImageServlet'), url1, headers3)

request7501 = createRequest(Test(7501, 'GET AuctionImageServlet'), url1, headers3)

request7601 = createRequest(Test(7601, 'GET AuctionImageServlet'), url1, headers3)

request7701 = createRequest(Test(7701, 'GET AuctionImageServlet'), url1, headers3)

request7801 = createRequest(Test(7801, 'GET DetailServlet'), url1, headers4)

request7901 = createRequest(Test(7901, 'GET AuctionImageServlet'), url1)

request8001 = createRequest(Test(8001, 'GET ListServlet'), url1)

request8101 = createRequest(Test(8101, 'GET AuctionImageServlet'), url1, headers3)

request8201 = createRequest(Test(8201, 'GET AuctionImageServlet'), url1, headers3)

request8301 = createRequest(Test(8301, 'GET AuctionImageServlet'), url1, headers3)

request8401 = createRequest(Test(8401, 'GET AuctionImageServlet'), url1, headers3)

request8501 = createRequest(Test(8501, 'GET AuctionImageServlet'), url1, headers3)

request8601 = createRequest(Test(8601, 'GET AuctionImageServlet'), url1, headers3)

request8701 = createRequest(Test(8701, 'GET AuctionImageServlet'), url1, headers3)

request8801 = createRequest(Test(8801, 'GET AuctionImageServlet'), url1, headers3)

request8901 = createRequest(Test(8901, 'GET AuctionImageServlet'), url1, headers3)

request9001 = createRequest(Test(9001, 'GET AuctionImageServlet'), url1, headers3)

request9101 = createRequest(Test(9101, 'GET AuctionImageServlet'), url1, headers3)

request9201 = createRequest(Test(9201, 'GET AuctionImageServlet'), url1, headers3)

request9301 = createRequest(Test(9301, 'GET AuctionImageServlet'), url1, headers3)

request9401 = createRequest(Test(9401, 'GET AuctionImageServlet'), url1, headers3)

request9501 = createRequest(Test(9501, 'GET AuctionImageServlet'), url1, headers3)

request9601 = createRequest(Test(9601, 'GET DetailServlet'), url1, headers4)

request9701 = createRequest(Test(9701, 'GET AuctionImageServlet'), url1, headers5)

request9801 = createRequest(Test(9801, 'GET /'), url1, headers6)

request9901 = createRequest(Test(9901, 'GET setup.jsp'), url1, headers2)

request10001 = createRequest(Test(10001, 'GET SetupServlet'), url1, headers7)

request10101 = createRequest(Test(10101, 'GET /'), url1, headers1)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """GET console (requests 101-103)."""
    
    # Expecting 302 'Moved Temporarily'
    result = request101.GET('/console')

    grinder.sleep(91)
    
    # Expecting 302 'Moved Temporarily'
    request102.GET('/console/')

    grinder.sleep(14)
    request103.GET('/console/login/LoginForm.jsp')
    self.token_j_character_encoding = \
      httpUtilities.valueFromHiddenInput('j_character_encoding') # 'UTF-8'

    return result

  def page2(self):
    """GET index.jsp (request 201)."""
    result = request201.GET('/SimpleAuctionWebAppDb/index.jsp')
    self.token_jsessionid = \
      httpUtilities.valueFromBodyURI('jsessionid') # 'kqtpZBLTGeNarPKq995RMusBulyPu86slbMOHkIW...'

    return result

  def page3(self):
    """GET styles.css (request 301)."""
    result = request301.GET('/SimpleAuctionWebAppDb/res/styles.css;jsessionid=' +
      self.token_jsessionid, None,
      ( NVPair('Accept', 'text/css,*/*;q=0.1'),
        NVPair('Referer', 'http://192.0.2.11:7777/SimpleAuctionWebAppDb/index.jsp'), ))

    return result

  def page4(self):
    """GET setup.jsp (request 401)."""
    result = request401.GET('/SimpleAuctionWebAppDb/setup.jsp;jsessionid=' +
      self.token_jsessionid, None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://192.0.2.11:7777/SimpleAuctionWebAppDb/index.jsp'), ))

    return result

  def page5(self):
    """GET SetupServlet (request 501)."""
    result = request501.GET('/SimpleAuctionWebAppDb/SetupServlet', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://192.0.2.11:7777/SimpleAuctionWebAppDb/setup.jsp;jsessionid=kqtpZBLTGeNarPKq995RMusBulyPu86slbMOHkIWGSOgkTXJbj0V!138960029'), ))

    return result

  def page6(self):
    """GET / (request 601)."""
    result = request601.GET('/SimpleAuctionWebAppDb/')

    return result

  def page7(self):
    """GET ListServlet (request 701)."""
    result = request701.GET('/SimpleAuctionWebAppDb/ListServlet')
    # 8 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '85'

    return result

  def page8(self):
    """GET AuctionImageServlet (request 801)."""
    self.token_imageId = \
      '77'
    self.token_mode = \
      'thumb'
    result = request801.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page9(self):
    """GET AuctionImageServlet (request 901)."""
    self.token_imageId = \
      '83'
    result = request901.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page10(self):
    """GET AuctionImageServlet (request 1001)."""
    self.token_imageId = \
      '82'
    result = request1001.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page11(self):
    """GET AuctionImageServlet (request 1101)."""
    self.token_imageId = \
      '0'
    result = request1101.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page12(self):
    """GET AuctionImageServlet (request 1201)."""
    self.token_imageId = \
      '78'
    result = request1201.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page13(self):
    """GET AuctionImageServlet (request 1301)."""
    self.token_imageId = \
      '79'
    result = request1301.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page14(self):
    """GET AuctionImageServlet (request 1401)."""
    self.token_imageId = \
      '80'
    result = request1401.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page15(self):
    """GET AuctionImageServlet (request 1501)."""
    self.token_imageId = \
      '81'
    result = request1501.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page16(self):
    """GET DetailServlet (request 1601)."""
    result = request1601.GET('/SimpleAuctionWebAppDb/DetailServlet' +
      '?id=' +
      self.token_id)

    return result

  def page17(self):
    """GET AuctionImageServlet (request 1701)."""
    self.token_imageId = \
      '77'
    result = request1701.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId, None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://192.0.2.11:7777/SimpleAuctionWebAppDb/DetailServlet?id=85'), ))

    return result

  def page18(self):
    """GET ListServlet (request 1801)."""
    result = request1801.GET('/SimpleAuctionWebAppDb/ListServlet', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://192.0.2.11:7777/SimpleAuctionWebAppDb/DetailServlet?id=85'), ))
    # 7 different values for token_id found in response; the first matched
    # the last known value of token_id - don't update the variable.

    return result

  def page19(self):
    """GET AuctionImageServlet (request 1901)."""
    self.token_imageId = \
      '0'
    result = request1901.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page20(self):
    """GET AuctionImageServlet (request 2001)."""
    self.token_imageId = \
      '78'
    result = request2001.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page21(self):
    """GET AuctionImageServlet (request 2101)."""
    self.token_imageId = \
      '82'
    result = request2101.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page22(self):
    """GET AuctionImageServlet (request 2201)."""
    self.token_imageId = \
      '81'
    result = request2201.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page23(self):
    """GET AuctionImageServlet (request 2301)."""
    self.token_imageId = \
      '77'
    result = request2301.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page24(self):
    """GET AuctionImageServlet (request 2401)."""
    self.token_imageId = \
      '79'
    result = request2401.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page25(self):
    """GET AuctionImageServlet (request 2501)."""
    self.token_imageId = \
      '80'
    result = request2501.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page26(self):
    """GET AuctionImageServlet (request 2601)."""
    self.token_imageId = \
      '83'
    result = request2601.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page27(self):
    """GET DetailServlet (request 2701)."""
    self.token_id = \
      '88'
    result = request2701.GET('/SimpleAuctionWebAppDb/DetailServlet' +
      '?id=' +
      self.token_id)

    return result

  def page28(self):
    """GET AuctionImageServlet (request 2801)."""
    self.token_imageId = \
      '80'
    result = request2801.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId)

    return result

  def page29(self):
    """GET ListServlet (request 2901)."""
    result = request2901.GET('/SimpleAuctionWebAppDb/ListServlet')
    # 8 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '85'

    return result

  def page30(self):
    """GET AuctionImageServlet (request 3001)."""
    self.token_imageId = \
      '0'
    result = request3001.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page31(self):
    """GET AuctionImageServlet (request 3101)."""
    self.token_imageId = \
      '80'
    result = request3101.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page32(self):
    """GET AuctionImageServlet (request 3201)."""
    self.token_imageId = \
      '77'
    result = request3201.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page33(self):
    """GET AuctionImageServlet (request 3301)."""
    self.token_imageId = \
      '81'
    result = request3301.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page34(self):
    """GET AuctionImageServlet (request 3401)."""
    self.token_imageId = \
      '79'
    result = request3401.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page35(self):
    """GET AuctionImageServlet (request 3501)."""
    self.token_imageId = \
      '78'
    result = request3501.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page36(self):
    """GET AuctionImageServlet (request 3601)."""
    self.token_imageId = \
      '83'
    result = request3601.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page37(self):
    """GET AuctionImageServlet (request 3701)."""
    self.token_imageId = \
      '82'
    result = request3701.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page38(self):
    """GET DetailServlet (request 3801)."""
    self.token_id = \
      '90'
    result = request3801.GET('/SimpleAuctionWebAppDb/DetailServlet' +
      '?id=' +
      self.token_id)

    return result

  def page39(self):
    """GET AuctionImageServlet (request 3901)."""
    result = request3901.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId, None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://192.0.2.11:7777/SimpleAuctionWebAppDb/DetailServlet?id=90'), ))

    return result

  def page40(self):
    """GET / (request 4001)."""
    result = request4001.GET('/SimpleAuctionWebAppDb/', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://192.0.2.11:7777/SimpleAuctionWebAppDb/DetailServlet?id=90'), ))

    return result

  def page41(self):
    """GET setup.jsp (request 4101)."""
    result = request4101.GET('/SimpleAuctionWebAppDb/setup.jsp')

    return result

  def page42(self):
    """GET SetupServlet (request 4201)."""
    result = request4201.GET('/SimpleAuctionWebAppDb/SetupServlet')

    return result

  def page43(self):
    """GET / (request 4301)."""
    result = request4301.GET('/SimpleAuctionWebAppDb/')

    return result

  def page44(self):
    """GET ListServlet (request 4401)."""
    result = request4401.GET('/SimpleAuctionWebAppDb/ListServlet')
    # 16 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '85'

    return result

  def page45(self):
    """GET AuctionImageServlet (request 4501)."""
    self.token_imageId = \
      '0'
    result = request4501.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page46(self):
    """GET AuctionImageServlet (request 4601)."""
    self.token_imageId = \
      '86'
    result = request4601.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page47(self):
    """GET AuctionImageServlet (request 4701)."""
    self.token_imageId = \
      '85'
    result = request4701.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page48(self):
    """GET AuctionImageServlet (request 4801)."""
    self.token_imageId = \
      '77'
    result = request4801.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page49(self):
    """GET AuctionImageServlet (request 4901)."""
    self.token_imageId = \
      '89'
    result = request4901.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page50(self):
    """GET AuctionImageServlet (request 5001)."""
    self.token_imageId = \
      '88'
    result = request5001.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page51(self):
    """GET AuctionImageServlet (request 5101)."""
    self.token_imageId = \
      '87'
    result = request5101.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page52(self):
    """GET AuctionImageServlet (request 5201)."""
    self.token_imageId = \
      '84'
    result = request5201.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page53(self):
    """GET AuctionImageServlet (request 5301)."""
    self.token_imageId = \
      '90'
    result = request5301.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page54(self):
    """GET AuctionImageServlet (request 5401)."""
    self.token_imageId = \
      '78'
    result = request5401.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page55(self):
    """GET AuctionImageServlet (request 5501)."""
    self.token_imageId = \
      '79'
    result = request5501.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page56(self):
    """GET AuctionImageServlet (request 5601)."""
    self.token_imageId = \
      '80'
    result = request5601.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page57(self):
    """GET AuctionImageServlet (request 5701)."""
    self.token_imageId = \
      '81'
    result = request5701.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page58(self):
    """GET AuctionImageServlet (request 5801)."""
    self.token_imageId = \
      '82'
    result = request5801.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page59(self):
    """GET AuctionImageServlet (request 5901)."""
    self.token_imageId = \
      '83'
    result = request5901.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page60(self):
    """GET DetailServlet (request 6001)."""
    self.token_id = \
      '86'
    result = request6001.GET('/SimpleAuctionWebAppDb/DetailServlet' +
      '?id=' +
      self.token_id)

    return result

  def page61(self):
    """GET AuctionImageServlet (request 6101)."""
    self.token_imageId = \
      '78'
    result = request6101.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId, None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://192.0.2.11:7777/SimpleAuctionWebAppDb/DetailServlet?id=86'), ))

    return result

  def page62(self):
    """GET ListServlet (request 6201)."""
    result = request6201.GET('/SimpleAuctionWebAppDb/ListServlet', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://192.0.2.11:7777/SimpleAuctionWebAppDb/DetailServlet?id=86'), ))
    # 16 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '85'

    return result

  def page63(self):
    """GET AuctionImageServlet (request 6301)."""
    self.token_imageId = \
      '0'
    result = request6301.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page64(self):
    """GET AuctionImageServlet (request 6401)."""
    self.token_imageId = \
      '80'
    result = request6401.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page65(self):
    """GET AuctionImageServlet (request 6501)."""
    self.token_imageId = \
      '84'
    result = request6501.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page66(self):
    """GET AuctionImageServlet (request 6601)."""
    self.token_imageId = \
      '82'
    result = request6601.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page67(self):
    """GET AuctionImageServlet (request 6701)."""
    self.token_imageId = \
      '77'
    result = request6701.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page68(self):
    """GET AuctionImageServlet (request 6801)."""
    self.token_imageId = \
      '81'
    result = request6801.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page69(self):
    """GET AuctionImageServlet (request 6901)."""
    self.token_imageId = \
      '78'
    result = request6901.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page70(self):
    """GET AuctionImageServlet (request 7001)."""
    self.token_imageId = \
      '79'
    result = request7001.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page71(self):
    """GET AuctionImageServlet (request 7101)."""
    self.token_imageId = \
      '83'
    result = request7101.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page72(self):
    """GET AuctionImageServlet (request 7201)."""
    self.token_imageId = \
      '85'
    result = request7201.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page73(self):
    """GET AuctionImageServlet (request 7301)."""
    self.token_imageId = \
      '86'
    result = request7301.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page74(self):
    """GET AuctionImageServlet (request 7401)."""
    self.token_imageId = \
      '87'
    result = request7401.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page75(self):
    """GET AuctionImageServlet (request 7501)."""
    self.token_imageId = \
      '88'
    result = request7501.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page76(self):
    """GET AuctionImageServlet (request 7601)."""
    self.token_imageId = \
      '89'
    result = request7601.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page77(self):
    """GET AuctionImageServlet (request 7701)."""
    self.token_imageId = \
      '90'
    result = request7701.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page78(self):
    """GET DetailServlet (request 7801)."""
    self.token_id = \
      '91'
    result = request7801.GET('/SimpleAuctionWebAppDb/DetailServlet' +
      '?id=' +
      self.token_id)

    return result

  def page79(self):
    """GET AuctionImageServlet (request 7901)."""
    self.token_imageId = \
      '83'
    result = request7901.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId, None,
      ( NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
        NVPair('Referer', 'http://192.0.2.11:7777/SimpleAuctionWebAppDb/DetailServlet?id=91'), ))

    return result

  def page80(self):
    """GET ListServlet (request 8001)."""
    result = request8001.GET('/SimpleAuctionWebAppDb/ListServlet', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://192.0.2.11:7777/SimpleAuctionWebAppDb/DetailServlet?id=91'), ))
    # 16 different values for token_id found in response, using the first one.
    self.token_id = \
      httpUtilities.valueFromBodyURI('id') # '85'

    return result

  def page81(self):
    """GET AuctionImageServlet (request 8101)."""
    self.token_imageId = \
      '0'
    result = request8101.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page82(self):
    """GET AuctionImageServlet (request 8201)."""
    self.token_imageId = \
      '84'
    result = request8201.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page83(self):
    """GET AuctionImageServlet (request 8301)."""
    self.token_imageId = \
      '81'
    result = request8301.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page84(self):
    """GET AuctionImageServlet (request 8401)."""
    self.token_imageId = \
      '77'
    result = request8401.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page85(self):
    """GET AuctionImageServlet (request 8501)."""
    self.token_imageId = \
      '78'
    result = request8501.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page86(self):
    """GET AuctionImageServlet (request 8601)."""
    self.token_imageId = \
      '79'
    result = request8601.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page87(self):
    """GET AuctionImageServlet (request 8701)."""
    self.token_imageId = \
      '80'
    result = request8701.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page88(self):
    """GET AuctionImageServlet (request 8801)."""
    self.token_imageId = \
      '83'
    result = request8801.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page89(self):
    """GET AuctionImageServlet (request 8901)."""
    self.token_imageId = \
      '82'
    result = request8901.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page90(self):
    """GET AuctionImageServlet (request 9001)."""
    self.token_imageId = \
      '85'
    result = request9001.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page91(self):
    """GET AuctionImageServlet (request 9101)."""
    self.token_imageId = \
      '86'
    result = request9101.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page92(self):
    """GET AuctionImageServlet (request 9201)."""
    self.token_imageId = \
      '87'
    result = request9201.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page93(self):
    """GET AuctionImageServlet (request 9301)."""
    self.token_imageId = \
      '88'
    result = request9301.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page94(self):
    """GET AuctionImageServlet (request 9401)."""
    self.token_imageId = \
      '89'
    result = request9401.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page95(self):
    """GET AuctionImageServlet (request 9501)."""
    self.token_imageId = \
      '90'
    result = request9501.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId +
      '&mode=' +
      self.token_mode)

    return result

  def page96(self):
    """GET DetailServlet (request 9601)."""
    self.token_id = \
      '88'
    result = request9601.GET('/SimpleAuctionWebAppDb/DetailServlet' +
      '?id=' +
      self.token_id)

    return result

  def page97(self):
    """GET AuctionImageServlet (request 9701)."""
    self.token_imageId = \
      '80'
    result = request9701.GET('/SimpleAuctionWebAppDb/AuctionImageServlet' +
      '?imageId=' +
      self.token_imageId)

    return result

  def page98(self):
    """GET / (request 9801)."""
    result = request9801.GET('/SimpleAuctionWebAppDb/')

    return result

  def page99(self):
    """GET setup.jsp (request 9901)."""
    result = request9901.GET('/SimpleAuctionWebAppDb/setup.jsp')

    return result

  def page100(self):
    """GET SetupServlet (request 10001)."""
    result = request10001.GET('/SimpleAuctionWebAppDb/SetupServlet')

    return result

  def page101(self):
    """GET / (request 10101)."""
    result = request10101.GET('/SimpleAuctionWebAppDb/')

    return result

  def __call__(self):
    """Called for every run performed by the worker thread."""
    self.page1()      # GET console (requests 101-103)

    grinder.sleep(13072)
    self.page2()      # GET index.jsp (request 201)

    grinder.sleep(114)
    self.page3()      # GET styles.css (request 301)

    grinder.sleep(5000)
    self.page4()      # GET setup.jsp (request 401)

    grinder.sleep(3468)
    self.page5()      # GET SetupServlet (request 501)

    grinder.sleep(2137)
    self.page6()      # GET / (request 601)

    grinder.sleep(2657)
    self.page7()      # GET ListServlet (request 701)

    grinder.sleep(66)
    self.page8()      # GET AuctionImageServlet (request 801)
    self.page9()      # GET AuctionImageServlet (request 901)
    self.page10()     # GET AuctionImageServlet (request 1001)
    self.page11()     # GET AuctionImageServlet (request 1101)
    self.page12()     # GET AuctionImageServlet (request 1201)
    self.page13()     # GET AuctionImageServlet (request 1301)
    self.page14()     # GET AuctionImageServlet (request 1401)
    self.page15()     # GET AuctionImageServlet (request 1501)

    grinder.sleep(3388)
    self.page16()     # GET DetailServlet (request 1601)

    grinder.sleep(14)
    self.page17()     # GET AuctionImageServlet (request 1701)

    grinder.sleep(6656)
    self.page18()     # GET ListServlet (request 1801)

    grinder.sleep(17)
    self.page19()     # GET AuctionImageServlet (request 1901)

    grinder.sleep(25)
    self.page20()     # GET AuctionImageServlet (request 2001)
    self.page21()     # GET AuctionImageServlet (request 2101)
    self.page22()     # GET AuctionImageServlet (request 2201)
    self.page23()     # GET AuctionImageServlet (request 2301)
    self.page24()     # GET AuctionImageServlet (request 2401)
    self.page25()     # GET AuctionImageServlet (request 2501)
    self.page26()     # GET AuctionImageServlet (request 2601)

    grinder.sleep(2224)
    self.page27()     # GET DetailServlet (request 2701)

    grinder.sleep(13)
    self.page28()     # GET AuctionImageServlet (request 2801)

    grinder.sleep(3775)
    self.page29()     # GET ListServlet (request 2901)

    grinder.sleep(20)
    self.page30()     # GET AuctionImageServlet (request 3001)
    self.page31()     # GET AuctionImageServlet (request 3101)
    self.page32()     # GET AuctionImageServlet (request 3201)
    self.page33()     # GET AuctionImageServlet (request 3301)
    self.page34()     # GET AuctionImageServlet (request 3401)
    self.page35()     # GET AuctionImageServlet (request 3501)
    self.page36()     # GET AuctionImageServlet (request 3601)
    self.page37()     # GET AuctionImageServlet (request 3701)

    grinder.sleep(3202)
    self.page38()     # GET DetailServlet (request 3801)

    grinder.sleep(13)
    self.page39()     # GET AuctionImageServlet (request 3901)

    grinder.sleep(4684)
    self.page40()     # GET / (request 4001)

    grinder.sleep(3902)
    self.page41()     # GET setup.jsp (request 4101)

    grinder.sleep(2229)
    self.page42()     # GET SetupServlet (request 4201)

    grinder.sleep(2028)
    self.page43()     # GET / (request 4301)

    grinder.sleep(2204)
    self.page44()     # GET ListServlet (request 4401)

    grinder.sleep(39)
    self.page45()     # GET AuctionImageServlet (request 4501)
    self.page46()     # GET AuctionImageServlet (request 4601)
    self.page47()     # GET AuctionImageServlet (request 4701)
    self.page48()     # GET AuctionImageServlet (request 4801)
    self.page49()     # GET AuctionImageServlet (request 4901)
    self.page50()     # GET AuctionImageServlet (request 5001)
    self.page51()     # GET AuctionImageServlet (request 5101)
    self.page52()     # GET AuctionImageServlet (request 5201)
    self.page53()     # GET AuctionImageServlet (request 5301)
    self.page54()     # GET AuctionImageServlet (request 5401)
    self.page55()     # GET AuctionImageServlet (request 5501)
    self.page56()     # GET AuctionImageServlet (request 5601)
    self.page57()     # GET AuctionImageServlet (request 5701)
    self.page58()     # GET AuctionImageServlet (request 5801)
    self.page59()     # GET AuctionImageServlet (request 5901)

    grinder.sleep(1656)
    self.page60()     # GET DetailServlet (request 6001)
    self.page61()     # GET AuctionImageServlet (request 6101)

    grinder.sleep(3948)
    self.page62()     # GET ListServlet (request 6201)

    grinder.sleep(22)
    self.page63()     # GET AuctionImageServlet (request 6301)
    self.page64()     # GET AuctionImageServlet (request 6401)
    self.page65()     # GET AuctionImageServlet (request 6501)
    self.page66()     # GET AuctionImageServlet (request 6601)
    self.page67()     # GET AuctionImageServlet (request 6701)
    self.page68()     # GET AuctionImageServlet (request 6801)
    self.page69()     # GET AuctionImageServlet (request 6901)
    self.page70()     # GET AuctionImageServlet (request 7001)
    self.page71()     # GET AuctionImageServlet (request 7101)
    self.page72()     # GET AuctionImageServlet (request 7201)
    self.page73()     # GET AuctionImageServlet (request 7301)
    self.page74()     # GET AuctionImageServlet (request 7401)
    self.page75()     # GET AuctionImageServlet (request 7501)
    self.page76()     # GET AuctionImageServlet (request 7601)
    self.page77()     # GET AuctionImageServlet (request 7701)

    grinder.sleep(9331)
    self.page78()     # GET DetailServlet (request 7801)

    grinder.sleep(17)
    self.page79()     # GET AuctionImageServlet (request 7901)

    grinder.sleep(2882)
    self.page80()     # GET ListServlet (request 8001)

    grinder.sleep(20)
    self.page81()     # GET AuctionImageServlet (request 8101)
    self.page82()     # GET AuctionImageServlet (request 8201)
    self.page83()     # GET AuctionImageServlet (request 8301)
    self.page84()     # GET AuctionImageServlet (request 8401)
    self.page85()     # GET AuctionImageServlet (request 8501)
    self.page86()     # GET AuctionImageServlet (request 8601)
    self.page87()     # GET AuctionImageServlet (request 8701)
    self.page88()     # GET AuctionImageServlet (request 8801)
    self.page89()     # GET AuctionImageServlet (request 8901)
    self.page90()     # GET AuctionImageServlet (request 9001)
    self.page91()     # GET AuctionImageServlet (request 9101)
    self.page92()     # GET AuctionImageServlet (request 9201)
    self.page93()     # GET AuctionImageServlet (request 9301)
    self.page94()     # GET AuctionImageServlet (request 9401)
    self.page95()     # GET AuctionImageServlet (request 9501)

    grinder.sleep(7544)
    self.page96()     # GET DetailServlet (request 9601)

    grinder.sleep(11)
    self.page97()     # GET AuctionImageServlet (request 9701)

    grinder.sleep(2930)
    self.page98()     # GET / (request 9801)

    grinder.sleep(4766)
    self.page99()     # GET setup.jsp (request 9901)

    grinder.sleep(2092)
    self.page100()    # GET SetupServlet (request 10001)

    grinder.sleep(1984)
    self.page101()    # GET / (request 10101)


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
Test(5100, 'Page 51').record(TestRunner.page51)
Test(5200, 'Page 52').record(TestRunner.page52)
Test(5300, 'Page 53').record(TestRunner.page53)
Test(5400, 'Page 54').record(TestRunner.page54)
Test(5500, 'Page 55').record(TestRunner.page55)
Test(5600, 'Page 56').record(TestRunner.page56)
Test(5700, 'Page 57').record(TestRunner.page57)
Test(5800, 'Page 58').record(TestRunner.page58)
Test(5900, 'Page 59').record(TestRunner.page59)
Test(6000, 'Page 60').record(TestRunner.page60)
Test(6100, 'Page 61').record(TestRunner.page61)
Test(6200, 'Page 62').record(TestRunner.page62)
Test(6300, 'Page 63').record(TestRunner.page63)
Test(6400, 'Page 64').record(TestRunner.page64)
Test(6500, 'Page 65').record(TestRunner.page65)
Test(6600, 'Page 66').record(TestRunner.page66)
Test(6700, 'Page 67').record(TestRunner.page67)
Test(6800, 'Page 68').record(TestRunner.page68)
Test(6900, 'Page 69').record(TestRunner.page69)
Test(7000, 'Page 70').record(TestRunner.page70)
Test(7100, 'Page 71').record(TestRunner.page71)
Test(7200, 'Page 72').record(TestRunner.page72)
Test(7300, 'Page 73').record(TestRunner.page73)
Test(7400, 'Page 74').record(TestRunner.page74)
Test(7500, 'Page 75').record(TestRunner.page75)
Test(7600, 'Page 76').record(TestRunner.page76)
Test(7700, 'Page 77').record(TestRunner.page77)
Test(7800, 'Page 78').record(TestRunner.page78)
Test(7900, 'Page 79').record(TestRunner.page79)
Test(8000, 'Page 80').record(TestRunner.page80)
Test(8100, 'Page 81').record(TestRunner.page81)
Test(8200, 'Page 82').record(TestRunner.page82)
Test(8300, 'Page 83').record(TestRunner.page83)
Test(8400, 'Page 84').record(TestRunner.page84)
Test(8500, 'Page 85').record(TestRunner.page85)
Test(8600, 'Page 86').record(TestRunner.page86)
Test(8700, 'Page 87').record(TestRunner.page87)
Test(8800, 'Page 88').record(TestRunner.page88)
Test(8900, 'Page 89').record(TestRunner.page89)
Test(9000, 'Page 90').record(TestRunner.page90)
Test(9100, 'Page 91').record(TestRunner.page91)
Test(9200, 'Page 92').record(TestRunner.page92)
Test(9300, 'Page 93').record(TestRunner.page93)
Test(9400, 'Page 94').record(TestRunner.page94)
Test(9500, 'Page 95').record(TestRunner.page95)
Test(9600, 'Page 96').record(TestRunner.page96)
Test(9700, 'Page 97').record(TestRunner.page97)
Test(9800, 'Page 98').record(TestRunner.page98)
Test(9900, 'Page 99').record(TestRunner.page99)
Test(10000, 'Page 100').record(TestRunner.page100)
Test(10100, 'Page 101').record(TestRunner.page101)
