# archiv pass - 971
# Archive password: 7777
# The file is password protected - 2758954
# Password: EY2KfXjueK
# The password for the document is ZzEHhMPJr
# The ZIP pass: pVSbnmhsl
# I have attached the current invoice and the password for the document is: 1234

import spacy
import random
from spacy.training.example import Example
import json
import pprint
import time
from datetime import timedelta
from colorama import init

init(autoreset=True)

# Load custom NER model
spacy.require_gpu()
custom_ner_model = spacy.load('output/model-best')

# view meta data of the model
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(custom_ner_model.meta)

while True:
    user_input = input("#>")
    if user_input == 'exit' :
        exit(0)
    elif user_input == '' :
        continue

    start_time = time.time()
    doc_custom = custom_ner_model(user_input)
    end_time = time.time()
    elapsed_time = timedelta(seconds=end_time - start_time)
    print()

    print("Result: ", end='')

    for ent in doc_custom.ents:
        print(f"\033[0;31m{ent.text}\033[0m", " : ", end='')
        print(f"{elapsed_time}s")

    print("")
