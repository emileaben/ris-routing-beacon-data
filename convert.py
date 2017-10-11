#!/usr/bin/env python
import csv
import json

j = []
with open("ris-routing-beacons.tsv") as inf:
	for line in inf:
		line = line.rstrip('\n')
		(pfx,name,loc) = line.split('\t')
		typ = 'local'
		if name.startswith('RRC00'):
			typ = 'multihop'
		j.append({
			'pfx': pfx,
			'name': name,
			'location': loc,
			'type': typ
		})

print json.dumps( j , indent=2)
		
