import aiohttp
import yarl
import json
import os


emojis = {
    'goldcoins': '<:goldcoins:487736737485946880>',
    'youtube'  : '<:youtube:487738563379593218>',

}


def get_emoji(name):
    return emojis[name]


async def get_json(uri, timeout=60):
    print('Requesting JSON ->', yarl.URL(uri))
    async with aiohttp.ClientSession() as session:
        async with session.get(str(yarl.URL(uri)), timeout=timeout) as json_request:
            return json.loads(await json_request.text())


async def get_guild_roster(realm_slug, guild_name):
    async with aiohttp.ClientSession() as session:
        async with session.get(
                f'https://eu.api.blizzard.com/wow/guild/{realm_slug}/{guild_name}?fields=members&locale=en_GB&access_token={os.environ["JB_BNET_TOKEN"]}'
        ) as guild_req:
            guild = json.loads(await guild_req.text())
            if guild_req.status == 404:
                print('Guild not found')
                return 404, 'Not Found'
            # print(guild['members'])
            return guild['members']


def color_pick(score):
    # Raider.io official score-dependant color scheme
    if score >= 6000:
        return 0xe6cc80
    elif score >= 5500:
        return 0xecb960
    elif score >= 5000:
        return 0xf2a640
    elif score >= 4500:
        return 0xf89320
    elif score >= 4000:
        return 0xff8800
    elif score >= 3800:
        return 0xec712f
    elif score >= 3600:
        return 0xda625f
    elif score >= 3400:
        return 0xc7538e
    elif score >= 3200:
        return 0xb544be
    elif score >= 3000:
        return 0xa335ee
    elif score >= 2800:
        return 0x8240ea
    elif score >= 2600:
        return 0x614ce7
    elif score >= 2400:
        return 0x4158e3
    elif score >= 2200:
        return 0x2064e0
    elif score >= 2000:
        return 0x0070dd
    elif score >= 1800:
        return 0x068cb0
    elif score >= 1600:
        return 0x0ca984
    elif score >= 1400:
        return 0x12c558
    elif score >= 1200:
        return 0x18e22c
    elif score >= 1000:
        return 0x1eff00
    elif score >= 900:
        return 0x4bff33
    elif score >= 800:
        return 0x78ff66
    elif score >= 700:
        return 0xa5ff99
    elif score >= 600:
        return 0xd2ffcc
    elif score < 600:
        return 0xffffff
    else:
        return None

