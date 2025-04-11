import time
import pickle
over=False
file_name='data.txt'


def welcome():
    print(' 📝 Task Manager 📝 '.center(100,'='))
    print('1. View Task 📰⬅ \n2. Add Task 📌\n3. Delete Task ❌\n4. Completee Task ✅\n5.Exit ✋🏻\n ')

def addTask():
    # global tasks
    tasks=getData()
    f=open(file_name,"wb")
    text=input('Enter task: ')
    tasks.append({'title':text,"done":False})
    saveData(tasks)
    print('Task Added Succesfully',end="")
    for _ in range(3):
        time.sleep(0.5)
        print('.',end="",flush=True)
    print()
    f.close()

def saveData(task):
    with open(file_name,'wb') as f:
        pickle.dump(task,f)

def getData():
    try:
        with open(file_name,'rb') as f:
            return pickle.load(f)
    except:
        with open(file_name,'wb')as f:
            return []
        
def showTask():
    # global tasks
    tasks=getData()
    c=0
    print('-'.center(100,'-'))
    print('Index\tStatus\t\tTask')
    print('-'.center(100,'-'))
    if(tasks==[]):
        print('No Task Found')
    else:
        for a,b in tasks:
            status=' ✅ ' if tasks[c][b] ==True else " ❌ "
            print(f'  {c+1}\t{status}\t\t{tasks[c][a]}')
            # print(tasks[c][a],tasks[c][b])
            c+=1
        print()

def deleteTask():
    tasks=getData()
    l=len(tasks)
    try:
        d=int(input('Enter Task no to Delete: '))
        temp=tasks[d-1]['done']
        if(temp!=True):
            ch=input('This task doesnt seem to completed do you wanna proceed still (yes/no).')
            if(ch.lower().strip()=='no'):
                print(f'Delete task {tasks[d-1]['title']} canceled')
                return
        data=tasks.pop(d-1)
        status=' ✅ ' if data['done']==True else " ❌ "
        print('Task ',data['title'],'status is ',status)
        print('Task Succesfully Deleted',end='')
        for _ in range(3):
            time.sleep(0.5)
            print('.',end="",flush=True)
        print()
    except IndexError:
        print('item no not in list')
    except ValueError:
        print('Enter integer value')
    finally:
        saveData(tasks)

def completeTask():
    tasks=getData()
    try:
        c=int(input('Enter Task No to Complete '))
        temp=tasks[c-1]
        tasks[c-1]['done']=True
        print('Task Succesfully Completed',end='')
        for _ in range(3):
            time.sleep(0.5)
            print('.',end="",flush=True)
        print()
    except IndexError:
        print('Index not in List')
    except ValueError:
        print('Enter integer value')
    finally:
        saveData(tasks)
def main():
    global tasks
    global over
    while(not over):
        welcome()
        try:
            t1=int(input('Enter Choice No: '))
            if(t1<1 or t1>5):
                print('Provide No between 1-5 ')
                continue
        except ValueError:
            print('Add integer value')
            continue
        if(t1==5):
            print('Goodbye ✋')
            over=True
            # break
        elif(t1==1):
            showTask()
        elif(t1==2):
            addTask()
        elif(t1==3):
            deleteTask()
        elif(t1==4):
            completeTask()

tasks=getData()
main()