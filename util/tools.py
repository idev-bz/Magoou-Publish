from math import sqrt
from operator import *
from itertools import *
from datetime import datetime
import re
import json

def prod(one):
	return reduce(mul, one)
	
def dot(one,two):
	return sum(imap(mul,one,two))
	
def magnitude(list):
	return sqrt(dot(list,list))
	
HTMLCODES = (
				('&', '&amp;'),
				('<', '&lt;'),
				('>', '&gt;'),
				('"', '&quot;'),
				("'", '&#39;'),
				('>>', '&raquo;'),
				('/', '&frasl;'),
				(' ', '&nbsp;'),
				("'", '&#8217;'),
				('--', '&#8211;'),
			)
	
def htmlDecode(string,encode=False):
	for before,after in HTMLCODES:
		if not encode:
			before,after = after,before
		string = string.replace(before,after)
	return string
	
def removeTags(string):
	string = htmlDecode(string)
	return re.sub(r'<[^<]*?>',' ',string)
	
def cleanText(string):
	string = removeTags(string)
	string = string.strip()
	return unicode(string)
	
def updateDictValue(dict,key,value,additive=True):
	# update value in dict, only for numbers
	if type(value) not in (float,int):
		raise NotImplementedError, 'Unsupported type: '+repr(type(value))
	
	try:
		if additive: dict[key] += value
		else: dict[key] *= value
	except KeyError:
		if additive: dict[key] = value
		else: dict[key] = value / len(dict)
	return dict
	
def updateDictValues(dict,value,additive=True):
	return completeDict(dict,dict.keys(),default=value,additive=additive)
	
def mergeDictss(dict,dict2,additive=True):
	for key,value in dict2.iteritems():
		updateDictValue(dict,key,value,additive=additive)
	return dict
	
def sortDictByValue(dict,revert=False):
	return sorted(dict.iteritems(),key=itemgetter(1),reverse=revert)
	
def completeDict(dict,keys,default=None,additive=True):
	# for creating dict containing all key in keys
	return mergeDictss(dict,
			dict.fromkeys(keys,default),
			additive=additive
		)
