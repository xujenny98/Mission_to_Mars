# Mission_to_Mars
# Purpose 
Use BeautifulSoup and Splinter to scrape full-resolution images of Mar's hermisphere.  Store the scraped data on a Mongo database, and use a web application to display the data. 

# Results
<br/>**Deliverable 1** is to write codes to retreive the full-resolution image of each Mar's hermisphere with title for each hermisphere.
![Deliverable 1](https://user-images.githubusercontent.com/77771292/116021541-65a90880-a616-11eb-8d35-30160513aae2.png)
<br/> **Deliverable 2** using def scrape_all() function is written in Scraping.py file to create a new dictionary in the data dictionary to hold a list of dictionaries with the URL string and title of each hemisphere image. the def mars_facts() functions in Scraping.py file create a function that will scrape the hemisphere data by using your code from Mission_to_Mars_Challenge.py file and return the scrapped data as a list of dictionary with URL string. Then using PyMongo and setting up a MongoDB on our local machine we were able to store the data obtained from scraping in a database for continued use. We created the Flask app, and then connected to the MongoDB with the following: 
<br/>![Screen Shot 2021-04-25 at 11 39 27 PM](https://user-images.githubusercontent.com/77771292/116025878-7f028280-a61f-11eb-85e2-9ec10f27a6fa.png)
<br/> **Deliverable 3** uing the bootstrap to design the HTML page and display scraped data. Index.html file contains code that will display the full-resolution image URL and title for each hemisphere image.
