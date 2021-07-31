# The Grinder 3.11
# HTTP script recorded by TCPProxy at Sep 26, 2013 2:51:08 PM

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
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://host01:7777/ShoppingCart/'), ]

headers2= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://host01:7777/ShoppingCart/viewshoppingcart'), ]

headers3= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://host01:7777/ShoppingCart/shopping.jsp'), ]

headers4= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://host01:7777/ShoppingCart/shopping.jsp'), ]

headers5= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://host01:7777/ShoppingCart/welcome.jsp'), ]

headers6= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://host01:7777/ShoppingCart/browsestore.jsp'), ]

headers7= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://host01:7777/ShoppingCart/browsecategories'), ]

headers8= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://host01:7777/ShoppingCart/addtocart?item=3%20mechanical%20pencils&price=8.99'), ]

url0 = 'http://host01:7777'

request101 = createRequest(Test(101, 'GET ShoppingCart'), url0, headers0)

request102 = createRequest(Test(102, 'GET /'), url0, headers0)

request103 = createRequest(Test(103, 'GET DWResortHeader1a.jpg'), url0, headers1)

request104 = createRequest(Test(104, 'GET DWResortFooter1a.jpg'), url0, headers1)

request201 = createRequest(Test(201, 'GET viewshoppingcart'), url0)

request301 = createRequest(Test(301, 'GET shopping.jsp'), url0, headers2)

request302 = createRequest(Test(302, 'GET DWResortHeader1a.jpg'), url0, headers3)

request303 = createRequest(Test(303, 'GET DWResortFooter1a.jpg'), url0, headers3)

request401 = createRequest(Test(401, 'GET addtocart'), url0, headers4)

request501 = createRequest(Test(501, 'GET welcome.jsp'), url0)

request601 = createRequest(Test(601, 'GET shopping.jsp'), url0, headers5)

request701 = createRequest(Test(701, 'GET addtocart'), url0, headers4)

request801 = createRequest(Test(801, 'GET welcome.jsp'), url0)

request901 = createRequest(Test(901, 'GET shopping.jsp'), url0, headers5)

request1001 = createRequest(Test(1001, 'GET addtocart'), url0, headers4)

request1101 = createRequest(Test(1101, 'GET welcome.jsp'), url0)

request1201 = createRequest(Test(1201, 'GET viewshoppingcart'), url0, headers5)

request1301 = createRequest(Test(1301, 'GET shopping.jsp'), url0, headers2)

request1401 = createRequest(Test(1401, 'GET addtocart'), url0, headers4)

request1501 = createRequest(Test(1501, 'GET welcome.jsp'), url0)

request1601 = createRequest(Test(1601, 'GET browsestore.jsp'), url0, headers5)

request1701 = createRequest(Test(1701, 'POST browsecategories'), url0, headers6)

request1801 = createRequest(Test(1801, 'GET welcome.jsp'), url0, headers7)

request1901 = createRequest(Test(1901, 'GET shopping.jsp'), url0, headers5)

request2001 = createRequest(Test(2001, 'GET addtocart'), url0, headers4)

request2101 = createRequest(Test(2101, 'GET welcome.jsp'), url0)

request2201 = createRequest(Test(2201, 'GET shopping.jsp'), url0, headers5)

request2301 = createRequest(Test(2301, 'GET addtocart'), url0, headers4)

request2401 = createRequest(Test(2401, 'GET welcome.jsp'), url0, headers8)

request2501 = createRequest(Test(2501, 'GET shopping.jsp'), url0, headers5)

request2601 = createRequest(Test(2601, 'GET addtocart'), url0, headers4)

request2701 = createRequest(Test(2701, 'GET welcome.jsp'), url0, headers8)

request2801 = createRequest(Test(2801, 'GET browsestore.jsp'), url0, headers5)

request2901 = createRequest(Test(2901, 'POST browsecategories'), url0, headers6)

request3001 = createRequest(Test(3001, 'GET welcome.jsp'), url0, headers7)

