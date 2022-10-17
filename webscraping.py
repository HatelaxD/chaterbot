import re  # re is pythons standard library for regular expressions > no download needed
import requests  # requests is a library that allows HTTP requests > pip install requests
from bs4 import BeautifulSoup  # BeautifulSoup is a HTML parser for Python > pip install beautifulsoup4


def extract_ingredients_from_txt(item):
    """Find item from ingredients.txt, removes item then returns ingredients"""
    item = item.title()  # ingredients.txt is all title case
    whole_item = ""
    item_split = item.split(" ")
    if len(item_split) > 1:
        for i in range(0, len(item_split)):
            whole_item += item_split[i]  # appends each word from list to one string
    else:  # Crafting Table becomes CraftingTable
        whole_item = item
    ingredientsFile = open('ingredients.txt', "r")
    ingredients = ingredientsFile.readlines()
    for j in range(len(ingredients)):
        wordList = ingredients[j].split()  # splits each line of ingredients.txt into list of words
        if wordList[0] == whole_item:
            del [wordList[0]]  # removes 1st word as this is item and is not needed
            wordList = ' '.join(wordList)
            return wordList  # Crafting Table Ingredients: Wood planks becomes Ingredients: Wood planks


class GetWebInfo:
    def __init__(self):
        url = 'https://www.minecraftcraftingguide.net'  # website we're extracting HTML from
        response = requests.get(url)  # returns html from url
        self.soup = BeautifulSoup(response.text, "html.parser")  # bs4 is a html parser for Python

    def get_craft_info(self, item):
        """Finds info about item, including name, url (showing how to craft), description (what item is and how to
        use) and ingredients (how to craft item) """
        item_regex = r"\b" + item + r"\b"  # creates a regular expression of item including word boundaries so book
        # doesn't return bookshelf

        for i in range(0, len(self.soup.find_all('tr', class_="bottomline"))):
            data = self.soup.find_all('tr', class_="bottomline")[i]
            for x in range(0, len(data.find_all('img'))):
                img = data.find_all('img')[x]  # finds all imgs within data (tr's with class bottomline)
                desc = img.find_next_sibling('span')  # span (description) is ALWAYS after img
                img_title = img['title']
                img_link = img['src']
                contains_item = re.compile(item_regex, re.IGNORECASE)
                if contains_item.search(img_title):
                    print(img_title[9:], str(img_link)[2:], desc.text, extract_ingredients_from_txt(item))
                    return img_title[9:], str(img_link)[2:], desc.text, extract_ingredients_from_txt(item)
                    # splicing img_title as it contains "Crafting" which we can remove
                    # splicing img_link as first two characters are //
