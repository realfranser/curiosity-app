# This scripts scrapes facts from webpages
# Selenium imports
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# Other imports
import time
import json
import unidecode

# Data
topics = {
    'random' : {
        'source' :['https://www.thefactsite.com/100-amazing-facts-you-never-knew/',
                    'https://www.thefactsite.com/top-100-random-funny-facts/'],
        'fact_list' : []
    },
    'technology' : {
        'source' :['https://www.thefactsite.com/top-100-technology-facts/',
                    'https://www.thefactsite.com/microsoft-facts/',
                    'https://www.thefactsite.com/youtube-facts/'],
        'fact_list' : []
    },
    'nature' : {
        'source' : ['https://www.thefactsite.com/100-space-facts/',
                    'https://www.thefactsite.com/cat-facts/',
                    'https://www.thefactsite.com/25-random-penguin-facts/',
                    'https://www.thefactsite.com/300-random-animal-facts/'],
        'fact_list' : []
    },
    'humanity' : {
        'source' : ['https://www.thefactsite.com/100-history-facts/',
                    'https://www.thefactsite.com/shakespeare-facts/',
                    'https://www.thefactsite.com/queen-band-facts/'],
        'fact_list' : []
    }
}

# Get path of the json file
json_path = "/Users/fserranoarrese/Projects/bootcamp-app/src/database/facts.json"


# Functions
def scrape():
    # Flag for the accept button
    first = True
    # Initiate the browser
    browser = webdriver.Chrome(ChromeDriverManager().install())
    # Search facts for each topic
    for topic, content in topics.items():
        # Get links of the websites related to a topic
        link_list = content['source']
        # Get facts from all links related to a certain topic
        for link in link_list:
            # Open the website containing the curiosities
            browser.get(link)
            # Click the accept button
            if first:
                time.sleep(5)
                first = False
            # Get list of curiosities about one topic
            #cur_list = browser.find_elements_by_xpath('/html/body/div[1]/div/div/main/article/div/div/h2')
            cur_list = browser.find_elements_by_class_name('list')

            # Print all the curiosities
            for i in range(1, len(cur_list)):
                decoded_text = unidecode.unidecode(cur_list[i].text)
                topics[topic]['fact_list'].append(decoded_text)

    # Close the automated browser
    browser.close()

def write_json():
    # Store facts into a JSON file at the folder ../database
    with open(json_path, 'w+') as json_file:
        json.dump(topics, json_file, indent=4)

def main():
    scrape()
    write_json()

if __name__ == "__main__":
    main()
