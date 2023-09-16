# https://stackoverflow.com/questions/64675654/spacy-bilou-format-to-spacy-json-format/64677899#64677899
import spacy
from spacy.training import Example
from spacy.tokens import DocBin
import json

with open('train.json', 'r') as file:
    file_content = file.read()

TRAIN_DATA = json.loads(file_content)

nlp = spacy.blank("en")
db = DocBin()

for text, annotations in TRAIN_DATA:
    example = Example.from_dict(nlp.make_doc(text), annotations)
    db.add(example.reference)

db.to_disk("td.spacy")