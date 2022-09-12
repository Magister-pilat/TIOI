
def interim_results(facts, rules):
    interim_results = []
    for i in rules:
         for j in i['if']:
              if j == 'or':
                  for a in facts:
                       if a in i['if'][j]:
                           interim_results.append({facts:i['then']})
                           break
              if j == 'and':
                  count = len(i['if'][j])
                  counter = 0
                  for a in facts:
                       if a in i['if'][j]:     
                           counter = counter +1
                  if counter == count:
                           interim_results.append({facts:i['then']})
              if j == 'not':
                  count = len(i['if'][j])
                  counter = 0
                  for a in facts:
                       if a not in i['if'][j]:     
                           counter = counter +1
                  if counter == count:
                           interim_results.append({facts:i['then']})
              
                  
