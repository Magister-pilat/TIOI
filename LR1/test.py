from random import choice, shuffle, randint
from time import time

def generate_simple_rules(code_max, n_max, n_generate, log_oper_choice=["and","or","not"]):
	rules = []
	for j in range(0, n_generate):

	    log_oper = choice(log_oper_choice)  #not means and-not (neither)
	    if n_max < 2:
		    n_max = 2
	    n_items = randint(2,n_max)
	    items = []
	    for i in range(0,n_items):
		    items.append( randint(1,code_max) )
	    rule = {
	          'if':{
	              log_oper:	 items         
	           },
	           'then':code_max+j
	        }
	    rules.append(rule)
	shuffle(rules)
	return(rules)

def generate_seq_facts(M):
	facts = list(range(0,M))
	shuffle(facts)
	return facts

def generate_rand_facts(code_max, M):
	facts = []
	for i in range(0,M):
		facts.append( randint(0, code_max) )
	return facts

def results(facts, rules):
    fact = set(facts)
    interim_results = []
    for i in rules:
         for j in i['if']:
              if j == 'or':
                  for a in i['if'][j]:
                       #if a in facts:
                       if a in fact:
                           #interim_results.append([facts,i['then']])
                           if len(interim_results) == 0:
                           		interim_results.append({'if': facts, 'or': i['if'][j], 'then': i['then']})
                           		break
                           else:
                                	put = True
                                	for m in interim_results:
                                        	if 'or' in m:
                                        		if (m['or'] == i['if'][j] and m['then'] != i['then']) or ( m['or'] != i['if'][j] and m['then'] == i['then']):
                                                		put = False
                                	                	break
                                        	if 'and' in m:
                                                	if (m['and'] == i['if'][j]) and (m['then'] != i['then']):
                                                        	put = False
                                                        	break
                                	if put == True:
                                		interim_results.append({'if': facts, 'or': i['if'][j], 'then': i['then']})
              if j == 'and':
                  count = len(i['if'][j])
                  counter = 0
                  for a in i['if'][j]:
                       #if a in facts:
                       if a in fact:     
                           counter = counter +1
                       else:
                           break
                  if counter == count:
                           #interim_results.append([facts,i['then']])
                           if len(interim_results) == 0:
                           	interim_results.append({'if': facts, 'and': i['if'][j], 'then': i['then']})
                           else:
                                put = True
                                for m in interim_results:
                                        if 'and' in m:
                                                if (m['and'] == i['if'][j] and m['then'] != i['then']) or ( m['and'] != i['if'][j] and m['then'] == i['then']):
                                                	put = False
                                	                break
                                if put == True:
                                	interim_results.append({'if': facts, 'and': i['if'][j], 'then': i['then']})
                                          
              if j == 'not':
                  count = len(i['if'][j])
                  counter = 0
                  for a in i['if'][j]:
                       #if a not in facts:
                       if a not in fact:     
                           counter = counter +1
                       else:
                           break
                  if counter == count:
                           #interim_results.append([facts,i['then']])
                           if len(interim_results) == 0:
                                 interim_results.append({'if': facts, 'not': i['if'][j], 'then': i['then']})
                           else:
                                 put = True
                                 for m in interim_results:
                                         if 'not' in m:
                                                if (m['not'] == i['if'][j] and m['then'] != i['then']) or ( m['not'] != i['if'][j] and m['then'] == i['then']):
                                                	put = False
                                	                break
                                 if put == True:
                                          interim_results.append({'if': facts, 'not': i['if'][j], 'then': i['then']}) 
              
    return interim_results 

time_start = time()
N = 100000
M = 1000
rules = generate_simple_rules(100, 4, N)
facts = generate_rand_facts(100, M)
print("%d rules generated in %f seconds" % (N,time()-time_start))

time_start = time()

results(facts, rules)
rez = time()-time_start
print("%d facts validated vs %d rules in %f seconds" % (M,N,rez))
