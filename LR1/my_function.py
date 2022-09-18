
def interim_results(facts, rules):
    interim_results = []
    for i in rules:
         for j in i['if']:
              if j == 'or':
                  for a in i['if'][j]:
                       if a in facts:
                           interim_results.append({facts:i['then']})
                           break
              if j == 'and':
                  count = len(i['if'][j])
                  counter = 0
                  for a in i['if'][j]:
                       if a in facts:     
                           counter = counter +1
                  if counter == count:
                           interim_results.append({facts:i['then']})
              if j == 'not':
                  count = len(i['if'][j])
                  counter = 0
                  for a in i['if'][j]:
                       if a not in facts:     
                           counter = counter +1
                  if counter == count:
                           interim_results.append({facts:i['then']})
              
    return interim_results      
