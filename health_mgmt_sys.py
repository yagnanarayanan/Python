# Health Management System
# 3 clients - Yagna, Rohan and Hammad

def getdate():
    import datetime
    return datetime.datetime.now()


# Total 6 files (food and exercise)
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

def get_data(file_name_1):
    fp = open(file_name_1, 'rt')
    content = fp.read()
    print("{name_1}'s {choice_1} file data: ".format(name_1=name, choice_1=choice))
    print(content)
    fp.close()


def put_data(file_name_1, log_1):
    fp = open(file_name_1, 'a+')
    fp.write("[" + str(getdate()) + "] " + log_1 + "\n")
    fp.close()


while True:
    name = input("Please enter name ( Yagna, Rohan and Hammad) : ")
    choice = input("Please enter request is for food or exercise : ")
    oper = input("Do you you want to read or append: ")
    log = ''
    if oper == 'append':
        log = input("Please enter the log for " + choice + " : ")
    file_name = "{name_1}_{choice_1}.txt".format(name_1=name, choice_1=choice)
    # make sure to create the empty file with correct name_choice.txt first before running this program
    if oper == "read":
        get_data(file_name)
        c = input("Do you want to continue?: ")
        if c == 'N' or c == 'n':
            break
        else:
            continue
    elif oper == "append":
        put_data(file_name, log)
        d = input("Do you want to continue?: ")
        if d == 'N' or d == 'n':
            break
        else:
            continue
