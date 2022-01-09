import os
import platform
import sys
import pkg_resources

def editsettings(project, app):
    app = "'" + app + "'"
    file = project + '/settings.py'
    reading_file = open(file, "r")

    new_file_content = ""
    to_replace = "'django.contrib.staticfiles',"
    app = "'django.contrib.staticfiles', \n" + app 
    for line in reading_file:
          stripped_line = line.strip()
          new_line = stripped_line.replace(to_replace, app)
          new_file_content += new_line +"\n"
    reading_file.close()

    writing_file = open(file, "w")
    writing_file.write(new_file_content)

    writing_file.close()   

print('This Program only Supports Powershell or Termial available in windows 10, 11 and linux respectively.')
print('If you are using Windows 10 you might not able to find powershell So for using this program follow the below given steps: ')
print('Press Windows+R to open the Run dialog box, and then type “powershell” in the text box. You can either click “OK” and navigate your powershell to this file location')
print('--- Launch ---')
yon = input('Start Program by typing yes: ')

if yon == 'yes':
    print('--- Installing Requirements ---')
    os.system('python3 -m pip install --upgrade pip && pip install  virtualenv')
    path = input('Where you want to Create Your Django project Enter Full Path: ')
    os.chdir(path)
    print('\n --- Your Env Name would be decided by this program using your project name ---')
    project_name = input('Enter Project Name: ')
    env_name = project_name + '_env'

    osys = platform.system()
    if osys == 'Windows':
        os.system('python -m virtualenv {env_name}'.format(env_name=env_name))
        print("\033[1;33;40m Warning: You Might Have ExecutionPolicy \n For That Run Windows Powershell as Administrator and then type command: 'Set-ExecutionPolicy RemoteSigned' and Type Y in capital \n")
        done = input('If Done Type yes or enter: ')
        print('\033[1;37;40m Policy Accepted Done \n')
        env_created = env_name + '/Script/S'
    if osys == 'Linux':
        os.system('virtualenv {env_name}'.format(env_name=env_name))
        env_created = env_name + '/bin/S'
    env = str(os.path.dirname(env_created)).format(env_name=env_name) + '/activate_this.py'
    with open(env) as f:
        code = compile(f.read(), env, 'exec')
        exec(code, dict(__file__=env))
    os.system('pip3 install Django')
    os.system('django-admin startproject '+project_name)
    os.chdir('{project}'.format(project=project_name))
    print('\033[1;32;40m --- Project has been created ---')
    app_name = input('\033[1;37;40m Enter App Name: ')
    os.system('django-admin startapp '+ app_name)
    editsettings(project_name, app_name)
    os.system('python3 manage.py makemigrations')
    os.system('python3 manage.py migrate')

    print('\033[1;32;40m \n This Program Created/Done: \n ENV {env} \n Installed Requirements \n Project: {project} \n App: {app} \n Added app name in settings.py \n And Created Migrations \n Thanks For Using This Program Created By \n Proud Wadhwa'.format(env=env_name, project=project_name, app=app_name))
    
