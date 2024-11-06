import json


def print_file_contents():
    f = open('example.json', 'r')
    contents = f.read()
    print(contents)


def print_file_contents_with_with():
    with open('example.json', 'r') as f:
        contents = f.read()
        print(contents)


def parse_json_file(file_name):
    with open(file_name, 'r') as f:
        users_with_notif_on_list = []
        config_dict = json.load(f)

        for user_dict in config_dict['users']:
            is_email_notif = user_dict['preferences']['notifications']['email']
            if is_email_notif:
                print(user_dict['username'], ' has notifications ON!')
                users_with_notif_on_list.append(user_dict)

        # We have the list of users with notification ON, so that we can process it later.
        print(
            'Users with notification on are ',
            len(users_with_notif_on_list),
            ' out of ',
            len(config_dict['users'])
        )


parse_json_file('example.json')