request3101 = createRequest(Test(3101, 'GET viewshoppingcart'), url0, headers5)

request3201 = createRequest(Test(3201, 'GET shopping.jsp'), url0, headers2)

request3301 = createRequest(Test(3301, 'GET addtocart'), url0, headers4)

request3401 = createRequest(Test(3401, 'GET welcome.jsp'), url0)

request3501 = createRequest(Test(3501, 'GET shopping.jsp'), url0, headers5)

request3601 = createRequest(Test(3601, 'GET addtocart'), url0, headers4)

request3701 = createRequest(Test(3701, 'GET welcome.jsp'), url0)

request3801 = createRequest(Test(3801, 'GET shopping.jsp'), url0, headers5)

request3901 = createRequest(Test(3901, 'GET addtocart'), url0, headers4)

request4001 = createRequest(Test(4001, 'GET welcome.jsp'), url0)

request4101 = createRequest(Test(4101, 'GET shopping.jsp'), url0, headers5)

request4201 = createRequest(Test(4201, 'GET addtocart'), url0, headers4)

request4301 = createRequest(Test(4301, 'GET welcome.jsp'), url0)

request4401 = createRequest(Test(4401, 'GET viewshoppingcart'), url0, headers5)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """GET ShoppingCart (requests 101-104)."""
    
    # Expecting 302 'Moved Temporarily'
    result = request101.GET('/ShoppingCart')

    grinder.sleep(20)
    request102.GET('/ShoppingCart/')

    grinder.sleep(23)
    request103.GET('/ShoppingCart/pages/images/DWResortHeader1a.jpg')

    grinder.sleep(87)
    request104.GET('/ShoppingCart/pages/images/DWResortFooter1a.jpg')

    return result

  def page2(self):
    """GET viewshoppingcart (request 201)."""
    result = request201.GET('/ShoppingCart/viewshoppingcart', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://host01:7777/ShoppingCart/'), ))

    return result

  def page3(self):
    """GET shopping.jsp (requests 301-303)."""
    result = request301.GET('/ShoppingCart/shopping.jsp')

    grinder.sleep(21)
    request302.GET('/ShoppingCart/pages/images/DWResortHeader1a.jpg', None,
      ( NVPair('If-Modified-Since', 'Thu, 26 Sep 2013 14:43:58 GMT'), ))

    request303.GET('/ShoppingCart/pages/images/DWResortFooter1a.jpg', None,
      ( NVPair('If-Modified-Since', 'Thu, 26 Sep 2013 14:43:58 GMT'), ))

    return result

  def page4(self):
    """GET addtocart (request 401)."""
    self.token_item = \
      'box of 12 pens (blue)'
    self.token_price = \
      '4.99'
    result = request401.GET('/ShoppingCart/addtocart' +
      '?item=' +
      self.token_item +
      '&price=' +
      self.token_price)

    return result

  def page5(self):
    """GET welcome.jsp (request 501)."""
    result = request501.GET('/ShoppingCart/welcome.jsp', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://host01:7777/ShoppingCart/addtocart?item=box%20of%2012%20pens%20(blue)&price=4.99'), ))

    return result

  def page6(self):
    """GET shopping.jsp (request 601)."""
    result = request601.GET('/ShoppingCart/shopping.jsp')

    return result

  def page7(self):
    """GET addtocart (request 701)."""
    self.token_item = \
      'package of 5 legal pads'
    self.token_price = \
      '15.99'
    result = request701.GET('/ShoppingCart/addtocart' +
      '?item=' +
      self.token_item +
      '&price=' +
      self.token_price)

    return result

  def page8(self):
    """GET welcome.jsp (request 801)."""
    result = request801.GET('/ShoppingCart/welcome.jsp', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://host01:7777/ShoppingCart/addtocart?item=package%20of%205%20legal%20pads&price=15.99'), ))

    return result

  def page9(self):
    """GET shopping.jsp (request 901)."""
    result = request901.GET('/ShoppingCart/shopping.jsp')

    return result

  def page10(self):
    """GET addtocart (request 1001)."""
    self.token_item = \
      'box of 12 pens (black)'
    self.token_price = \
      '4.99'
    result = request1001.GET('/ShoppingCart/addtocart' +
      '?item=' +
      self.token_item +
      '&price=' +
      self.token_price)

    return result

  def page11(self):
    """GET welcome.jsp (request 1101)."""
    result = request1101.GET('/ShoppingCart/welcome.jsp', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://host01:7777/ShoppingCart/addtocart?item=box%20of%2012%20pens%20(black)&price=4.99'), ))

    return result

  def page12(self):
    """GET viewshoppingcart (request 1201)."""
    result = request1201.GET('/ShoppingCart/viewshoppingcart')

    return result

  def page13(self):
    """GET shopping.jsp (request 1301)."""
    result = request1301.GET('/ShoppingCart/shopping.jsp')

    return result

  def page14(self):
    """GET addtocart (request 1401)."""
    self.token_item = \
      '100 Post-It notes'
    self.token_price = \
      '7.99'
    result = request1401.GET('/ShoppingCart/addtocart' +
      '?item=' +
      self.token_item +
      '&price=' +
      self.token_price)

    return result

  def page15(self):
    """GET welcome.jsp (request 1501)."""
    result = request1501.GET('/ShoppingCart/welcome.jsp', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://host01:7777/ShoppingCart/addtocart?item=100%20Post-It%20notes&price=7.99'), ))

    return result

  def page16(self):
    """GET browsestore.jsp (request 1601)."""
    result = request1601.GET('/ShoppingCart/browsestore.jsp')

    return result

  def page17(self):
    """POST browsecategories (request 1701)."""
    result = request1701.POST('/ShoppingCart/browsecategories',
      ( NVPair('boxFurniture', 'furniture'),
        NVPair('btnSubmit', 'Retrieve Items'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))

    return result

  def page18(self):
    """GET welcome.jsp (request 1801)."""
    result = request1801.GET('/ShoppingCart/welcome.jsp')

    return result

  def page19(self):
    """GET shopping.jsp (request 1901)."""
    result = request1901.GET('/ShoppingCart/shopping.jsp')

    return result

  def page20(self):
    """GET addtocart (request 2001)."""
    self.token_item = \
      'corner computer desk'
    self.token_price = \
      '199.99'
    result = request2001.GET('/ShoppingCart/addtocart' +
      '?item=' +
      self.token_item +
      '&price=' +
      self.token_price)

    return result

  def page21(self):
    """GET welcome.jsp (request 2101)."""
    result = request2101.GET('/ShoppingCart/welcome.jsp', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://host01:7777/ShoppingCart/addtocart?item=corner%20computer%20desk&price=199.99'), ))

    return result

  def page22(self):
    """GET shopping.jsp (request 2201)."""
    result = request2201.GET('/ShoppingCart/shopping.jsp')

    return result

  def page23(self):
    """GET addtocart (request 2301)."""
    self.token_item = \
      '3 mechanical pencils'
    self.token_price = \
      '8.99'
    result = request2301.GET('/ShoppingCart/addtocart' +
      '?item=' +
      self.token_item +
      '&price=' +
      self.token_price)

    return result

  def page24(self):
    """GET welcome.jsp (request 2401)."""
    result = request2401.GET('/ShoppingCart/welcome.jsp')

    return result

  def page25(self):
    """GET shopping.jsp (request 2501)."""
    result = request2501.GET('/ShoppingCart/shopping.jsp')

    return result

  def page26(self):
    """GET addtocart (request 2601)."""
    result = request2601.GET('/ShoppingCart/addtocart' +
      '?item=' +
      self.token_item +
      '&price=' +
      self.token_price)

    return result

  def page27(self):
    """GET welcome.jsp (request 2701)."""
    result = request2701.GET('/ShoppingCart/welcome.jsp')

    return result

  def page28(self):
    """GET browsestore.jsp (request 2801)."""
    result = request2801.GET('/ShoppingCart/browsestore.jsp')

    return result

  def page29(self):
    """POST browsecategories (request 2901)."""
    result = request2901.POST('/ShoppingCart/browsecategories',
      ( NVPair('boxPaper', 'paper'),
        NVPair('btnSubmit', 'Retrieve Items'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))

    return result

  def page30(self):
    """GET welcome.jsp (request 3001)."""
    result = request3001.GET('/ShoppingCart/welcome.jsp')

    return result

  def page31(self):
    """GET viewshoppingcart (request 3101)."""
    result = request3101.GET('/ShoppingCart/viewshoppingcart')

    return result

  def page32(self):
    """GET shopping.jsp (request 3201)."""
    result = request3201.GET('/ShoppingCart/shopping.jsp')

    return result

  def page33(self):
    """GET addtocart (request 3301)."""
    self.token_item = \
      'adjustable chair'
    self.token_price = \
      '99.99'
    result = request3301.GET('/ShoppingCart/addtocart' +
      '?item=' +
      self.token_item +
      '&price=' +
      self.token_price)

    return result

  def page34(self):
    """GET welcome.jsp (request 3401)."""
    result = request3401.GET('/ShoppingCart/welcome.jsp', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://host01:7777/ShoppingCart/addtocart?item=adjustable%20chair&price=99.99'), ))

    return result

  def page35(self):
    """GET shopping.jsp (request 3501)."""
    result = request3501.GET('/ShoppingCart/shopping.jsp')

    return result

  def page36(self):
    """GET addtocart (request 3601)."""
    self.token_item = \
      'leather adjustable chair'
    self.token_price = \
      '139.99'
    result = request3601.GET('/ShoppingCart/addtocart' +
      '?item=' +
      self.token_item +
      '&price=' +
      self.token_price)

    return result

  def page37(self):
    """GET welcome.jsp (request 3701)."""
    result = request3701.GET('/ShoppingCart/welcome.jsp', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://host01:7777/ShoppingCart/addtocart?item=leather%20adjustable%20chair&price=139.99'), ))

    return result

  def page38(self):
    """GET shopping.jsp (request 3801)."""
    result = request3801.GET('/ShoppingCart/shopping.jsp')

    return result

  def page39(self):
    """GET addtocart (request 3901)."""
    self.token_item = \
      'box of 12 pens (red)'
    self.token_price = \
      '4.99'
    result = request3901.GET('/ShoppingCart/addtocart' +
      '?item=' +
      self.token_item +
      '&price=' +
      self.token_price)

    return result

  def page40(self):
    """GET welcome.jsp (request 4001)."""
    result = request4001.GET('/ShoppingCart/welcome.jsp', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://host01:7777/ShoppingCart/addtocart?item=box%20of%2012%20pens%20(red)&price=4.99'), ))

    return result

  def page41(self):
    """GET shopping.jsp (request 4101)."""
    result = request4101.GET('/ShoppingCart/shopping.jsp')

    return result

  def page42(self):
    """GET addtocart (request 4201)."""
    self.token_item = \
      'package of 500 sheets of multipurpose paper'
    self.token_price = \
      '6.99'
    result = request4201.GET('/ShoppingCart/addtocart' +
      '?item=' +
      self.token_item +
      '&price=' +
      self.token_price)

    return result

  def page43(self):
    """GET welcome.jsp (request 4301)."""
    result = request4301.GET('/ShoppingCart/welcome.jsp', None,
      ( NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        NVPair('Referer', 'http://host01:7777/ShoppingCart/addtocart?item=package%20of%20500%20sheets%20of%20multipurpose%20paper&price=6.99'), ))

    return result

  def page44(self):
    """GET viewshoppingcart (request 4401)."""
    result = request4401.GET('/ShoppingCart/viewshoppingcart')

    return result

  def __call__(self):
    """Called for every run performed by the worker thread."""
    self.page1()      # GET ShoppingCart (requests 101-104)

    grinder.sleep(3047)
    self.page2()      # GET viewshoppingcart (request 201)

    grinder.sleep(4754)
    self.page3()      # GET shopping.jsp (requests 301-303)

    grinder.sleep(2051)
    self.page4()      # GET addtocart (request 401)

    grinder.sleep(1418)
    self.page5()      # GET welcome.jsp (request 501)

    grinder.sleep(2454)
    self.page6()      # GET shopping.jsp (request 601)

    grinder.sleep(1455)
    self.page7()      # GET addtocart (request 701)

    grinder.sleep(1546)
    self.page8()      # GET welcome.jsp (request 801)

    grinder.sleep(1650)
    self.page9()      # GET shopping.jsp (request 901)

    grinder.sleep(2079)
    self.page10()     # GET addtocart (request 1001)

    grinder.sleep(2408)
    self.page11()     # GET welcome.jsp (request 1101)

    grinder.sleep(1608)
    self.page12()     # GET viewshoppingcart (request 1201)

    grinder.sleep(1835)
    self.page13()     # GET shopping.jsp (request 1301)

    grinder.sleep(1919)
    self.page14()     # GET addtocart (request 1401)

    grinder.sleep(1716)
    self.page15()     # GET welcome.jsp (request 1501)

    grinder.sleep(2511)
    self.page16()     # GET browsestore.jsp (request 1601)

    grinder.sleep(2902)
    self.page17()     # POST browsecategories (request 1701)

    grinder.sleep(1448)
    self.page18()     # GET welcome.jsp (request 1801)

    grinder.sleep(1747)
    self.page19()     # GET shopping.jsp (request 1901)

    grinder.sleep(2193)
    self.page20()     # GET addtocart (request 2001)

    grinder.sleep(1861)
    self.page21()     # GET welcome.jsp (request 2101)

    grinder.sleep(1989)
    self.page22()     # GET shopping.jsp (request 2201)

    grinder.sleep(1526)
    self.page23()     # GET addtocart (request 2301)

    grinder.sleep(1579)
    self.page24()     # GET welcome.jsp (request 2401)

    grinder.sleep(1420)
    self.page25()     # GET shopping.jsp (request 2501)

    grinder.sleep(1397)
    self.page26()     # GET addtocart (request 2601)

    grinder.sleep(1350)
    self.page27()     # GET welcome.jsp (request 2701)

    grinder.sleep(1481)
    self.page28()     # GET browsestore.jsp (request 2801)

    grinder.sleep(1916)
    self.page29()     # POST browsecategories (request 2901)

    grinder.sleep(1806)
    self.page30()     # GET welcome.jsp (request 3001)

    grinder.sleep(1659)
    self.page31()     # GET viewshoppingcart (request 3101)

    grinder.sleep(2091)
    self.page32()     # GET shopping.jsp (request 3201)

    grinder.sleep(3976)
    self.page33()     # GET addtocart (request 3301)

    grinder.sleep(1885)
    self.page34()     # GET welcome.jsp (request 3401)

    grinder.sleep(2075)
    self.page35()     # GET shopping.jsp (request 3501)

    grinder.sleep(2424)
    self.page36()     # GET addtocart (request 3601)

    grinder.sleep(2114)
    self.page37()     # GET welcome.jsp (request 3701)

    grinder.sleep(1995)
    self.page38()     # GET shopping.jsp (request 3801)

    grinder.sleep(1905)
    self.page39()     # GET addtocart (request 3901)

    grinder.sleep(1626)
    self.page40()     # GET welcome.jsp (request 4001)

    grinder.sleep(1786)
    self.page41()     # GET shopping.jsp (request 4101)

    grinder.sleep(1949)
    self.page42()     # GET addtocart (request 4201)

    grinder.sleep(1582)
    self.page43()     # GET welcome.jsp (request 4301)

    grinder.sleep(2098)
    self.page44()     # GET viewshoppingcart (request 4401)


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
