enc/fixtures
============

This is a quick and horribly dirty hack.

A short while ago, NodeMeister had no automated tests at all. We wanted *some*
simple form of tests in place before making any real changes to the
codebase. Here's my hack to do that.

Usage is as follows:
1. With a blank/empty NodeMeister database (empty.sql at this time), create
   a node called "testnode" with some groups, classes, params, etc through the
   admin interactively.
2. Run `dump.sh` to create three files named for the time of creation
   (YYYY-MM-DD_HH-MM-SS): a JSON file with the Django objects (`manage.py dumpdata`), 
   a SQL dump of the database, and the ENC YAML output for "testnode".
3. Run `dump_to_creates.py YYYY-MM-DD_HH-MM-SS.json` which attempts to create
   a test funtion that creates the objects specified in the JSON dump, and
   then uses the pytest-django plugin to request the YAML file for "testnode",
   and compares that to the saved YAML file.

This is awful. It makes me cry, and the thought that it might actually make it
to see the light of day is a bit depressing. But being able to run real,
useful unit tests on the NM codebase will require some refactoring, and we
want at least some high-level integration/functional tests before we touch the
internal logic.

Once those unit tests are in place, this (and the tests generated from it)
should go away forever.
