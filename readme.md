# Music App
A music app for Second Life.


# Requirements
* Python 3
* Django
* Postgresql (Soft requirement. SQLite can be used, other databases *might* be usable)


# Installation
TODO


# Troubleshooting

## Server keeps 500ing
You might be using SQLite. SQLite can only be accessed by one instance at a time.
You need to set the number of instances in uWSGI to 1, or use PostgreSQL.


# Linden Lab Trademarks
It is **IMPORTANT** to use Linden Lab Trademarks appropriately.
Please see their official guide on what is and is not acceptable:
* https://secondlife.com/corporate/linden-lab-trademarks-list
* (GOOD) https://secondlife.com/corporate/trademark-reference
* (BAD) https://secondlife.com/corporate/trademark-unauthorized
