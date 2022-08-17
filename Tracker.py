import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

class Tracker():
    def __init__(self, url):
        self.url = url
    def set_tracking_url(self, url):
        self.tracking_url = url
    def update(self):
        pass
    def add_element_to_track(self, elem):
        pass
    def save(self, folder):
        pass 


class NewsSite(Tracker):
    def __init__(self, url):
        super().__init__(url)
        
    def set_tracking_url(self, url):
        super().set_tracking_url(url)
        
    def update(self):
        pass
    def add_element_to_track(self, elem):
        pass
    def save(self, folder):
        pass
        