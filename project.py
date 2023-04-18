import json
from math import *
import time
from pathlib import Path



def create(user_id):

    title = input("Title : ")
    details = input("Details : ")
    total_target = input("Total target : ")
    start_time = input("Start Date (mm/dd/yyyy) : ")
    end_time = input("End Date (mm/dd/yyyy) : ")

    list_data = {'project_user_id': user_id,'title': title, 'details': details , 'total_target': total_target, 'start_time': start_time,
             'end_time': end_time}

    try:
        valid_date1 = time.strptime(start_time, '%m/%d/%Y')
        valid_date2 = time.strptime(end_time, '%m/%d/%Y')

        if valid_date1 and valid_date2:

            mypath = Path(r"C:\Users\amrfa\PycharmProjects\Crowd-Funding-iti/projects_data.json")
            with open('projects_data.json') as json_file:

                if mypath.stat().st_size == 0:
                    projects = open("projects_data.json", "a")
                    json.dump(list_data, projects)
                    projects.write("\n")
                    projects.close()

                # search for poject name if it is already exist or no
                else:
                    list = []
                    for line in json_file:
                        Dict = json.loads(line)
                        list.append(Dict)
                    for dict in list:
                        if title == dict['title'] and dict['project_user_id'] == user_id:
                            print("\nthis project name is already exit ,, please try again")
                            create(user_id)
                    else :
                        projects = open("projects_data.json", "a")
                        json.dump(list_data, projects)
                        projects.write("\n")
                        projects.close()

            print('Your project is created successfully')
        else:
            print("\nYour data is invalid ,, please enter valid data :")
            create(user_id)

    except ValueError:
        print('Invalid date!')
        create(user_id)


def delete(user_id):
    view(user_id)

    project_name = input('\nSelect one projct to delete : ')

    list = []
    json_file = open('projects_data.json')
    for line in json_file:
        Dict = json.loads(line)
        list.append(Dict)

    # search for poject name and remove and update json file
    for dict in list:
        if dict['title'] == project_name:
            list.remove(dict)
            # update in json file
            projects = open("projects_data.json", "w")
            for add_dict in list:
                json.dump(add_dict, projects)
                projects.write("\n")
            projects.close()

            print("\ndelete project successfully")
            break
    else:
        print("this project name is n't exist ,, please try again")
        delete(user_id)


def edit(user_id):
    view(user_id)

    project_name = input('\nSelect one projct to edit : ')

    list = []
    json_file = open('projects_data.json')
    for line in json_file:
        Dict = json.loads(line)
        list.append(Dict)

    # search for poject name
    for dict in list:
        if dict['title'] == project_name:

            print("\nYour project information:")
            print(dict)

            key_name = input('\n\nplease enter the name of key that you want to update in this project : ')

            for key in dict:
                if key == key_name:
                    key_value = input('\n\nplease enter the new value of key : ')
                    dict[key] = key_value

                    # update in json file
                    projects = open("projects_data.json", "w")
                    for add_dict in list:
                        json.dump(add_dict, projects)
                        projects.write("\n")
                    projects.close()

                    print("\nupdate project successfully")
                    break
            else:
                print("invalid key_name ,, please try again :")
                edit(user_id)

    else:
        print("this project name is n't exist ,, please try again")
        edit(user_id)




def search(user_id):
    view(user_id)

    project_date = input('\nWrite project date (mm/dd/yyyy) : ')
    try:
        valid_date = time.strptime(project_date, '%m/%d/%Y')
        if valid_date:
            list = []
            json_file = open('projects_data.json')
            for line in json_file:
                Dict = json.loads(line)
                list.append(Dict)

            # search for poject
            for dict in list:

                if project_date == dict['start_time'] or project_date == dict['end_time']:
                    print("\nYour project information:")
                    print(dict)
                else:
                    print("this project is n't exist ,, please try again")
                    search(user_id)

        else:
            print("\nYour data is invalid ,, please enter valid data :")

    except ValueError:
        print('Invalid date!')



def view(user_id):

    mypath = Path(r"C:\Users\amrfa\PycharmProjects\Crowd-Funding-iti/projects_data.json")
    with open('projects_data.json') as json_file:
        if mypath.stat().st_size == 0:
            print("there is no projects")
        else:
            list = []
            json_file = open('projects_data.json')
            for line in json_file:
                Dict = json.loads(line)
                if Dict['project_user_id'] == user_id:
                    list.append(Dict)

            if len(list) == 0:
                print("no project for you ")
                menu(user_id)
            else:
                print("your projects :")
                for dict in list:
                    print(dict['title'])





def menu(user_id):
    print(
        "\n\n 1) Create Project \n 2) View All Projects \n 3) Edit Project \n 4) Delete Project \n 5) Search For Project")

    choise = input("\nPlease choose from menu :\n")
    if choise == "1":
        create(user_id)

    elif choise == "2":
        view(user_id)

    elif choise == "3":
        edit(user_id)

    elif choise == "4":
        delete(user_id)

    elif choise == "5":
        search(user_id)
    else:
        print("\nPlease choose From menu")
    menu(user_id)