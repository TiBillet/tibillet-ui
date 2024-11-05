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
    tpl = Template(read(path))

    return tpl.safe_substitute(params)

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

subscribe = dict(
    base_url = '../..',
    page_title = 'Adhérer au réseau',
    page_content = read('templates/subscribe/index.html'),
    subscribe_link = active_link,
)

network = dict(
    base_url = '..',
    page_title = 'Réseau local',
    page_content = render('templates/network/index.html', dict(
        chantefrein = read('templates/part/chantefrein.html'),
        bonnie_market = read('templates/part/bonnie-market.html'),
        danzavec = read('templates/part/danzavec.html'),
        sel_de_la_vie = read('templates/part/sel-de-la-vie.html'),
        tiers_lustre = read('templates/part/tiers-lustre.html'),
        philosoniques = read('templates/part/philosoniques.html'),
        sand_witch = read('templates/part/sand-witch.html'),
    )),
    network_link = active_link,
)

register = dict(
    base_url = '..',
    page_title = 'Associer ma carte',
)

def render_account(params):
    account_page = render('templates/account/base.html', params)

    params['page_content'] = account_page

    return render('templates/base.html', params)

piggybank = dict(
    base_url = '..',
    page_title = 'Tirelire',
    page_content = read('templates/account/index.html'),
    piggybank_link = active_link,
)

subscriptions = dict(
    base_url = '../..',
    page_title = 'Adhésions',
    page_content = read('templates/account/subscriptions/index.html'),
    subscriptions_link = active_link,
)

punchclock = dict(
    base_url = '../..',
    page_title = 'Badgeuse',
    page_content = read('templates/account/punchclock/index.html'),
    punchclock_link = active_link,
)

card = dict(
    base_url = '../..',
    page_title = 'Carte',
    page_content = read('templates/account/card/index.html'),
    card_link = active_link,
)

settings = dict(
    base_url = '../..',
    page_title = 'Préférences',
    page_content = read('templates/account/settings/index.html'),
    settings_link = active_link,
)

# build

clean_dir('public')

write('public/index.html', render('templates/base.html', tenant))
write('public/agenda/index.html', render('templates/base.html', agenda))
write('public/agenda/boeuf-lampions/index.html', render('templates/base.html', agenda_event_free))
write('public/agenda/see-you-in-the-pit-13/index.html', render('templates/base.html', agenda_event))
write('public/adherer/index.html', render('templates/base.html', subscribe))
write('public/reseau/index.html', render('templates/base.html', network))
write('public/inscription/index.html', render('templates/register/index.html', register))
write('public/compte/index.html', render_account(piggybank))
write('public/compte/adhesions/index.html', render_account(subscriptions))
write('public/compte/badgeuse/index.html', render_account(punchclock))
write('public/compte/carte/index.html', render_account(card))
write('public/compte/preferences/index.html', render_account(settings))

shutil.copytree('assets', 'public/assets')
