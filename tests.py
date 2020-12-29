import TrinityPyDatabase
import TrinityPyAuth

TrinityPyDatabase.connect("127.0.0.1", 3306, "trinity", "trinity")

def test_if_account_exists():
    assert TrinityPyDatabase.user_exists("AfrofuturismX")

def test_account_not_exist():
    assert not TrinityPyDatabase.user_exists("hgtuoijrtu35rhtnrjhb43ou;oj4nthr4rjie3jk")

def test_hash_correct():
    assert TrinityPyAuth.are_credentials_correct("TestUser123456", "hunter2")

def test_create_acct():
    TrinityPyAuth.create_account("JokerMan456780", "iamjokerman2", "test1233@gmail.com")

def test_change_pwd():
    TrinityPyAuth.change_password("JokerMan4567", "iamjokerman23")

def test_get_online_players():
    assert TrinityPyDatabase.get_online_players_count() == 1

def test_char_table():
    print(TrinityPyDatabase.get_player_health("Kalaumyaymoo"))
    print(TrinityPyDatabase.set_player_money("Kalaumyaymoo", 900000))
    print(TrinityPyDatabase.get_player_money("Kalaumyaymoo"))
    print(TrinityPyDatabase.get_player_total_kills("Kalaumyaymoo"))
    print(TrinityPyDatabase.get_player_today_kills("Kalaumyaymoo"))
    print(TrinityPyDatabase.get_player_total_playtime("Kalaumyaymoo"))
    print(TrinityPyDatabase.get_player_ping("Kalaumyaymoo"))
    print(TrinityPyDatabase.is_player_online("Kalaumyaymoo"))
    print(TrinityPyDatabase.get_player_honor_points("Kalaumyaymoo"))
    print(TrinityPyDatabase.get_player_level("Kalaumyaymoo"))
    print(TrinityPyDatabase.get_characters_by_account_name("AfrofuturismX"))
    print(TrinityPyDatabase.revive_character_next_login("Kalaumyaypoo"))
    print(TrinityPyDatabase.customize_character_next_login("Kalaumyaypoo"))
    print(TrinityPyDatabase.set_player_health("Kalaumyaypoo", 80))
    print(TrinityPyDatabase.get_top_characters_by_money("Kalaumyaypoo"))
    print(TrinityPyDatabase.get_top_characters_by_total_kills("Kalaumyaypoo"))
    print(TrinityPyDatabase.get_top_characters_by_total_time("Kalaumyaypoo"))
    print("Level " + str(TrinityPyDatabase.get_player_level("Kalaumyaymoo")))
    print(TrinityPyDatabase.get_player_race_name("Kalaumyaymoo"))
    print(TrinityPyDatabase.get_player_class_name("Kalaumyaymoo"))

test_if_account_exists()
test_account_not_exist()
test_hash_correct()
test_create_acct()
test_change_pwd()
test_char_table()
#test_get_online_players()

print("All tests passed!")