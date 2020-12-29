# TrinityPy
## Introduction
TrinityPy is a **super simple** Python library for interacting with your [TrinityCore 3.3.5](https://github.com/TrinityCore/TrinityCore/tree/3.3.5) server. TrinityPy allows you to interact with your
server, but without fiddling with any SQL, and instead providing clean, one-liner Python solutions for many actions.<br>

TrinityPy is compatible with the latest TrinityCore 3.3.5 version, and works with the [new authentication system](https://github.com/TrinityCore/TrinityCore/commit/bcdbdd6f23ce65cc0e381e61d2840140dce79311).

## Examples
```python
import TrinityPyAuth
import TrinityPyDatabase
TrinityPyDatabase.connect("127.0.0.1", 3306, "trinity", "trinity", "auth", "characters")

TrinityPyAuth.create_account("JokerMan456780", "iamjokerman2", "test1233@gmail.com")
TrinityPyAuth.change_password("JokerMan456780", "iamjokerman23")

cash = TrinityPyDatabase.get_player_money("Kalaumyaymoo")
TrinityPyDatabase.set_player_health("Kalaumyaymoo" 50)
```
The code above creates an account, changes its passwords, stores a player's money in a variable, and sets
the player's health to 50. Pretty self-explanatory and easy, right?

[Check out the wiki](https://github.com/UltraFuture7000/TrinityPy/wiki) for more examples and documentation!

## Documentation
Before using any library functions, you need to connect to the database. [See here for more info](https://github.com/UltraFuture7000/TrinityPy/wiki/Home/_edit#before-using-the-library).<br>

``TrinityPyAuth.py`` provides features such as account creation, password reset, and authentication checks.<br>
``TrinityPyDatabase.py`` provides everything else!

[TrinityPyAuth.py documentation](https://github.com/UltraFuture7000/TrinityPy/wiki/TrinityPyAuth-documentation)<br>
[TrinityPyDatabase.py documentation](https://github.com/UltraFuture7000/TrinityPy/wiki/TrinityPyDatabase-documentation)

## Setup
Just install the requirements, connect to your database, and use any functions you like.<br><br>
Step 0) Clone this repo (``git clone https://github.com/UltraFuture7000/TrinityPy``)<br>
Step 1) ``pip install -r requirements.txt`` to install the requirements.<br>
Step 2) Connecting to the database:

```python
import TrinityPyDatabase

TrinityPyDatabase.connect("127.0.0.1", 3306, "trinity", "trinity", "auth", "characters")
# You are now ready to use any TrinityPy functions!
```

## Use cases
TrinityPy is being developed for the upcoming Velamoon 3.3.5a server, but has been developed from the ground-up with the intention of it being open-source.

Use cases include using your own Python code along TrinityPy to control your server, or even a Flask or Django webserver to allow many web-based actions.

## License
TrinityPy is licensed under the [Apache License 2.0](https://github.com/UltraFuture7000/TrinityPy/blob/main/LICENSE).
