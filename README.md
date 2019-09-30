# Wiki first-link spider
## Overview
This is a very simple python web-crawler/spider. It takes a URL from the English-language Wikipedia and generates a list of increasingly general connected terms. 
### Problem statement 
I was curious to see where a user would end up if they were to follow the first link contained in the body of a Wikipedia article, and then kept applying the same logic until they encountered a previously visited article. I wanted to see the most common result of this logic when a random article is given, as well as the path the spider would take to get there.

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

### Restrictions

In order to avoid the chain of articles looping prematurely, I applied restrictions to the way the 'first link' is extracted. The spider will ignore the link and move on to find the next one in the following cases:

- the link does not lead to a separate article
- the link leads to a wikipedia help article
- the link leads to a file
- the link leads to a disambiguation page
- the link leads to an article on a language or a writing system (the reason being that many Wiki articles begin with linguistic information on the term's name, which meant that before applying this restriction most scrapes quickly fell into a chain of language-related terms)

Language and writing system articles to be excluded were scraped from appropriate index pages.

## Sample results

```
{"page title": "Carl Jung", "first href": "https://en.wikipedia.org/wiki/Psychiatrist"},
{"page title": "Psychiatrist", "first href": "https://en.wikipedia.org/wiki/Physician"},
{"page title": "Physician", "first href": "https://en.wikipedia.org/wiki/Professional"},
{"page title": "Professional", "first href": "https://en.wikipedia.org/wiki/Profession"},
{"page title": "Profession", "first href": "https://en.wikipedia.org/wiki/Educational"},
{"page title": "Education", "first href": "https://en.wikipedia.org/wiki/Learning"},
{"page title": "Learning", "first href": "https://en.wikipedia.org/wiki/Knowledge"},
{"page title": "Knowledge", "first href": "https://en.wikipedia.org/wiki/Fact"},
{"page title": "Fact", "first href": "https://en.wikipedia.org/wiki/Reality"},
{"page title": "Reality", "first href": "https://en.wikipedia.org/wiki/Object_of_the_mind"},
{"page title": "Object of the mind", "first href": "https://en.wikipedia.org/wiki/Object_(philosophy)"},
{"page title": "Object (philosophy)", "first href": "https://en.wikipedia.org/wiki/Philosophy"},
{"page title": "Philosophy", "first href": "https://en.wikipedia.org/wiki/Sophia_(wisdom)"},
{"page title": "Sophia (wisdom)", "first href": "https://en.wikipedia.org/wiki/Wisdom"},
{"page title": "Wisdom", "first href": "https://en.wikipedia.org/wiki/Knowledge"}
```

```
{"page title": "Abdullah Qureshi", "first href": "https://en.wikipedia.org/wiki/Activism"},
{"page title": "Activism", "first href": "https://en.wikipedia.org/wiki/Social_change"},
{"page title": "Social change", "first href": "https://en.wikipedia.org/wiki/Social_order"},
{"page title": "Social order", "first href": "https://en.wikipedia.org/wiki/Social_structure"},
{"page title": "Social structure", "first href": "https://en.wikipedia.org/wiki/Social_science"},
{"page title": "Social science", "first href": "https://en.wikipedia.org/wiki/Discipline_(academia)"},
{"page title": "Discipline (academia)", "first href": "https://en.wikipedia.org/wiki/Knowledge"},
{"page title": "Knowledge", "first href": "https://en.wikipedia.org/wiki/Fact"},
{"page title": "Fact", "first href": "https://en.wikipedia.org/wiki/Reality"},
{"page title": "Reality", "first href": "https://en.wikipedia.org/wiki/Object_of_the_mind"},
{"page title": "Object of the mind", "first href": "https://en.wikipedia.org/wiki/Object_(philosophy)"},
{"page title": "Object (philosophy)", "first href": "https://en.wikipedia.org/wiki/Philosophy"},
{"page title": "Philosophy", "first href": "https://en.wikipedia.org/wiki/Sophia_(wisdom)"},
{"page title": "Sophia (wisdom)", "first href": "https://en.wikipedia.org/wiki/Wisdom"},
{"page title": "Wisdom", "first href": "https://en.wikipedia.org/wiki/Knowledge"}
```