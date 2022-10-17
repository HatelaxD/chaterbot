class Meaning:
    """By passing refactored input this class calculate the meaning of sentence
       Simple algorithm will predict what user want to know
    """

    from difflib import SequenceMatcher
    import json
    import requests

    def __init__(self):
        self.classifier_words = {
            "Craft_question": ['how', 'do', 'does,', 'would', 'can', 'could',
                               'i', 'is', 'be', 'was', 'were', 'to', 'been',
                               'craft', 'crafted', 'make', 'made',
                               'solution', 'recipe',
                               'know', 'about'],
            "Item_question": ['what', 'can', 'could',
                              'i', 'is', 'be',
                              'do', 'did', 'done', 'like', 'for', 'used',
                              'with'],
            "Greeting": ['hi', 'hello', 'good', 'morning', 'afternoon', 'yo',
                         'hey'],
            "Feeling": ['how', 'do', 'you', 'feel', 'are', 'you', 'feeling',
                        'mood', 'what', 'is'],
            "Thanks": ['goodbot', 'good', 'bot', 'thanks', 'thank', 'you', 'nice']
        }

        self.normal_words = [
            'sven', 'how', 'do', 'does,', 'would', 'can', 'could',
            'i', 'is', 'be', 'was', 'were', 'to', 'been',
            'craft', 'crafted', 'make', 'made',
            'solution', 'recipe',
            'know', 'about', 'what', 'can', 'could',
            'i', 'is', 'be',
            'do', 'did', 'done', 'like', 'for', 'used',
            'with', 'hi', 'hello', 'good', 'morning', 'afternoon', 'yo',
            'hey'
        ]

        self.items_names = self.requests.get("http://51.83.46.159:8000/allItems/?format=json").json()

    def predict(self, refactored_sentence, unrefactored_sentence):
        """returns list of sentence type, Minecraft item name, and confidence of prediction (percentage)"""
        max_local = 0
        max_global = 0
        final_type = None
        confidence1 = 0
        confidence2 = 0
        for key in self.classifier_words:
            for word in refactored_sentence[0]:
                if word[0] in self.classifier_words.get(key):
                    max_local = max_local + 1 + word[1]
            if max_local > max_global:
                confidence2 = confidence1
                confidence1 = max_local - max_global
                max_global = max_local
                final_type = key
            max_local = 0

        item_name = None
        for item in self.items_names:
            if item['itemTitle'].lower() in unrefactored_sentence:
                item_name = item
                break

        possible_items = list()
        if item_name is None:
            possible_item_words = list()
            for word in refactored_sentence[0]:
                if word[0] not in self.normal_words:
                    possible_item_words.append(word[0])

            for item in self.items_names:
                if len(possible_items) >= 10:
                    break;
                for word in possible_item_words:
                    if word in item['itemTitle'].lower():
                        possible_items.append(item['itemTitle'].lower())
                        continue
                    for item_part in item['itemTitle'].lower():
                        similarity = self.SequenceMatcher(None, item_part, word).ratio()
                        if similarity > 0.5:
                            possible_items.append(item['itemTitle'].lower())
                            break

        confidence_percentage = 100
        if confidence2 is not 0:
            confidence_percentage = confidence_percentage - confidence1 * 100 / confidence2
        return final_type, item_name, confidence_percentage, possible_items
