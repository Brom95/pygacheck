import argparse
import requests
CHECK_URL = 'https://accounts.google.com/_/signin/sl/lookup'


def check_email(email):
    headers = {
        'x-same-domain': '1',
        'origin': 'https://accounts.google.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'google-accounts-xsrf': '1',
        'cookie': 'GAPS=1:5anptsFCcX86o8zx79JaMKbjR6SUSg:i9ZZi85-G8eD7wsC; ',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'accept': '*/*',
        'referer': 'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fhl%3Den%26app%3Ddesktop%26next%3D%252F%26action_handle_signin%3Dtrue&hl=en&service=youtube&passive=true&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin',
        'authority': 'accounts.google.com',
        'dnt': '1'
    }
    data = [
        ('continue', 'https://www.youtube.com/signin?hl=en&app=desktop&next=%2F&action_handle_signin=true'),
        ('service', 'youtube'),
        ('hl', 'en'),
        ('f.req', '["'+email+'","",[],null,"EG",null,null,2,false,true,[null,null,[2,1,null,1,"https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fhl%3Den%26app%3Ddesktop%26next%3D%252F%26action_handle_signin%3Dtrue&hl=en&service=youtube&passive=true&uilel=3",null,[],4,[],"GlifWebSignIn"],1,[null,null,[]],null,null,null,true],"'+email+'"]'),
        ('cookiesDisabled', 'false'),
        ('deviceinfo',
         '[null,null,null,[],null,"EG",null,null,[],"GlifWebSignIn",null,[null,null,[]]]'),
        ('gmscoreversion', 'undefined'),
        ('checkConnection', 'youtube:202:1'),
        ('checkedDomains', 'youtube'), ('pstMsg', '1')]

    r = requests.post(CHECK_URL, data=data, headers=headers)
    # print(r.text)
    if "http" in r.text:
        return True
    return False


def main(args):

    with open(args.input, "r") as i_file:
        for email in i_file:
            email = email.replace("\n", "")
            if check_email(email):
                with open(args.output, "a") as o_file:
                    o_file.write(email+"\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check if gmail account exist.')
    parser.add_argument('-i', "--input", help="Emails for checking", required=True)
    parser.add_argument('-o', "--output", help="File to write checked emails", default="out.txt")
    args = parser.parse_args()
    main(args)
