""" Use k-means to locate voting clusters in US Congress """

import csv
from collections import defaultdict, namedtuple
from pprint import pprint
import glob

Senator = namedtuple('Senator', ['name', 'party', 'state'])

vote_value = {'Yea': 1, 'Nay': -1, 'Not Voting': 0}

accumulated_record: dict = defaultdict(list)
for filename in glob.glob('congress_data/*.csv'):
    with open(
            'congress_data/congress_votes_116-2019_h141.csv',
            encoding='utf-8') as f:
        reader = csv.reader(f)
        vote_topic = next(reader)
        headers = next(reader)
        for person, state, district, vote, name, party in reader:
            senator = Senator(name, party, state)
            accumulated_record[senator].append(vote)

pprint(accumulated_record)
