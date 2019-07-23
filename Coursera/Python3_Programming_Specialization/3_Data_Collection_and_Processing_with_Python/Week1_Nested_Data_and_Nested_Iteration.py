print("============================================")
print("Python 3 Programming Specialization")
print("Course 3 : Data Collection and Processing with Python")
print("Week 1 : Nested Data and Nested Iteration")

print("")

print("============================================")
print("============ 1.1. Nested Lists =============")
print("--------------------------------------------")
nested1 = [["a", "b", "c"], ["d", "e"], ["f", "g", "h"]]
print(nested1[0])
print(len(nested1))
print(len(nested1[1]))
nested1.append(["i"])
for L in nested1:
	print(L)

print("")

nested1 = [["a", "b", "c"], ["d", "e"], ["f", "g", "h"]]
y = nested1[1]
print(y)
print(y[0])

print([10, 20, 30][1])
print(nested1[1][0])

print("")

nested1 = [["a", "b", "c"], ["d", "e"], ["f", "g", "h"], ["i"]]
print(nested1)
nested1[1] = [1, 2, 3]
print(nested1)
nested1[1][0] = 100
print(nested1)

print("")

nested2 = [{'a': 1, 'b': 3}, {'a': 5, 'c': 90, 5: 50}, {'b': 3, 'c': "yes"}]
print(nested2)
print(nested2[1])
print(nested2[1]["c"])
nested2[1]["c"] = 7
print(nested2[1])
print(nested2[2])
nested2[2]["c"] = "no"
print(nested2[2])
print(nested2)

print("")

def square(x):
	return x*x

L = [square, abs, lambda x: x+1]

print("***names***")
for f in L:
	print(f)

print("***call each of them***")
for f in L:
	print(f(-2))

print("***just the first one in the list***")
print(L[0])
print(L[0](3))


print("")

animals = [['cat', 'dog', 'mouse'], ['horse', 'cow', 'goat'], ['cheetah', 'giraffe', 'rhino']]
idx1 = animals[1][0]
print(idx1)


print("")

data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []], [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]

plant = data[7][0][0]
print(plant)

print("")

print("============================================")
print("========= 1.2. Nested Dictionaries =========")
print("--------------------------------------------")
info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }

color = info["personal_data"]["physical_features"]["color"]
print(color)

print("")

print("============================================")
print("=== 1.3. JSON Format and the JSON Module ===")
print("--------------------------------------------")
import json
a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(a_string)
d = json.loads(a_string)

print("")

print(type(d))
print(d.keys())
print(d["resultCount"])
print(d)

print("")

def pretty(obj):
	return json.dumps(obj, indent=2)

d = {'key1': {'c': True, 'a': 90, 5: 50}, 'key2':{'b': 3, 'c': "yes"}}

print(d)
print("")
print(pretty(d))

print("")

print("============================================")
print("=========== 1.3. Nested Iteration ==========")
print("--------------------------------------------")
nested1 = [["a", "b", "c"], ["d", "e"], ["f", "g", "h"]]
for x in nested1:
	print("level1: ")
	for y in x:
		print("    level2: " + y)

print("")

info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]


last_names = []

for celeb in info:
	last_names.append(celeb[1])

print(last_names)

print("")

L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]

b_strings = []

for lst in L:
	for item in lst:
		if "b" in item:
			b_strings.append(item)

print(b_strings)

print("")

print("============================================")
print("====== 1.5. Structuring Nested Data ========")
print("--------------------------------------------")
nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
	print("level1")
	if type(x) is list:
		for y in x:
			print("     level2: {}".format(y))
	else:
		print(x)

print("")

print("============================================")
print("======= 1.6. Deep and Shallow Copies =======")
print("--------------------------------------------")
original = [["dogs", "puppies"], ["cats", "kittens"]]
copied_version = original[:]
print(copied_version)
print(copied_version is original)
print(copied_version == original)

original[0].append(["canines"])
print(original)
print("----Now look at the copied version----")
print(copied_version)

print("")

original = [["dogs", "puppies"], ["cats", "kittens"]]
copied_outer_list = []

for inner_list in original:
	copied_inner_list = []
	for item in inner_list:
		copied_inner_list.append(item)
	copied_outer_list.append(copied_inner_list)

print(copied_outer_list)

