#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import glob
import io
import random

def main(argv):
	#print u'哈哈'.encode('utf-8')
	inputDir = argv[0]
	os.chdir("./"+inputDir)
	outfile = "z_master.txt"
	data = []
	dict = {}
	for file in glob.glob("*.txt"):
		print(file)
		with io.open(file, mode = 'rb') as f:
			for line in f:
				arr = line.split(":")
				print line[:line.find(':')]
				key = line[:line.find(':')]
				val = line[line.find(':')+1:]
				arr = val.split(":")
				if(len(arr) == 1 or arr[1] == ''):
					val = val.strip() + ':0\n'
				dict[key] = val
				#dict[arr[0].decode('utf-8')] = arr[1]
	# for key, value in dict.iteritems():
	# 	print key
	write(dict,outfile)
	while True:
		q,a = random.choice(list(dict.items()))
		n = int(a.split(":")[1])
		q2,a2 = random.choice(list(dict.items()))
		n2 = int(a2.split(":")[1])
		if(n<n2):
			q = q2
			a = a2
			n = n2
		l = raw_input("q:"+q)
		l = raw_input(a)
		if(l=='n'):
			print 'no'
			dict[q] = a.split(":")[0]+':'+str(n+1)+'\n'
			write(dict,outfile)

def write(dict, file):
	file = open(file,'w')
	for key, value in dict.iteritems():
		str = key+":"+value
		file.write(str)
	file.close()

if __name__ == "__main__":
	main(sys.argv[1:])
