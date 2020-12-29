import pymysql
import hashlib
import TrinityPyAuth

def table_exists(table_name):
    cur.execute("USE %s" % (auth_db))
    try:
        cur.execute("SELECT 1 FROM " + table_name + " LIMIT 1;")
    except pymysql.err.ProgrammingError: 
        return False
    return True

def user_exists(username):
    
    if not table_exists("account"): # just in case
        raise RuntimeError("Accounts table doesn't exist!")
    cur.execute("SELECT * FROM account WHERE username = '" + username + "'")
    return cur.fetchone() != None

def get_player_health(name):
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * FROM characters WHERE name = '" + name + "'")
    return cur.fetchone()['health']

def get_player_money(name):
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * FROM characters WHERE name = '" + name + "'")
    return cur.fetchone()['money']

def get_player_xp(name):
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * FROM characters WHERE name = '" + name + "'")
    return cur.fetchone()['xp']

def get_player_total_kills(name):
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * FROM characters WHERE name = '" + name + "'")
    return cur.fetchone()['totalKills']

def get_player_today_kills(name):
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * FROM characters WHERE name = '" + name + "'")
    return cur.fetchone()['todayKills']

def get_player_total_playtime(name):
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * FROM characters WHERE name = '" + name + "'")
    return cur.fetchone()['totaltime']

def get_player_ping(name):
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * FROM characters WHERE name = '" + name + "'")
    return cur.fetchone()['latency']

def get_player_level(name):
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * FROM characters WHERE name = '" + name + "'")
    return cur.fetchone()['level']

"""
Get the player's race ID.

1 = Human
2 = Orc
3 = Dwarf
4 = Night Elf
5 = Undead
6 = Tauren
7 = Gnome
8 = Troll
9 = Goblin
10 = Blood Elf
11 = Draenei
12 = Fel Orc
13 = Naga
14 = Broken
15 = Skeleton
16 = Vrykul
17 = Tuskarr
18 = Forest Troll
19 = Taunka
20 = Northrend Skeleton
21 = Ice Troll
"""
def get_player_race_id(name):
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * FROM characters WHERE name = '" + name + "'")
    return cur.fetchone()['race']

def get_player_race_name(name):
    id = get_player_race_id(name)
    if id == 1:
        return "Human"
    elif id == 2:
        return "Orc"
    elif id == 3:
        return "Dwarf"
    elif id == 4:
        return "Night Elf"
    elif id == 5:
        return "Undead"
    elif id == 6:
        return "Tauren"
    elif id == 7:
        return "Gnome"
    elif id == 8:
        return "Troll"
    elif id == 9:
        return "Goblin"
    elif id == 10:
        return "Blood Elf"
    elif id == 11:
        return "Draenei"
    elif id == 12:
        return "Fel Orc"
    elif id == 13:
        return "Naga"
    elif id == 14:
        return "Broken"
    elif id == 15:
        return "Skeleton"
    elif id == 16:
        return "Vrykul"
    elif id == 17:
        return "Tuskarr"
    elif id == 18:
        return "Forest Troll"
    elif id == 19:
        return "Taunka"
    elif id == 20:
        return "Northrend Skeleton"
    elif id == 21:
        return "Ice Troll"
    else: 
            return "Unknown"
"""
Get the player's class ID.
1 = Warrior
2 = Paladin
3 = Hunter
4 = Rogue
5 = Priest
6 = Death Knight
7 = Shaman
8 = Mage
9 = Warlock
10 = Monk
11 = Druid
"""
def get_player_class_id(name):
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * FROM characters WHERE name = '" + name + "'")
    return cur.fetchone()['class']

def get_player_class_name(name):
    id = get_player_class_id(name)
    if id == 1:
        return "Warrior"
    elif id == 2:
        return "Paladin"
    elif id == 3:
        return "Hunter"
    elif id == 4:
        return "Rogue"
    elif id == 5:
        return "Priest"
    elif id == 6:
        return "Death Knight"
    elif id == 7:
        return "Shaman"
    elif id == 8:
        return "Mage"
    elif id == 9:
        return "Warlock"
    elif id == 10:
        return "Monk"
    elif id == 11:
        return "Druid"

def get_player_honor_points(name):
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * FROM characters WHERE name = '" + name + "'")
    return cur.fetchone()['totalHonorPoints']

def raw_get_all_character_info(name):
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * FROM characters WHERE name = '" + name + "'")
    return cur.fetchall()

def is_player_online(name):
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * FROM characters WHERE name = '" + name + "'")
    o = cur.fetchone()['online']
    return o == 1

def get_online_players_count():
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * from characters WHERE online = 1;")
    count = cur.rowcount
    return count

def set_player_money(username, money):
    cur.execute("USE %s" % (characters_db))
    query = "UPDATE characters SET money = %s WHERE name = %s"
    cur.execute(query, (money, username,))

def set_player_level(username, level):
    cur.execute("USE %s" % (characters_db))
    query = "UPDATE characters SET level = %s WHERE name = %s"
    cur.execute(query, (level, username,))

def set_player_health(username, health):
    cur.execute("USE %s" % (characters_db))
    query = "UPDATE characters SET health = %s WHERE name = %s"
    cur.execute(query, (health, username,))

def get_salt(username):
    cur.execute("USE %s" % (auth_db))
    cur.execute("SELECT * FROM account WHERE username = '" + username + "'")
    return cur.fetchone()['salt']

