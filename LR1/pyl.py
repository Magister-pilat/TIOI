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
                            fac = facts.copy()
                            interim_results.append({'if': fac, 'or': i['if'][j],
                                                    'then': i['then']})
                            facts.append(i['then'])
                            fact.add(i['then'])
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
                                fac = facts.copy()
                                interim_results.append({'if': fac, 'or': i['if'][j],
                                                        'then': i['then']})
                                facts.append(i['then'])
                                fact.add(i['then'])
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
                        fac = facts.copy()
                        interim_results.append({'if': fac, 'and': i['if'][j], 'then': i['then']})
                        facts.append(i['then'])
                        fact.add(i['then'])
                    else:
                        put = True
                        for mer in interim_results:
                            if 'and' in mer:
                                if (mer['and'] == i['if'][j] and mer['then'] != i['then']) or (
                                        mer['and'] != i['if'][j] and mer['then'] == i['then']):
                                    put = False
                                    break
                        if put is True:
                            fac = facts.copy()
                            interim_results.append({'if': fac, 'and': i['if'][j],
                                                    'then': i['then']})
                            facts.append(i['then'])
                            fact.add(i['then'])

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
                        fac = facts.copy()
                        interim_results.append({'if': fac, 'not': i['if'][j], 'then': i['then']})
                        facts.append(i['then'])
                        fact.add(i['then'])
                    else:
                        put = True
                        for mer in interim_results:
                            if 'not' in mer:
                                if (mer['not'] == i['if'][j] and mer['then'] != i['then']) or (
                                        mer['not'] != i['if'][j] and mer['then'] == i['then']):
                                    put = False
                                    break
                        if put is True:
                            fac = facts.copy()
                            interim_results.append({'if': fac, 'not': i['if'][j], 'then': i['then']})
                            facts.append(i['then'])
                            fact.add(i['then'])

    return interim_results