original[0].append(["canines"])
print(original)
print("----Now look at the copied version----")
print(copied_outer_list)

print("")

original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_outer_list = []
for inner_list in original:
	copied_inner_list = inner_list[:]
	copied_outer_list.append(copied_inner_list)
print(copied_outer_list)

original[0].append(["canines"])
print(original)
print("----Now look at the copied version----")
print(copied_outer_list)

print("")

import copy
original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]

shallow_copy_version = original[:]
deeply_copied_version = copy.deepcopy(original)

original.append("Hi there")
original[0].append(["marsupials"])

print("---- Original ----")
print(original)
print("---- Depp copy ----")
print(deeply_copied_version)
print("---- Shallow copy -----")
print(shallow_copy_version)

print("")

print("============================================")
print("===== 1.7. Extracting from Nested Data =====")
print("--------------------------------------------")
res = {
  "search_metadata": {
    "count": 3,
    "completed_in": 0.015,
    "max_id_str": "536624519285583872",
    "since_id_str": "0",
    "next_results": "?max_id=536623674942439424&q=University%20of%20Michigan&count=3&include_entities=1",
    "refresh_url": "?since_id=536624519285583872&q=University%20of%20Michigan&include_entities=1",
    "since_id": 0,
    "query": "University+of+Michigan",
    "max_id": 536624519285583872
  },
  "statuses": [
    {
      "contributors": None,
      "truncated": False,
      "text": "RT @mikeweber25: I'm decommiting from the university of Michigan thank you Michigan for the love and support I'll remake my decision at the\u2026",
      "in_reply_to_status_id": None,
      "id": 536624519285583872,
      "favorite_count": 0,
      "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
      "retweeted": False,
      "coordinates": None,
      "entities": {
        "symbols": [],
        "user_mentions": [
          {
            "id": 1119996684,
            "indices": [
              3,
              15
            ],
            "id_str": "1119996684",
            "screen_name": "mikeweber25",
            "name": "Mikey"
          }
        ],
        "hashtags": [],
        "urls": []
      },
      "in_reply_to_screen_name": None,
      "in_reply_to_user_id": None,
      "retweet_count": 2014,
      "id_str": "536624519285583872",
      "favorited": False,
      "retweeted_status": {
        "contributors": None,
        "truncated": False,
        "text": "I'm decommiting from the university of Michigan thank you Michigan for the love and support I'll remake my decision at the army bowl",
        "in_reply_to_status_id": None,
        "id": 536300265616322560,
        "favorite_count": 1583,
        "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
        "retweeted": False,
        "coordinates": None,
        "entities": {
          "symbols": [],
          "user_mentions": [],
          "hashtags": [],
          "urls": []
        },
        "in_reply_to_screen_name": None,
        "in_reply_to_user_id": None,
        "retweet_count": 2014,
        "id_str": "536300265616322560",
        "favorited": False,
        "user": {
          "follow_request_sent": False,
          "profile_use_background_image": True,
          "profile_text_color": "666666",
          "default_profile_image": False,
          "id": 1119996684,
          "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme9/bg.gif",
          "verified": False,
          "profile_location": None,
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/534465900343083008/A09dIq1d_normal.jpeg",
          "profile_sidebar_fill_color": "252429",
          "entities": {
            "description": {
              "urls": []
            }
          },
          "followers_count": 5444,
          "profile_sidebar_border_color": "FFFFFF",
          "id_str": "1119996684",
          "profile_background_color": "C0DEED",
          "listed_count": 36,
          "is_translation_enabled": False,
          "utc_offset": None,
          "statuses_count": 6525,
          "description": "Mike Weber (U.S Army All American) DETROIT CTSENIOR State Champion",
          "friends_count": 693,
          "location": "",
          "profile_link_color": "0084B4",
          "profile_image_url": "http://pbs.twimg.com/profile_images/534465900343083008/A09dIq1d_normal.jpeg",
          "following": False,
          "geo_enabled": False,
          "profile_banner_url": "https://pbs.twimg.com/profile_banners/1119996684/1416261575",
          "profile_background_image_url": "http://abs.twimg.com/images/themes/theme9/bg.gif",
          "name": "Mikey",
          "lang": "en",
          "profile_background_tile": False,
          "favourites_count": 1401,
          "screen_name": "mikeweber25",
          "notifications": False,
          "url": None,
          "created_at": "Fri Jan 25 18:45:53 +0000 2013",
          "contributors_enabled": False,
          "time_zone": None,
          "protected": False,
          "default_profile": False,
          "is_translator": False
        },
        "geo": None,
        "in_reply_to_user_id_str": None,
        "lang": "en",
        "created_at": "Sat Nov 22 23:28:41 +0000 2014",
        "in_reply_to_status_id_str": None,
        "place": None,
        "metadata": {
          "iso_language_code": "en",
          "result_type": "recent"
        }
      },
      "user": {
        "follow_request_sent": False,
        "profile_use_background_image": True,
        "profile_text_color": "333333",
        "default_profile_image": False,
        "id": 2435537208,
        "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
        "verified": False,
        "profile_location": None,
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/532694075947110400/oZEP5XNQ_normal.jpeg",
        "profile_sidebar_fill_color": "DDEEF6",
        "entities": {
          "description": {
            "urls": []
          }
        },
        "followers_count": 161,
        "profile_sidebar_border_color": "C0DEED",
        "id_str": "2435537208",
        "profile_background_color": "C0DEED",
        "listed_count": 0,
        "is_translation_enabled": False,
        "utc_offset": None,
        "statuses_count": 524,
        "description": "Delasalle '17 Baseball & Football.",
        "friends_count": 255,
        "location": "",
        "profile_link_color": "0084B4",
        "profile_image_url": "http://pbs.twimg.com/profile_images/532694075947110400/oZEP5XNQ_normal.jpeg",
        "following": False,
        "geo_enabled": False,
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/2435537208/1406779364",
        "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
        "name": "Andrew Brooks",
        "lang": "en",
        "profile_background_tile": False,
        "favourites_count": 555,
        "screen_name": "31brooks_",
        "notifications": False,
        "url": None,
        "created_at": "Wed Apr 09 14:34:41 +0000 2014",
        "contributors_enabled": False,
        "time_zone": None,
        "protected": False,
        "default_profile": True,
        "is_translator": False
      },
      "geo": None,
      "in_reply_to_user_id_str": None,
      "lang": "en",
      "created_at": "Sun Nov 23 20:57:10 +0000 2014",
      "in_reply_to_status_id_str": None,
      "place": None,
      "metadata": {
        "iso_language_code": "en",
        "result_type": "recent"
      }
    },
    {
      "contributors": None,
      "truncated": False,
      "text": "RT @Plantedd: The University of Michigan moved a big Bur Oak yesterday. 65ft tall. 350+ tons. http://t.co/v2Y6vl3f9e",
      "in_reply_to_status_id": None,
      "id": 536624216305848320,
      "favorite_count": 0,
      "source": "<a href=\"http://tapbots.com/tweetbot\" rel=\"nofollow\">Tweetbot for i\u039fS</a>",
      "retweeted": False,
      "coordinates": None,
      "entities": {
        "symbols": [],
        "user_mentions": [
          {
            "id": 462890283,
            "indices": [
              3,
              12
            ],
            "id_str": "462890283",
            "screen_name": "Plantedd",
            "name": "David Wong"
          }
        ],
        "hashtags": [],
        "urls": [],
        "media": [
          {
            "source_status_id_str": "526276522374889472",
            "expanded_url": "http://twitter.com/Plantedd/status/526276522374889472/photo/1",
            "display_url": "pic.twitter.com/v2Y6vl3f9e",
            "url": "http://t.co/v2Y6vl3f9e",
            "media_url_https": "https://pbs.twimg.com/media/B021tLsIYAADq21.jpg",
            "source_status_id": 526276522374889472,
            "id_str": "526276519308845056",
            "sizes": {
              "small": {
                "h": 191,
                "resize": "fit",
                "w": 340
              },
              "large": {
                "h": 576,
                "resize": "fit",
                "w": 1024
              },
              "medium": {
                "h": 337,
                "resize": "fit",
                "w": 600
              },
              "thumb": {
                "h": 150,
                "resize": "crop",
                "w": 150
              }
            },
            "indices": [
              94,
              116
            ],
            "type": "photo",
            "id": 526276519308845056,
            "media_url": "http://pbs.twimg.com/media/B021tLsIYAADq21.jpg"
          }
        ]
      },
      "in_reply_to_screen_name": None,
      "in_reply_to_user_id": None,
      "retweet_count": 27,
      "id_str": "536624216305848320",
      "favorited": False,
      "retweeted_status": {
        "contributors": None,
        "truncated": False,
        "text": "The University of Michigan moved a big Bur Oak yesterday. 65ft tall. 350+ tons. http://t.co/v2Y6vl3f9e",
        "in_reply_to_status_id": None,
        "id": 526276522374889472,
        "favorite_count": 25,
        "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
        "retweeted": False,
        "coordinates": None,
        "entities": {
          "symbols": [],
          "user_mentions": [],
          "hashtags": [],
          "urls": [],
          "media": [
            {
              "expanded_url": "http://twitter.com/Plantedd/status/526276522374889472/photo/1",
              "display_url": "pic.twitter.com/v2Y6vl3f9e",
              "url": "http://t.co/v2Y6vl3f9e",
              "media_url_https": "https://pbs.twimg.com/media/B021tLsIYAADq21.jpg",
              "id_str": "526276519308845056",
              "sizes": {
                "small": {
                  "h": 191,
                  "resize": "fit",
                  "w": 340
                },
                "large": {
                  "h": 576,
                  "resize": "fit",
                  "w": 1024
                },
                "medium": {
                  "h": 337,
                  "resize": "fit",
                  "w": 600
                },
                "thumb": {
                  "h": 150,
                  "resize": "crop",
                  "w": 150
                }
              },
              "indices": [
                80,
                102
              ],
              "type": "photo",
              "id": 526276519308845056,
              "media_url": "http://pbs.twimg.com/media/B021tLsIYAADq21.jpg"
            }
          ]
        },
        "in_reply_to_screen_name": None,
        "in_reply_to_user_id": None,
        "retweet_count": 27,
        "id_str": "526276522374889472",
        "favorited": False,
        "user": {
          "follow_request_sent": False,
          "profile_use_background_image": True,
          "profile_text_color": "333333",
          "default_profile_image": False,
          "id": 462890283,
          "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
          "verified": False,
          "profile_location": None,
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/1791926707/Plantedd_Logo__square__normal.jpg",
          "profile_sidebar_fill_color": "DDEEF6",
          "entities": {
            "url": {
              "urls": [
                {
                  "url": "http://t.co/ZOnsCHvoKt",
                  "indices": [
                    0,
                    22
                  ],
                  "expanded_url": "http://www.plantedd.com",
                  "display_url": "plantedd.com"
                }
              ]
            },
            "description": {
              "urls": []
            }
          },
          "followers_count": 2598,
          "profile_sidebar_border_color": "C0DEED",
          "id_str": "462890283",
          "profile_background_color": "C0DEED",
          "listed_count": 61,
          "is_translation_enabled": False,
          "utc_offset": 0,
          "statuses_count": 8157,
          "description": "Hello, I'm the supervillain behind Plantedd. We're an online market for plant lovers plotting to take over the world by making it simple to find and buy plants.",
          "friends_count": 2664,
          "location": "UK",
          "profile_link_color": "0084B4",
          "profile_image_url": "http://pbs.twimg.com/profile_images/1791926707/Plantedd_Logo__square__normal.jpg",
          "following": False,
          "geo_enabled": False,
          "profile_banner_url": "https://pbs.twimg.com/profile_banners/462890283/1398254314",
          "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
          "name": "David Wong",
          "lang": "en",
          "profile_background_tile": False,
          "favourites_count": 371,
          "screen_name": "Plantedd",
          "notifications": False,
          "url": "http://t.co/ZOnsCHvoKt",
          "created_at": "Fri Jan 13 13:46:46 +0000 2012",
          "contributors_enabled": False,
          "time_zone": "Edinburgh",
          "protected": False,
          "default_profile": True,
          "is_translator": False
        },
        "geo": None,
        "in_reply_to_user_id_str": None,
        "possibly_sensitive": False,
        "lang": "en",
        "created_at": "Sun Oct 26 07:37:55 +0000 2014",
        "in_reply_to_status_id_str": None,
        "place": None,
        "metadata": {
          "iso_language_code": "en",
          "result_type": "recent"
        }
      },
      "user": {
        "follow_request_sent": False,
        "profile_use_background_image": True,
        "profile_text_color": "2A48AE",
        "default_profile_image": False,
        "id": 104940733,
        "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme17/bg.gif",
        "verified": False,
        "profile_location": None,
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/2878477539/78e20432088b5ee2addc9ce3362fd461_normal.jpeg",
        "profile_sidebar_fill_color": "6378B1",
        "entities": {
          "description": {
            "urls": []
          }
        },
        "followers_count": 149,
        "profile_sidebar_border_color": "FBD0C9",
        "id_str": "104940733",
        "profile_background_color": "0C003D",
        "listed_count": 18,
        "is_translation_enabled": False,
        "utc_offset": 0,
        "statuses_count": 16031,
        "description": "Have you any dreams you'd like to sell?",
        "friends_count": 248,
        "location": "",
        "profile_link_color": "0F1B7C",
        "profile_image_url": "http://pbs.twimg.com/profile_images/2878477539/78e20432088b5ee2addc9ce3362fd461_normal.jpeg",
        "following": False,
        "geo_enabled": False,
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/104940733/1410032966",
        "profile_background_image_url": "http://abs.twimg.com/images/themes/theme17/bg.gif",
        "name": "Heather",
        "lang": "en",
        "profile_background_tile": False,
        "favourites_count": 777,
        "screen_name": "froyoho",
        "notifications": False,
        "url": None,
        "created_at": "Thu Jan 14 21:37:54 +0000 2010",
        "contributors_enabled": False,
        "time_zone": "London",
        "protected": False,
        "default_profile": False,
        "is_translator": False
      },
      "geo": None,
      "in_reply_to_user_id_str": None,
      "possibly_sensitive": False,
      "lang": "en",
      "created_at": "Sun Nov 23 20:55:57 +0000 2014",
      "in_reply_to_status_id_str": None,
      "place": None,
      "metadata": {
        "iso_language_code": "en",
        "result_type": "recent"
      }
    },
    {
      "contributors": None,
      "truncated": False,
      "text": "RT @NotableHistory: Madonna, 18 year old freshman at the University of Michigan, 1976 http://t.co/x2dm1G67ea",
      "in_reply_to_status_id": None,
      "id": 536623674942439425,
      "favorite_count": 0,
      "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
      "retweeted": False,
      "coordinates": None,
      "entities": {
        "symbols": [],
        "user_mentions": [
          {
            "id": 844766941,
            "indices": [
              3,
              18
            ],
            "id_str": "844766941",
            "screen_name": "NotableHistory",
            "name": "OnThisDay & Facts"
          }
        ],
        "hashtags": [],
        "urls": [],
        "media": [
          {
            "source_status_id_str": "536610190334779392",
            "expanded_url": "http://twitter.com/NotableHistory/status/536610190334779392/photo/1",
            "display_url": "pic.twitter.com/x2dm1G67ea",
            "url": "http://t.co/x2dm1G67ea",
            "media_url_https": "https://pbs.twimg.com/media/B3EXbQkCMAEipwM.jpg",
            "source_status_id": 536610190334779392,
            "id_str": "536235587703812097",
            "sizes": {
              "small": {
                "h": 487,
                "resize": "fit",
                "w": 340
              },
              "large": {
                "h": 918,
                "resize": "fit",
                "w": 640
              },
              "medium": {
                "h": 860,
                "resize": "fit",
                "w": 600
              },
              "thumb": {
                "h": 150,
                "resize": "crop",
                "w": 150
              }
            },
            "indices": [
              86,
              108
            ],
            "type": "photo",
            "id": 536235587703812097,
            "media_url": "http://pbs.twimg.com/media/B3EXbQkCMAEipwM.jpg"
          }
        ]
      },
      "in_reply_to_screen_name": None,
      "in_reply_to_user_id": None,
      "retweet_count": 9,
      "id_str": "536623674942439425",
      "favorited": False,
      "retweeted_status": {
        "contributors": None,
        "truncated": False,
        "text": "Madonna, 18 year old freshman at the University of Michigan, 1976 http://t.co/x2dm1G67ea",
        "in_reply_to_status_id": None,
        "id": 536610190334779392,
        "favorite_count": 13,
        "source": "<a href=\"https://ads.twitter.com\" rel=\"nofollow\">Twitter Ads</a>",
        "retweeted": False,
        "coordinates": None,
        "entities": {
          "symbols": [],
          "user_mentions": [],
          "hashtags": [],
          "urls": [],
          "media": [
            {
              "expanded_url": "http://twitter.com/NotableHistory/status/536610190334779392/photo/1",
              "display_url": "pic.twitter.com/x2dm1G67ea",
              "url": "http://t.co/x2dm1G67ea",
              "media_url_https": "https://pbs.twimg.com/media/B3EXbQkCMAEipwM.jpg",
              "id_str": "536235587703812097",
              "sizes": {
                "small": {
                  "h": 487,
                  "resize": "fit",
                  "w": 340
                },
                "large": {
                  "h": 918,
                  "resize": "fit",
                  "w": 640
                },
                "medium": {
                  "h": 860,
                  "resize": "fit",
                  "w": 600
                },
                "thumb": {
                  "h": 150,
                  "resize": "crop",
                  "w": 150
                }
              },
              "indices": [
                66,
                88
              ],
              "type": "photo",
              "id": 536235587703812097,
              "media_url": "http://pbs.twimg.com/media/B3EXbQkCMAEipwM.jpg"
            }
          ]
        },
        "in_reply_to_screen_name": None,
        "in_reply_to_user_id": None,
        "retweet_count": 9,
        "id_str": "536610190334779392",
        "favorited": False,
        "user": {
          "follow_request_sent": False,
          "profile_use_background_image": True,
          "profile_text_color": "333333",
          "default_profile_image": False,
          "id": 844766941,
          "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/458461302696837121/rGlGdWsc.png",
          "verified": False,
          "profile_location": None,
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/481243404320251905/gCr1cVP2_normal.png",
          "profile_sidebar_fill_color": "DDFFCC",
          "entities": {
            "url": {
              "urls": [
                {
                  "url": "http://t.co/9fTPk5A4wh",
                  "indices": [
                    0,
                    22
                  ],
                  "expanded_url": "http://notablefacts.com/",
                  "display_url": "notablefacts.com"
                }
              ]
            },
            "description": {
              "urls": []
            }
          },
          "followers_count": 73817,
          "profile_sidebar_border_color": "FFFFFF",
          "id_str": "844766941",
          "profile_background_color": "9AE4E8",
          "listed_count": 485,
          "is_translation_enabled": False,
          "utc_offset": -21600,
          "statuses_count": 38841,
          "description": "On This Day in History, Historical Pictures & other Interesting Facts....Historyfollower@gmail.com",
          "friends_count": 43594,
          "location": "",
          "profile_link_color": "0084B4",
          "profile_image_url": "http://pbs.twimg.com/profile_images/481243404320251905/gCr1cVP2_normal.png",
          "following": False,
          "geo_enabled": False,
          "profile_banner_url": "https://pbs.twimg.com/profile_banners/844766941/1411076349",
          "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/458461302696837121/rGlGdWsc.png",
          "name": "OnThisDay & Facts",
          "lang": "en",
          "profile_background_tile": True,
          "favourites_count": 1383,
          "screen_name": "NotableHistory",
          "notifications": False,
          "url": "http://t.co/9fTPk5A4wh",
          "created_at": "Tue Sep 25 03:08:59 +0000 2012",
          "contributors_enabled": False,
          "time_zone": "Central Time (US & Canada)",
          "protected": False,
          "default_profile": False,
          "is_translator": False
        },
        "geo": None,
        "in_reply_to_user_id_str": None,
        "possibly_sensitive": False,
        "lang": "en",
        "created_at": "Sun Nov 23 20:00:13 +0000 2014",
        "in_reply_to_status_id_str": None,
        "place": None,
        "metadata": {
          "iso_language_code": "en",
          "result_type": "recent"
        }
      },
      "user": {
        "follow_request_sent": False,
        "profile_use_background_image": True,
        "profile_text_color": "333333",
        "default_profile_image": False,
        "id": 818185729,
        "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
        "verified": False,
        "profile_location": None,
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/486215801498640384/rz9o7LnF_normal.jpeg",
        "profile_sidebar_fill_color": "DDEEF6",
        "entities": {
          "description": {
            "urls": []
          }
        },
        "followers_count": 302,
        "profile_sidebar_border_color": "C0DEED",
        "id_str": "818185729",
        "profile_background_color": "C0DEED",
        "listed_count": 0,
        "is_translation_enabled": False,
        "utc_offset": None,
        "statuses_count": 395,
        "description": "Formerly with California Dept of General Services, now freelancing around the Sacramento area...",
        "friends_count": 1521,
        "location": "Citrus Heights, CA",
        "profile_link_color": "0084B4",
        "profile_image_url": "http://pbs.twimg.com/profile_images/486215801498640384/rz9o7LnF_normal.jpeg",
        "following": False,
        "geo_enabled": True,
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/818185729/1383764759",
        "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
        "name": "M Duncan",
        "lang": "en",
        "profile_background_tile": False,
        "favourites_count": 6544,
        "screen_name": "MDuncan95814",
        "notifications": False,
        "url": None,
        "created_at": "Tue Sep 11 21:02:09 +0000 2012",
        "contributors_enabled": False,
        "time_zone": None,
        "protected": False,
        "default_profile": True,
        "is_translator": False
      },
      "geo": None,
      "in_reply_to_user_id_str": None,
      "possibly_sensitive": False,
      "lang": "en",
      "created_at": "Sun Nov 23 20:53:48 +0000 2014",
      "in_reply_to_status_id_str": None,
      "place": None,
      "metadata": {
        "iso_language_code": "en",
        "result_type": "recent"
      }
    }
  ]
}

