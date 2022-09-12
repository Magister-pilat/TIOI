
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
                 count = len()
                 counter = 0
                       
                          
