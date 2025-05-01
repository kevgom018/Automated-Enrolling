import pexpect, json

def main():
    creds = {}
    with open('credentials.json', 'r') as file:
        creds = json.load(file)
    print(creds['pin'])

if __name__ == '__main__':
    main()