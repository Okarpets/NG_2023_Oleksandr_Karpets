import json
jsonstr = '''{
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": [
                            "GML",
                            "XML"
                        ]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
} '''
json = json.loads(jsonstr)
Titleone = json['glossary']
Titletwostep = json['glossary']
Titletwo = Titletwostep['GlossDiv']
print("Title one: "'{}'.format(Titleone['title']))
print("Title two: "'{}'.format(Titletwo['title']))