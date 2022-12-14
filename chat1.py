import os
import requests
from json import dumps
from httplib2 import Http
from jinja2 import Template
from sys import stdout, stderr

def main():
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    additional_variable=os.environ
    Body=additional_variable.pop('BODY')
    url=additional_variable.pop('GCHAT_URL')
    print(url)
    template=Template(Body)
    Body=template.render(additional_variable)
    print(Body)
    bot_message=(Body)
    print(bot_message)
    try:
        response = requests.post(url, headers=headers, data=bot_message)
        print(response.content)
        if response.status_code == 200:
            print("G-Chat notification send successfully",file=stdout)
            exit(0) 
        elif response.status_code == 403:
            print("URL has {response.content}",file=stderr)
            print("Unable to send G-Chat notification",file=stderr)
            exit(1)
        elif response.status_code == 400:
            print("request body has {response.content}",file=stderr)
            print("Unable to send G-Chat notification",file=stderr)
            exit(1)
        else:
            print("Unable to send G-Chat notification",file=stderr)
            exit(1)
    except Exception as e:
        print(e,file=stderr)
        exit(1)
if __name__ == '__main__':
    main()
