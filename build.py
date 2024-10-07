#! /usr/bin/env python

import os
import shutil
from string import Template

# ssb utils

def read(path):
    file = open(path, 'r')
    content = file.read()

    file.close()

    return content

def render(path, params):
    output = ''

    with open(path, 'r') as f:
        src = Template(f.read())
        result = src.safe_substitute(params)
        output += result
    
    return output

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    file = open(path, 'w')
    
    file.write(content)
    file.close()

def clean_dir(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
        os.makedirs(path)

# page conf

active_link = 'active" aria-current="page'

tenant = dict(
    base_url = '.',
    page_title = 'Accueil',
    page_content = read('templates/index.html'),
    tenant_link = active_link,
)

agenda = dict(
    base_url = '..',
    page_title = 'Agenda',
    page_content = read('templates/agenda/index.html'),
    agenda_link = active_link,
)


agenda_event_free = dict(
    base_url = '../..',
    page_title = 'Bœuf des Lampions',
    page_content = read('templates/agenda/event-free/index.html'),
)

agenda_event = dict(
    base_url = '../..',
    page_title = 'See You In The Pit #13: Sheer Terror / Warrior Kids',
    page_content = read('templates/agenda/event/index.html'),
)

# build

clean_dir('public')

write('public/index.html', render('templates/base.html', tenant))
write('public/agenda/index.html', render('templates/base.html', agenda))
write('public/agenda/boeuf-lampions/index.html', render('templates/base.html', agenda_event_free))
write('public/agenda/see-you-in-the-pit-13/index.html', render('templates/base.html', agenda_event))


shutil.copytree('assets', 'public/assets')
