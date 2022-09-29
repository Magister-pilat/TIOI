""" In this file contains function 'results'"""
def results(facts, rules):
    """
        This function returns new rules!
        Args:
             List of facts and statements
        Returns:
             New rules
        """
    fact = set(facts)
    interim_results = []
    for i in rules:
        for j in i['if']:
            if j == 'or':
                for atr in i['if'][j]:
                    # if a in facts:
                    if atr in fact:
                        # interim_results.append([facts,i['then']])
                        if len(interim_results) == 0:
                            interim_results.append({'if': facts, 'or': i['if'][j],
                                                    'then': i['then']})
                            break
                        else:
                            put = True
                            for mer in interim_results:
                                if 'or' in mer:
                                    if (mer['or'] == i['if'][j] and mer['then'] != i['then']) or (
                                            mer['or'] != i['if'][j] and mer['then'] == i['then']):
                                        put = False
                                        break
                                if 'and' in mer:
                                    if (mer['and'] == i['if'][j]) and (mer['then'] != i['then']):
                                        put = False
                                        break
                            if put is True:
                                interim_results.append({'if': facts, 'or': i['if'][j],
                                                        'then': i['then']})
            if j == 'and':
                count = len(i['if'][j])
                counter = 0
                for atr in i['if'][j]:
                    # if a in facts:
                    if atr in fact:
                        counter = counter + 1
                    else:
                        break
                if counter == count:
                    # interim_results.append([facts,i['then']])
                    if len(interim_results) == 0:
                        interim_results.append({'if': facts, 'and': i['if'][j], 'then': i['then']})
                    else:
                        put = True
                        for mer in interim_results:
                            if 'and' in mer:
                                if (mer['and'] == i['if'][j] and mer['then'] != i['then']) or (
                                        mer['and'] != i['if'][j] and mer['then'] == i['then']):
                                    put = False
                                    break
                        if put is True:
                            interim_results.append({'if': facts, 'and': i['if'][j],
                                                    'then': i['then']})

            if j == 'not':
                count = len(i['if'][j])
                counter = 0
                for atr in i['if'][j]:
                    # if a not in facts:
                    if atr not in fact:
                        counter = counter + 1
                    else:
                        break
                if counter == count:
                    # interim_results.append([facts,i['then']])
                    if len(interim_results) == 0:
                        interim_results.append({'if': facts, 'not': i['if'][j], 'then': i['then']})
                    else:
                        put = True
                        for mer in interim_results:
                            if 'not' in mer:
                                if (mer['not'] == i['if'][j] and mer['then'] != i['then']) or (
                                        mer['not'] != i['if'][j] and mer['then'] == i['then']):
                                    put = False
                                    break
                        if put is True:
                            interim_results.append({'if': facts, 'not': i['if'][j],
                                                    'then': i['then']})

    return interim_results


