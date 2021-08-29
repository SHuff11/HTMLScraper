import requests
import sys

webpage = sys.argv[1]

response = requests.get(webpage)
#import pdb;pdb.set_trace()
print(response.content)
