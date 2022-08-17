class TrackingElement():
    def __init__(self, elem):
        self.identity = elem
        self.data = {}
    def collect_data(self):
        pass
    
 def get_main_text(tag):
    ls = tag.find_all('p')
    txt = ''
    for elem in ls:
        txt = txt + elem.text.strip() + '\n'
    return txt   


class Article(TrackingElement):
    def __init__(self, url):
        super().__init__(url)
    def collect_data(self):
        url = self.identity
        #send GET requests
        resp = requests.get(url)
        print(resp.status_code)

        #turn into soup
        soup = BeautifulSoup(resp.content, 'html.parser')

        #process data
        results = soup.find_all('div', attrs={'id':'mainContent'})
        tag = results[0]

        #title 
        title = soup.find_all('h1', attrs={'class':'title'})[0].text.strip()
        #tag
        category = soup.find_all('a', attrs={'class':'cat'})[0].text.strip()
        category_url = soup.find_all('a', attrs={'class':'cat'})[0].get('href')
        #summary
        summary = soup.find_all('h2', attrs={'class':'sapo'})[0].text.strip()
        #main text
        text = get_main_text(tag)

        tracking_elements_dict = {}
        tracking_elements_dict['title'] = title
        tracking_elements_dict['category'] = category
        tracking_elements_dict['category-url'] = category_url
        tracking_elements_dict['summary']  = summary
        tracking_elements_dict['text'] = text   
        
        self.data = tracking_elements_dict    
