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
    make_dirs(path)

    file = open(path, 'w')
    
    file.write(content)
    file.close()

def clean_dir(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
        os.makedirs(path)

def make_dirs(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

# page conf

active_link = 'active" aria-current="page'

agenda = dict(
    base_url = '..',
    page_title = 'Agenda',
    page_content = read('templates/agenda/index.html'),
    agenda_link_class = active_link,
)

# build

clean_dir('public')

write('public/agenda/index.html', render('templates/base.html', agenda))

shutil.copytree('assets', 'public/assets')
