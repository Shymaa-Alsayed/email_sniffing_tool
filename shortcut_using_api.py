import csv
import MailboxValidator


api_key = '29ZR5ZE2TB6BJKYO7M8C'
mbv = MailboxValidator.EmailValidation(api_key)

found_valid = False
valid_email = ''


def generate_email(f_name,l_name,domain):
    genereted_emails = []

    global found_valid
    global valid_email


    # generate list of emails
    list_of_gen_patterns=[f_name+'.'+l_name,
                          f_name,
                          f_name[0] + l_name,
                          f_name[0]+'.'+l_name,
                          f_name+l_name]
    for pattern in list_of_gen_patterns:
            genereted_emails.append(pattern+'@'+domain)

    for gen_email in genereted_emails:
        print(gen_email)
        response = mbv.validate_email(gen_email)
        print(response)
        state=response['status']

        if response is None:
            print("Error connecting to API.\n")
        elif response['error_code'] == '':
            if state == 'True':
                found_valid=True
                valid_email=gen_email
                save_to_csv(f_name,l_name,valid_email,domain)
                return '{} is found and Deliverable'.format(gen_email)
        else:
            print('error_code = ' + response['error_code'] + "\n")
            print('error_message = ' + response['error_message'] + "\n")

    return 'No valid email found'

def save_to_csv(f_name, l_name,valid_email,domain):
    with open("leads.csv", "a") as infile:
        writer = csv.writer(infile)
        line = [f_name, l_name,valid_email,domain]
        writer.writerow(line)


