import requests

class HttpHandler(object):
    
    def getContentFromUrl(self, urlAddress):
        try:
            page = requests.get(urlAddress)
        except:
            print("Page not opened! ", urlAddress)
            return ''
        
        return str(page.content)