import json
#print(json.dumps(res, indent=2)[:100])
#print("------------------")
#print(type(res))
#print(res.keys())

res2 = res["statuses"]
#print("------ Level 2 -------")
#print(type(res2))
#print(len(res2))


for res3 in res2:
  #print("----- Level 3: a tweet -----")
  #print(json.dumps(res3, indent=2)[:30])
  #print(type(res3))
  #print(res3.keys())
  res4 = res3["user"]
  #print("----Level 4: the user who wrote the tweet----")
  #print(type(res4))
  #print(res4.keys())
  print(res4['screen_name'], res4['created_at'])

print("-----")

for res3 in res["statuses"]:
  print(res3["user"]["screen_name"], res3["user"]["created_at"])

print("")

print("============================================")
print("======= 1.8. Assessments & Exercises =======")
print("--------------------------------------------")
d = ['good morning', 'hello', 'chair', 'python', ['music', 'flowers', 'facebook', 'instagram', 'snapchat', ['On my Own', 'monster', 'Words dont come so easily', 'lead me right']], 'Stressed Out', 'Pauver Coeur', 'Reach for Tomorrow', 'mariners song', 'Wonder sleeps here']

m_list = []

for item in d:
	if type(item) is list:
		for inner_item in item:
			if type(inner_item) is list:
				for inner_item2 in inner_item:
					if "m" in inner_item2:
						m_list.append(inner_item2)
			else:
				if "m" in inner_item:
					m_list.append(inner_item)
	else:
		if "m" in item:
			m_list.append(item)

