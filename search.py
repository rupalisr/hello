def first_search(page):
     start_link=page.find("<a href=")
     start_quote=page.find('"',start_link)
     end_quote=page.find('"',start_quote+1)
     url=page[start_quote:end_quote+1]
     return url,end_quote
def page_all_url(page):
    while True:
       url,end_quote=first_search(page)
       if(url):
          print(url)
          page=page[end_quote:]
       else:
          break
page_all_url('your email id is <a href="rupalisr0895@ggmail.com"> .....<a href="www.facebook.com">....yahoo acoount is<a href="www.yahoo2134.com">....')   
