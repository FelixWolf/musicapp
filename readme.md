# Music App
A music app for Second Life.


# Requirements
* Python 3
* Django
* Postgresql (Soft requirement. SQLite can be used, other databases *might* be usable)


# Installation
1. `python3 -m pip install django`
2. `git clone https://github.com/FelixWolf/musicapp`
3. `cd musicapp`
4. `python3 manage.py migrate`
5. `python3 manage.py runserver`


# Troubleshooting

## Server keeps 500ing
You might be using SQLite. SQLite can only be accessed by one instance at a time.
You need to set the number of instances in uWSGI to 1, or use PostgreSQL.


# Linden Lab Trademarks
It is **IMPORTANT** to use Linden Lab's trademarks appropriately.
Please see their official guide on what is and is not acceptable:
* https://secondlife.com/corporate/linden-lab-trademarks-list
* (GOOD) https://secondlife.com/corporate/trademark-reference
* (BAD) https://secondlife.com/corporate/trademark-unauthorized

Second Life® is a trademark of Linden Research, Inc. This project is not not affiliated with, endorsed by, or sponsored by Linden Research.