print(m_list)

print("")

pokemon = {'Trainer1':
          {'normal': {'rattatas':15, 'eevees': 2, 'ditto':1}, 'water': {'magikarps':3}, 'flying': {'zubats':8, 'pidgey': 12}},
          'Trainer2':
          {'normal': {'rattatas':25, 'eevees': 1}, 'water': {'magikarps':7}, 'flying': {'zubats':3, 'pidgey': 15}},
          'Trainer3':
          {'normal': {'rattatas':10, 'eevees': 3, 'ditto':2}, 'water': {'magikarps':2}, 'flying': {'zubats':3, 'pidgey': 20}},
          'Trainer4':
          {'normal': {'rattatas':17, 'eevees': 1}, 'water': {'magikarps':9}, 'flying': {'zubats':12, 'pidgey': 14}}}

r = 0
d = 0
p = 0

print(pokemon.keys())
print(pokemon["Trainer1"].keys())
print(pokemon["Trainer1"]["normal"].keys())
print(pokemon["Trainer1"]["water"].keys())
print(pokemon["Trainer1"]["flying"].keys())

print(pokemon["Trainer2"].keys())
print(pokemon["Trainer3"].keys())
print(pokemon["Trainer4"].keys())

for trainer in pokemon:
	types = ["normal", "water","flying"]
	for typ in types:
		for it in pokemon[trainer][typ]:
			if it == "rattatas":
				r+= pokemon[trainer][typ]["rattatas"]
			elif it == "ditto":
				d += pokemon[trainer][typ]["ditto"]
			elif it == "pidgey":
				p += pokemon[trainer][typ]["pidgey"]