def get_verifier(username):
    cur.execute("USE %s" % (auth_db))
    cur.execute("SELECT * FROM account WHERE username = '" + username + "'")
    return cur.fetchone()['verifier']

def update_salt(username, new_salt):
    cur.execute("USE %s" % (auth_db))
    query = "UPDATE account SET salt = %s WHERE username = %s"
    cur.execute(query, (new_salt, username,))

def update_verifier(username, new_verifier):
    cur.execute("USE %s" % (auth_db))
    query = "UPDATE account SET verifier = %s WHERE username = %s"
    cur.execute(query, (new_verifier, username,))

def add_account_to_db(username, password, email, verifier, salt):
    cur.execute("USE %s" % (auth_db))
    # Create with dummy salt and verifier salt first, then update
    cur.execute("INSERT INTO account (username, salt, verifier, email)"
                       " VALUES ('" + username + "',"
                       "'0x0', '0x0', '" + email + "')")
    update_salt(username, salt)
    update_verifier(username, verifier)

def get_account_id_by_name(account_name):
    cur.execute("USE %s" % (auth_db))
    cur.execute("SELECT * FROM account WHERE username = '" + account_name + "'")
    return cur.fetchone()['id']

def get_guid_by_player_name(name):
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * FROM characters WHERE name = '" + name + "'")
    return cur.fetchone()['guid']

def get_login_flags_by_player_name(name):
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * FROM characters WHERE name = '" + name + "'")
    return cur.fetchone()['at_login']

"""
Revive the character the next time he/she logs in.
TrinityCore6.x/src/server/game/Entities/Player/Player.h

Other flags for more functions below:
enum AtLoginFlags
{
	AT_LOGIN_NONE              = 0x000,
	AT_LOGIN_RENAME            = 0x001,
    AT_LOGIN_RESET_SPELLS      = 0x002,
    AT_LOGIN_RESET_TALENTS     = 0x004,
	AT_LOGIN_CUSTOMIZE         = 0x008,
    AT_LOGIN_RESET_PET_TALENTS = 0x010,
	AT_LOGIN_FIRST             = 0x020,
	AT_LOGIN_CHANGE_FACTION    = 0x040,
	AT_LOGIN_CHANGE_RACE       = 0x080,
	AT_LOGIN_RESURRECT         = 0x100,
};
"""
def revive_character_next_login(name):
    query = "UPDATE characters SET at_login = %s WHERE name = %s"
    cur.execute(query, (0x100 | get_login_flags_by_player_name(name), name,))
    set_player_health(name, 10)
    
def rename_character_next_login(name):
    query = "UPDATE characters SET at_login = %s WHERE name = %s"
    cur.execute(query, (0x100 | get_login_flags_by_player_name(name), name,))

def customize_character_next_login(name):
    query = "UPDATE characters SET at_login = %s WHERE name = %s"
    cur.execute(query, (0x008 | get_login_flags_by_player_name(name), name,))

def change_race_next_login(name):
    query = "UPDATE characters SET at_login = %s WHERE name = %s"
    cur.execute(query, (0x008 | get_login_flags_by_player_name(name), name,))

"""
Get top characters by money
@return List object containing a tuple: (character name, money)
"""
def get_top_characters_by_money(account_name):
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * FROM characters ORDER BY money DESC")
    chars = cur.fetchall()
    chars_list = []
    for row in chars:
        chars_list.append((row["name"], row["money"]))
    return chars_list

"""
Get top characters by money
@return List object containing a tuple: (character name, money)
"""
def get_top_characters_by_total_kills(account_name):
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * FROM characters ORDER BY totalkills DESC")
    chars = cur.fetchall()
    chars_list = []
    for row in chars:
        chars_list.append((row["name"], row["totalKills"]))
    return chars_list

"""
Get top characters by total time spent in the world, in seconds
@return List object containing a tuple: (character name, money)
"""
def get_top_characters_by_total_time(account_name):
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * FROM characters ORDER BY totaltime DESC")
    chars = cur.fetchall()
    chars_list = []
    for row in chars:
        chars_list.append((row["name"], row["totaltime"]))
    return chars_list

"""
Get top characters by health
@return List object containing a tuple: (character name, health)
"""
def get_top_characters_by_health(account_name):
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * FROM characters ORDER BY health DESC")
    chars = cur.fetchall()
    chars_list = []
    for row in chars:
        chars_list.append((row["name"], row["health"]))
    return chars_list

"""
Get all characters by the name of an account
@return List object with all the character names on the account.
"""
def get_characters_by_account_name(account_name):
    acctid = get_account_id_by_name(account_name)
    cur.execute("USE %s" % (characters_db))
    cur.execute("SELECT * FROM characters WHERE account = '" + str(acctid) + "'")
    chars = cur.fetchall()
    chars_list = []
    for row in chars:
        chars_list.append(row["name"])
    return chars_list

def connect(db_host, db_port, db_user, user_pass, auth_db_name="auth", characters_db_name="characters"):
    try:
        global application_db
        global auth_db
        auth_db = auth_db_name
        global characters_db
        characters_db = characters_db_name
        application_db = pymysql.connect(db_host, 
                                            port=db_port, 
                                            user=db_user,
                                            passwd=user_pass,
                                            db=auth_db_name,
                                            autocommit=True,
                                            cursorclass=pymysql.cursors.DictCursor)

    except pymysql.err.OperationalError as e:
        print(e)
        return

    global cur
    cur = application_db.cursor()

