user_name = str(input('\n''User_name: '))
print('hi, wellcome to TAKING (C) Chat_Bot')
print('______________________________', '\n')
file_list_txt = []
bin_file_list_txt = []
while True :
    bot_command = str(input('{}@Chat_Bot $ '.format(user_name)))
    if bot_command == 'mk file -txt' :
        mk_txt_file = str(input('{}@Chat_bot /file/ -m Enter File _txt Name $ '.format(user_name)))
        file_list_txt.append(mk_txt_file)
        text = input('{}@Chat_bot /file/ -m Enter text $ \n'.format(user_name))
        file_name = mk_txt_file + '.txt'
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text)
    elif bot_command == 'cat file -txt' :
        file_cat = str(input('{}@Chat_bot /file/ -m Enter File _txt Name $ '.format(user_name))) + '.txt'
        with open(file_cat, 'r', encoding='utf-8') as file:
            content = file.read()
        print(content)
    elif bot_command == 'cat file lst -txt' :
        print(file_list_txt)
    elif bot_command == 'rm file -txt' :
        file_rm = str(input('{}@Chat_bot /file/ -m Enter File _txt Name $ '.format(user_name)))
        file_list_txt.remove(file_rm)
        bin_file_list_txt.append(file_rm)
    elif bot_command == 'bin cat file -txt' :
        file_cat_bin = str(input('{}@Chat_bot /file/ -m Enter File _txt Name $ '.format(user_name))) + '.txt'
        with open(file_cat_bin, 'r', encoding='utf-8') as file:
            content = file.read()
        print(content)
    elif bot_command == 'bin cat file lst -txt' :
        print(bin_file_list_txt)