#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the Quotes to Scrape site
url = 'http://quotes.toscrape.com/'
browser.visit(url)


# In[4]:


# Parse the HTML
html = browser.html
html_soup = soup(html, 'html.parser')


# In[5]:


# Scrape the Title
title = html_soup.find('h2').text
title


# In[6]:


# Scrape the top ten tags
tag_box = html_soup.find('div', class_='tags-box')
# tag_box
tags = tag_box.find_all('a', class_='tag')

for tag in tags:
    word = tag.text
    print(word)


# In[7]:


url = 'http://quotes.toscrape.com/'
browser.visit(url)


# In[8]:


for x in range(1, 6):
   html = browser.html
   quote_soup = soup (html, 'html.parser')
   quotes = quote_soup.find_all('span', class_='text')
   for quote in quotes:
      print('page:', x, '----------')
      print(quote.text)
   browser.links.find_by_partial_text('Next')


# In[9]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[10]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[11]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[12]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# # Featured Images

# In[13]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[14]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[15]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[16]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[17]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[18]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[19]:


df.to_html()


# In[20]:


browser.quit()


# # Deliverable 1
# 

# In[21]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[22]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path)


# # Visit the NASA Mars News Site

# In[23]:


# Visit the mars nasa news site
url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[24]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[25]:


slide_elem.find('div', class_='content_title')


# In[26]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[27]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# # JPL Space Images Featured Image

# In[28]:


# Visit URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# In[29]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[30]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[31]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[32]:


# Use the base url to create an absolute url
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url


# # Mars Facts

# In[33]:


df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]
df.head()


# In[34]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[35]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# Hemispheres

# In[36]:


# 1. Use browser to visit the URL 
hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

browser.visit(hemisphere_url)


# In[37]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):
        browser.find_by_css("a.product-item h3")[i].click()
        html = browser.html
        image_soup = soup(html, 'html.parser')
        image_url_rel = image_soup.find("a", text="Sample").get("href")
        hemisphere_title = image_soup.find('h2', class_='title').get_text()
        hemisphere_image_url = f'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars{image_url_rel}'
        hemispheres = {"title":hemisphere_title,"img_url":image_url_rel}
        hemisphere_image_urls.append(hemispheres)
        browser.back()


# In[38]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[39]:


# 5. Quit the browser
browser.quit()