print(r)
print(d)
print(p)


print("")


big_list = [[['one', 'two'], ['seven', 'eight']], [['nine', 'four'], ['three', 'one']], [['two', 'eight'], ['seven', 'four']], [['five', 'one'], ['four', 'two']], [['six', 'eight'], ['two', 'seven']], [['three', 'five'], ['one', 'six']], [['nine', 'eight'], ['five', 'four']], [['six', 'three'], ['four', 'seven']]]

word_counts = {}

def w_counter(alist):
	for item in alist:
		if type(item) is list:
			w_counter(item)
		else:
			if item in word_counts:
				word_counts[item] += 1
			else:
				word_counts[item] = 1

w_counter(big_list)
print(word_counts)


print("")

pokemon_go_data = {'bentspoon':
                  {'Rattata': 203, 'Pidgey': 120, 'Drowzee': 89, 'Squirtle': 35, 'Pikachu': 3, 'Eevee': 34, 'Magikarp': 300, 'Paras': 38},
                  'Laurne':
                  {'Pidgey': 169, 'Rattata': 245, 'Squirtle': 9, 'Caterpie': 38, 'Weedle': 97, 'Pikachu': 6, 'Nidoran': 44, 'Clefairy': 15, 'Zubat': 79, 'Dratini': 4},
                  'picklejarlid':
                  {'Rattata': 32, 'Drowzee': 15, 'Nidoran': 4, 'Bulbasaur': 3, 'Pidgey': 56, 'Weedle': 21, 'Oddish': 18, 'Magmar': 6, 'Spearow': 14},
                  'professoroak':
                  {'Charmander': 11, 'Ponyta': 9, 'Rattata': 107, 'Belsprout': 29, 'Seel': 19, 'Pidgey': 93, 'Shellder': 43, 'Drowzee': 245, 'Tauros': 18, 'Lapras': 18}}


