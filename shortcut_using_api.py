import requests
import csv


api_key = 'test_a5bb737df3b9d6771a0f'

found_valid = False
valid_email = ''


def generate_email(f_name,l_name,domain):
    genereted_emails = []

    global found_valid
    global valid_email


    # generate list of emails
    list_of_gen_patterns=[f_name+'.'+l_name,
                          f_name[0]+'.'+l_name,
                          f_name,
                          f_name+l_name]
    for pattern in list_of_gen_patterns:
            genereted_emails.append(pattern+'@'+domain)

    result_set=[]
    for gen_email in genereted_emails:
        print(gen_email)
        url = 'https://api.emailable.com/v1/verify?email='+gen_email +'&api_key='  +  api_key
        jsonData = requests.get(url).json()
        print(jsonData)
        gen_email=jsonData['email']
        state=jsonData['state']
        print(state)
        if state == 'deliverable':
            found_valid=True
            valid_email=gen_email
            save_to_csv(f_name,l_name,valid_email,domain)
            return '{} is found and Deliverable'.format(gen_email)

        else:
            result_set.append('{} is {}'.format(gen_email,state))


    result_string='    , '.join(result_set)
    return 'No valid emails found, however these are the results:  '+result_string

def save_to_csv(f_name, l_name,valid_email,domain):
    with open("leads.csv", "a") as infile:
        writer = csv.writer(infile)
        line = [f_name, l_name,valid_email,domain]
        writer.writerow(line)


