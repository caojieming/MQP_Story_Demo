# BCI Game MQP
# James Cao, Andrew Ngyuen, Jagger Polvino

from operator import itemgetter
import pandas as pd
import time

# In order to run this file, you will need to install pandas and openpyxl. To do so, enter into your terminal:
# pip install pandas
# pip install openpyxl

def print_in(str):
    print(str)
    input()


def choice_2_loop():
    inp = ""
    inp = input()
    while inp != "1" and inp != "2":
        print("Invalid input, please try again.")
        inp = input()
    print()
    return inp

def choice_3_loop():
    inp = ""
    inp = input()
    while inp != "1" and inp != "2" and inp != "3":
        print("Invalid input, please try again.")
        inp = input()
    print()
    return inp

def excel_to_array():
    df = pd.read_excel('story_script.xlsx')
    return df.values

def read_script(script):
    pass_rows = 0
    for row in script:
        if pass_rows > 0:
            pass_rows -= 1
            continue
        match row[0]:
            case 'start_story':
                # mainly cosmetic, ignore row and continue
                continue
            case 'end_story':
                # end, break loop
                break
            case 'comment':
                # ignore row and continue
                continue
            case 'dialogue':
                print_in(row[1])
                continue
            case 'choice_2':
                print(row[1])
                print(row[2])
                choice = choice_2_loop()
                continue
            case 'choice_3':
                print(row[1])
                print(row[2])
                print(row[3])
                choice = choice_3_loop()
                continue
            case 'state_choice_3':
                match state:
                    case '1':
                        print(row[1])
                        print(row[2])
                        print(row[3])
                    case '2':
                        print(row[4])
                        print(row[5])
                        print(row[6])
                choice = choice_3_loop()
                continue
            case 'path_2':
                match choice:
                    case '1':
                        if row[1] != 'skip': print_in(row[1])
                    case '2':
                        if row[2] != 'skip': print_in(row[2])
                continue
            case 'path_3':
                match choice:
                    case '1':
                        if row[1] != 'skip': print_in(row[1])
                    case '2':
                        if row[2] != 'skip': print_in(row[2])
                    case '3':
                        if row[3] != 'skip': print_in(row[3])
                continue
            case 'state':
                print("Are you focused right now? (1 = yes, 2 = no)")
                state = choice_2_loop()
                continue
            case 'state_dialogue':
                match state:
                    case '1':
                        if row[1] != 'skip': print_in(row[1])
                    case '2':
                        if row[2] != 'skip': print_in(row[2])
                continue
            case 'state_path_2':
                match state:
                    case '1':
                        match choice:
                            case '1':
                                if row[1] != 'skip': print_in(row[1])
                            case '2':
                                if row[2] != 'skip': print_in(row[2])
                    case '2':
                        match choice:
                            case '1':
                                if row[3] != 'skip': print_in(row[4])
                            case '2':
                                if row[3] != 'skip': print_in(row[4])
                continue
            case 'state_path_3':
                match state:
                    case '1':
                        match choice:
                            case '1':
                                check_pass = row[1].split(' ')
                                if check_pass[0] == 'pass':
                                    pass_rows = int(check_pass[1])
                                elif row[1] != 'skip':
                                    print_in(row[1])
                            case '2':
                                check_pass = row[2].split(' ')
                                if check_pass[0] == 'pass':
                                    pass_rows = int(check_pass[1])
                                elif row[2] != 'skip':
                                    print_in(row[2])
                            case '3':
                                check_pass = row[3].split(' ')
                                if check_pass[0] == 'pass':
                                    pass_rows = int(check_pass[1])
                                elif row[3] != 'skip':
                                    print_in(row[3])
                    case '2':
                        match choice:
                            case '1':
                                check_pass = row[4].split(' ')
                                if check_pass[0] == 'pass':
                                    pass_rows = int(check_pass[1])
                                elif row[4] != 'skip':
                                    print_in(row[4])
                            case '2':
                                check_pass = row[5].split(' ')
                                if check_pass[0] == 'pass':
                                    pass_rows = int(check_pass[1])
                                elif row[5] != 'skip':
                                    print_in(row[5])
                            case '3':
                                check_pass = row[6].split(' ')
                                if check_pass[0] == 'pass':
                                    pass_rows = int(check_pass[1])
                                elif row[6] != 'skip':
                                    print_in(row[6])
                continue
            case 'wait':
                time.sleep(5)
                proceed = 0
                while True:
                    # optional dialogue
                    if row[1] != 'skip': print(row[1])

                    # player responses
                    print(row[2])
                    print(row[3])
                    proceed = choice_2_loop()

                    match proceed:
                        case "1":
                            # dialogue response positive, exit loop
                            print_in(row[4])
                            break
                        case "2":
                            # dialogue response negative, loop
                            print(row[5])
                continue
            case 'accuse':
                # look at points, and choose which row[#] to use, current code is temporary
                murderer = [None, Baker, Carpenter, Potter].index(max([Baker, Carpenter, Potter], key = itemgetter(1)))
                choice = str(murderer)
                print(row[murderer])

                # print("James Baker: " + str(Baker[1]))
                # print("Jagger Carpenter: " + str(Carpenter[1]))
                # print("Andrew Potter: " + str(Potter[1]))
                # print()
                continue
            case 'point_change':
                vals = ''
                match state:
                    case '1':
                        match choice:
                            case '1':
                                vals = row[1]
                            case '2':
                                vals = row[2]
                            case '3':
                                vals = row[3]
                    case '2':
                        match choice:
                            case '1':
                                vals = row[4]
                            case '2':
                                vals = row[5]
                            case '3':
                                vals = row[6]

                try:
                    vals = vals.split(',')
                except Exception:
                    continue

                vals = [val.strip() for val in vals]
                vals = [duo.split(' ') for duo in vals]

                for val in vals:
                    name = val[0]
                    points = val[1]
                    match name:
                        case 'Baker':
                            Baker[1] += int(points)
                            continue
                        case 'Carpenter':
                            Carpenter[1] += int(points)
                            continue
                        case 'Potter':
                            Potter[1] += int(points)
                            continue
                continue




state = ""
choice = ""
Baker = ["Baker", 0]
Carpenter = ["Carpenter", 0]
Potter = ["Potter", 0]

def main():
    ok = ""
    print("All characters in the game are fictional, any and all resemblances to real people are coincidental.")
    print("Warning: there are minor descriptions of violence, blood, murder, and occultism, if you do not feel comfortable with these topics, please stop playing this game.")
    print("Continue, knowing these warnings? (1 for yes, 2 for no)")
    ok = choice_2_loop()
    match ok:
        case "2":
            exit()

    script = excel_to_array()
    read_script(script)





if __name__ == "__main__":
    main()
