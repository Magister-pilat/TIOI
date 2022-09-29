from random import choice, shuffle, randint
from time import time


def results(facts, rules):
    fact = set(facts)
    interim_results = []
    for i in rules:
        for j in i['if']:
            if j == 'or':
                for a in i['if'][j]:
                    # if a in facts:
                    if a in fact:
                        # interim_results.append([facts,i['then']])
                        if len(interim_results) == 0:
                            interim_results.append({'if': facts, 'or': i['if'][j], 'then': i['then']})
                            break
                        else:
                            put = True
                            for m in interim_results:
                                if 'or' in m:
                                    if (m['or'] == i['if'][j] and m['then'] != i['then']) or (
                                            m['or'] != i['if'][j] and m['then'] == i['then']):
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
                    # if a in facts:
                    if a in fact:
                        counter = counter + 1
                    else:
                        break
                if counter == count:
                    # interim_results.append([facts,i['then']])
                    if len(interim_results) == 0:
                        interim_results.append({'if': facts, 'and': i['if'][j], 'then': i['then']})
                    else:
                        put = True
                        for m in interim_results:
                            if 'and' in m:
                                if (m['and'] == i['if'][j] and m['then'] != i['then']) or (
                                        m['and'] != i['if'][j] and m['then'] == i['then']):
                                    put = False
                                    break
                        if put == True:
                            interim_results.append({'if': facts, 'and': i['if'][j], 'then': i['then']})

            if j == 'not':
                count = len(i['if'][j])
                counter = 0
                for a in i['if'][j]:
                    # if a not in facts:
                    if a not in fact:
                        counter = counter + 1
                    else:
                        break
                if counter == count:
                    # interim_results.append([facts,i['then']])
                    if len(interim_results) == 0:
                        interim_results.append({'if': facts, 'not': i['if'][j], 'then': i['then']})
                    else:
                        put = True
                        for m in interim_results:
                            if 'not' in m:
                                if (m['not'] == i['if'][j] and m['then'] != i['then']) or (
                                        m['not'] != i['if'][j] and m['then'] == i['then']):
                                    put = False
                                    break
                        if put == True:
                            interim_results.append({'if': facts, 'not': i['if'][j], 'then': i['then']})

    return interim_results


