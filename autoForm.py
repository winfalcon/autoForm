import re
import time
import random
import numpy as np
import requests as rq

url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSfWbrd7T48GCACXZalCQYd0LbosMgSPrZH3pCAM_c5TVtLqSA/formResponse'

payload = {
    'entry.768626287' : 'TTT',
    'entry.2087321308' : 'TTT',
    'entry.966403824' : 'Option 3',
    'entry.1549659975' : 'Option 2',
    'entry.1955332482' : 'Option 2',
    'entry.529456087' : 'Option 1',   
    'fvv' : '0',
    'draftResponse' : '[]',
    'pageHistory' : '0',
    'fbzx' : '-1517347112612956814'
}

num = 10  # number of executions
period = np.arange(0.5, 5.0, 0.1)
delay = 0  # delay of execution
#while num > 0:
#    try:
    #    payload['entry.1216123536'] = random.choice(params)  # random choice
res = rq.post(url, data=payload)
res.raise_for_status()
if res.status_code == 200:
    print('already send form date')

   #         delay = round(random.choice(period), 2)  # round off to the 2nd decimal place
          #  print('Fill Out : ' + payload['entry.1216123536'] + ' delay : ' + str(delay) + ' sec')
    #        time.sleep(delay)
 #   except rq.HTTPError:
  #      print('HTTP Error!')
    
  #  num -= 1