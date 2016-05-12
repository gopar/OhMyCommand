import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

import django
django.setup()

from django.contrib.auth import get_user_model

from apps.commands.models import Command

User = get_user_model()


def populate():
    user = add_user('daniel', 'gopar', 'goparman',
                    'gopar@gopar.com', 'password')
    add_command('ls', user, 'L', '1.0',
                'List all given directory contents')
    add_command('git', user)

    user = add_user('joey', 'gopar', 'joey',
                    'joey@joey.com', 'password')
    add_command('tree', user, 'L', '1.0',
                'List all directories in a tree structure')
    add_command('rm -rf', user, 'L', note='Deletes everything \o/')
    add_command('ls -alh', user, 'L', note='LISTS ALL THINGS')


def add_user(first_name, last_name, username, email, password):
    user = User.objects.get_or_create(
        first_name=first_name, last_name=last_name,
        username=username, email=email)[0]
    user.set_password(password)
    user.save()
    return user


def add_command(command, user, os='', version='', note=''):
    command = Command.objects.get_or_create(
        command=command, os=os, version=version,
        note=note, user=user)[0]
    command.save()
    return command


def print_db():
    """
    Print what we have
    """
    for user in User.objects.all():
        for command in user.command_set.all():
            print("User: {} -- Command: {}".format(user, command))


if __name__ == '__main__':
    print("Starting to populate DB...\n")
    populate()
    print_db()
