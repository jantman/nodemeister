nodemeister
===========

.. image:: http://www.repostatus.org/badges/latest/unsupported.svg
   :alt: Project Status: Unsupported – The project has reached a stable, usable state but the author(s) have ceased all work on it. A new maintainer may be desired.
   :target: http://www.repostatus.org/#unsupported

NodeMeister is an External Node Classifier (ENC) for Puppet. It maintains a
database of your nodes, as well as what parameters and classes (including
parameterized classes) apply to them. It also supports hierarchical groups,
exclusions and overrides.

NodeMeister is written in Python, using the Django framework, backed by a
Postgres database. We wanted not
only to create an ENC that meets certain feature gaps lacking in (at the time
of writing) other options, but also which is friendly to the non-Rubyists out
there.

**BE WARNED this is currently alpha code. Very alpha code. So long as this
message is here, we make no guarantee that it will even run outside of a very
specific configuration. At the very least, it has few to no tests, depends on
a Python package that's only available as a pull request on GitHub, and has
many unused code paths still in the code base. It needs quite a bit of work
before we can consider it ready for production use outside of our own
environment. It's being put out here in this early state both out of agreement
with the original author, and because of some recent interest in the Puppet
community around alternate ENCs.**

Why?
----

There are a few well-known ENCs out there. One of the authors wrote a `blog post <http://blog.jasonantman.com/2012/02/the-state-of-puppet-external-node-classifiers/>`_
about some of them in February 2012, and in November 2013 the scene doesn't
seem to have changed much. There's `Puppet Dashboard <http://projects.puppetlabs.com/projects/dashboard>`_ 
(open source) and `Puppet Enterprise <http://puppetlabs.com/puppet/puppet-enterprise>`_
Console (the paid version of Dashboard, with a bunch of advanced features),
and there's `The Foreman <http://theforeman.org/projects/foreman>`_. And then
there's a bunch of other tools that can function as an ENC, and a pile of
internally-developed ENCs that may or may not be released publicly, and may or
may not be useful outside the company that wrote them (many of us have
contributed to this).

So why another ENC?

First, NodeMeister aims to be *just* an ENC. Dashboard and Foreman are both packed
with features. Dashboard/Console gives a lot (event inspection, report
storage/processing, live management) at the cost of being terribly slow. The
Foreman is a wonderful application, but if you're not managing DHCP and DNS
and cloud/virtual resources with it, you're not using 75% of its capabilities
(and form fields). NodeMeister lets you stay close to your data. It's designed
to be fast, predictable, and simple. It's designed to follow a simple mental
model of data. There's no editing of a "class", as that has no logical mapping
directly to the YAML data sent back to the puppet master. We're not against
hooking in to other services, but it's mainly about the data.

* Python/Django. It's what we happen to know (we're a Django shop through and
  through), and not everyone is a Ruby wizard. It's an ENC for the rest of us.
* Inheritance is done logically, from least to most specific. Classes or
  parameters will override less specific definitions.
* Classes or parameters can be excluded at any level. It's possible to exclude
  a class or parameter from being inherited at any level - even if you have a
  group with 1000 nodes, you can still exclude a class from being applied to
  one or two of them.
* Simple REST API
* Builds upon the power and stability of the Django framework - minimal custom
  code.
* Environment-agnostic. No need to import modules or define environments.
* Full support for parameterized classes and deep data structures (anything
  that can be represented in YAML and JSON).
* It scales. Period.
* Simple UI.
* Atomic changes - unlike Dashboard or Foreman, you can make any number of
  changes to a node or group and commit them in one transaction, eliminating
  possible inconsistent states while making changes through the UI.
* Classes and class parameters are edited on the page for the group or node
  they apply to. If the same class/parameters is needed in more than one
  place, a group should be used.

Planned but not yet fully implemented:

* Full audit logging, and versioning of all data; ability to roll back any
  change.
* Fine-grained access control at any object level.
* Use PuppetDB to store reports, facts, etc. With PuppetDB there's no longer a
  need to duplicate this in an ENC.
* Report processing, or integration with a report processor (puppetboard?)

Known Issues
------------

* NodeMeister requires a patched version of `fullhistory <https://pypi.python.org/pypi/fullhistory/>`_
  based on a `pull request <https://github.com/cuker/django-fullhistory/pull/3>`_ that
  isn't accepted yet. It appears that fullhistory is not actively maintained.
* django-jsonfield needs everything to be valid JSON, so strings must be quoted

Requirements
------------

* Python 2.6 (tested against 2.6.6)
* currently, a version of django-fullhistory that doesn't exist in the wild. See `django-fullhistory pull request 3 <https://github.com/cuker/django-fullhistory/pull/3>`_
* we use pytest-django for testing, and it currently requires Python 2.5-2.7,
  Django 1.3-1.6, and py.test 2.3.4+
* PostgresQL database

Installation
------------

Nothing Here Yet.

Usage
-----

At the moment, there's no "real" user interface. Set it up on a vhost, and browse to hostname/admin/. You should get the Django 

Development
===========

To install for development:

need to document instructions here.

.. code-block:: bash

    $ virtualenv nodemeister
    $ cd nodemeister && source bin/activate
    $ git clone repo

Testing
-------

Testing is done via `pytest <http://pytest.org/latest/>`_, driven by `tox <http://tox.testrun.org/>`_.
At the moment the project doesn't really have any tests. That's part of what
I'm trying to fix at the moment.

When tests are done, we should ideally end up with two sets of environments -
one that's entirely self-contained (i.e. static tests only), and one that
requires an actual database to run against.

* testing is as simple as:

  * ``pip install tox``
  * ``tox``

* If you want to see code coverage: ``py.test --cov-report term-missing --cov-report html --cov=.``

  * this produces two coverage reports - a summary on STDOUT and a full report in the ``htmlcov/`` directory

License
-------

NodeMeister is licensed under the `Apache License, version 2.0 <http://www.apache.org/licenses/LICENSE-2.0.html>`_.
A copy of the license is included in LICENSE.txt.

NodeMeister is Copyright 2013 `Cox Media Group <http://cmgdigital.com/>`_ and Contributors.

NodeMeister was originally written by Eli Meister as a lab project at Cox
Media Group Digital (CMGd, now Cox Media Group Technology / CMGt). Since then
maintenance and development has continued both internally at CMG, as well as
on a volunteer (read: personal time) basis by some CMG employees.
