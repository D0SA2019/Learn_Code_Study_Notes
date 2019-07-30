print("============================================")
print("Python 3 Programming Specialization")
print("Course 3 : Data Collection and Processing with Python")
print("Week 3 : Internet APIs")

print("")

print("============================================")
print("============ 3.3. Fetching A Page ==========")
print("--------------------------------------------")
import requests
import json

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print(type(page))
print(page.text[:150])
print(page.url)

print("-----------")

x = page.json()
print(type(x))

print("--- first item in the list ---")
print(x[0])

print("--- the whole list, pretty printed ---")
print(json.dumps(x, indent=2))

print("")

print("============================================")
print("== 3.4. Generating URLs with requests.get ==")
print("--------------------------------------------")

d = {'q': '"violins and guitars"', 'tbm': 'isch'}
results = requests.get("https://google.com/search", params=d)
print(results.url)

print("")

kval_pairs = {"rel_rhy": "funny"}
page = requests.get("https://api.datamuse.com/words", params=kval_pairs)
print(page.text[:150])
print(page.url)

print("")

print("============================================")
print("= 3.5. Reading API Documentation: Datamuse =")
print("--------------------------------------------")

def get_rhymes(word):
  baseurl = "https://api.datamuse.com/words"
  params_diction = {} # Set up an empty dictionary for wuery parameters
  params_diction["rel_rhy"] = word
  params_diction["max"] = "3" # get at most 3 results
  resp = requests.get(baseurl,params=params_diction)
  #return the top three words
  word_ds = resp.json()
  return [d["word"] for d in word_ds]
  return resp.json() # return a python object (a list of dictionaries in this case)

print(get_rhymes("funny"))

print("")

print("============================================")
print("=== 3.6. Debugging Calls to requests.get ===")
print("--------------------------------------------")

dest_url = "https://www.google.com/search"
d = {"tbm": "isch", "q": "violins and guitars"}
resp = requests.get(dest_url, params=d)
print(resp.url)
print(resp.text[:200])

print("")
dest_url = "https://www.google.com/search"
d = {"tbm": "isch", "q": '"violins and guitars"'}
resp = requests.get(dest_url, params=d)
print(resp.url)
print(resp.text[:200])

print("")

print("============================================")
print("==== 3.8. Searching for Media on iTunes ====")
print("--------------------------------------------")
parameters = {"term": "Ann Arbor", "entity": "podcast"}
iTunes_response = requests.get("https://itunes.apple.com/search", params=parameters)

py_data = json.loads(iTunes_response.text)
print(json.dumps(py_data, indent=2)[:500])

print("")

print(json.dumps(py_data["results"], indent=2))

print("")

for r in py_data["results"]:
  print(r["trackName"])


print("")

print("============================================")
print("==== 3.11. Project - OMDB and TasteDive ====")
print("--------------------------------------------")
