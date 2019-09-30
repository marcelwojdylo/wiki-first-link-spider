# Wiki term generalizer
## Overview
This is a very simple python web-crawler/spider. It takes a URL from the English-language Wikipedia and generates a list of increasingly general connected terms. 
### Problem statement 
I was curious to see where a user would end up if they were to follow the first link contained in the body of a Wikipedia article, and then kept applying the same logic until they encountered a previously visited article.

### Results
As it turns out, most randomly chosen Wikipedia articles, when this logic is applied to them, lead to either the article *Wisdom* or the article *Object of the mind*.

## Methodology
Broadly speaking, the spider scrapes the input page for the first term mentioned in the body of the Wikipedia article (with some restrictions, as explained further down this README), follows the link and applies the same logic to all resulting pages until it finds itself back on one of the pages it has already visited. 

The rationale is that, in a Wikipedia article, the first link in the body of the article is likely to lead to a connected, but more general term.

For instance, entering the URL for the *United States national missile defense* wiki article generates the following JSON:
```
{"page title":  "United States national missile defense", "first href":  "https://en.wikipedia.org/wiki/Missile_defense"},
{"page title":  "Missile defense", "first href":  "https://en.wikipedia.org/wiki/Missile"},
{"page title":  "Missile", "first href":  "https://en.wikipedia.org/wiki/Jet_engine"},
{"page title":  "Jet engine", "first href":  "https://en.wikipedia.org/wiki/Reaction_engine"},
{"page title":  "Reaction engine", "first href":  "https://en.wikipedia.org/wiki/Engine"},
{"page title":  "Engine", "first href":  "https://en.wikipedia.org/wiki/Machine"},
{"page title":  "Machine", "first href":  "https://en.wikipedia.org/wiki/Mechanical_structure"},
{"page title":  "Structural engineering", "first href":  "https://en.wikipedia.org/wiki/Civil_engineering"},
{"page title":  "Civil engineering", "first href":  "https://en.wikipedia.org/wiki/Regulation_and_licensure_in_engineering"},
{"page title":  "Regulation and licensure in engineering", "first href":  "https://en.wikipedia.org/wiki/Licensure"},
{"page title":  "Licensure", "first href":  "https://en.wikipedia.org/wiki/License"},
{"page title":  "License", "first href":  "https://en.wikipedia.org/wiki/Intellectual_property"},
{"page title":  "Intellectual property", "first href":  "https://en.wikipedia.org/wiki/Property"},
{"page title":  "Property", "first href":  "https://en.wikipedia.org/wiki/Abstract_and_concrete"},
{"page title":  "Abstract and concrete", "first href":  "https://en.wikipedia.org/wiki/Object_(philosophy)"},
{"page title":  "Object (philosophy)", "first href":  "https://en.wikipedia.org/wiki/Philosophy"},
{"page title":  "Philosophy", "first href":  "https://en.wikipedia.org/wiki/Sophia_(wisdom)"},
{"page title":  "Sophia (wisdom)", "first href":  "https://en.wikipedia.org/wiki/Wisdom"},
{"page title":  "Wisdom", "first href":  "https://en.wikipedia.org/wiki/Knowledge"},
{"page title":  "Knowledge", "first href":  "https://en.wikipedia.org/wiki/Fact"},
{"page title":  "Fact", "first href":  "https://en.wikipedia.org/wiki/Reality"},
{"page title":  "Reality", "first href":  "https://en.wikipedia.org/wiki/Object_of_the_mind"},
{"page title":  "Object of the mind", "first href":  "https://en.wikipedia.org/wiki/Object_(philosophy)"}
```