pokemons = {}

for item in pokemon_go_data.keys():
	#print(pokemon_go_data[item])
	for poke in pokemon_go_data[item]:
		if poke in pokemons:
			pokemons[poke] += pokemon_go_data[item][poke]
		else:
			pokemons[poke] = pokemon_go_data[item][poke]

most_common_pokemon = sorted(pokemons, reverse=True, key=lambda x: pokemons[x])[0]
print(most_common_pokemon)


print("")

nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]

output = nested[1][2]
print(output)


print("")


lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
yellow = "yellow" in lst[2]
print(yellow)

#Test to see if 4 is in the second list of lst. Save to variable ``four``
four = 4 in lst[1]
print(four)

#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
orange = "orange" in lst[0]
print(orange)


print("")



L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
test1 = "hola" in L
print(test1)


# Test if [5, 8, 7] is in the list L. Save to variable name test2
test2 = [5,8,7] in L
print(test2)

# Test if 6.6 is in the third element of list L. Save to variable name test3
test3 = 6.6 in L[2]
print(test3)


print("")

nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
data = "data" in nested.keys()
print(data)

# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
twentyfour = 24 in nested.keys()
print(twentyfour)

# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.

whole = "whole" not in nested["window"]
print(whole)

# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.

physics = "physics" in nested.keys()
print(physics)


print("")

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

london_gold = 0

for medals in nested_d["London"]:
	if medals == "Great Britain":
		london_gold += nested_d["London"][medals]

print(london_gold)


print("")

sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
v1 = sports["swimming"][2]
print(v1)

# Assign the string 'platform' to the name v2
v2 = sports["diving"][1]
print(v2)

# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 = sports["gymnastics"]["women"]
print(v3)

# Assign the string 'rings' to the name v4
v4 = sports["gymnastics"]["men"][3]
print(v4)



print("")

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count = []

for oly in nested_d.keys():
	for country in nested_d[oly]:
		if country == "USA":
			US_count.append(nested_d[oly]["USA"])

print(US_count)


print("")

l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]

third = []

for lst in l_of_l:
	third.append(lst[2])

print(third)


print("")

athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]

t = []
other = []

for lst in athletes:
	for athlete in lst:
		if "t" in athlete:
			t.append(athlete)
		else:
			other.append(athlete)

print(t)
print(other)
