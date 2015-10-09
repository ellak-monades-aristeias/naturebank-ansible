==========
naturebank
==========

Overview
========

This is an Ansible role that installs naturebank_ on a server.  It
creates a PostgreSQL user "naturebank" and a database "naturebank" owned
by "naturebank". It also sets up an apache virtual host and a gunicorn
service. It uses roles apache-vhost_ and gunicorn-instance_, which must
be installed.

.. _naturebank: https://github.com/ellak-monades-aristeias/naturebank
.. _apache-vhost: https://github.com/aptiko-ansible/apache-vhost
.. _gunicorn-instance: https://github.com/aptiko-ansible/gunicorn-instance

Example::

   - role: naturebank
     naturebank_admins:
     - name: Antonis Christofides
       email: anthony@itia.ntua.gr
     naturebank_server_mail: root@filotis.itia.ntua.gr
     naturebank_port: 8002
     naturebank_server_name: filotis.itia.ntua.gr
     naturebank_server_aliases:
     - filotis.itia.civil.ntua.gr
     - www.filotis.itia.ntua.gr
     - www.filotis.itia.civil.ntua.gr

(``naturebank_secret_key`` and ``postgres_password`` also need to be
specified, by they will normally be in the vault.)

Variables
=========

- ``naturebank_admins``: The system administrators; a list of hashes,
  each hash containing ``name`` and ``email``. When needed, naturebank
  notifies these admins by email.

- ``naturebank_server_email``: The email address from which emails about
  errors appear to be coming.

- ``naturebank_secret_key``: This key is used as the password to the
  database (it is set), and as a secret key for several web-related
  stuff, such as encrypting cookies. Store this in the vault.

- ``naturebank_port``: The port on which the naturebank gunicorn server
  will listen on.

- ``naturebank_server_name``: The domain name on which naturebank will
  be listening.

- ``naturebank_server_aliases``: Alternative domain names. Apache will
  redirect these to ``naturebank_server_name``. Default empty.

- ``naturebank_ssl_cert``, ``naturebank_ssl_key``,
  ``naturebank_chain_certificates``: The keys for https, in ASCII
  format. If ommitted, it will be http only.

- ``postgres_password``: The password of the PostgreSQL ``postgres``
  user. Store this in the vault.

Meta
====

Written by Antonis Christofides

| Copyright (C) 2015 Antonis Christofides
| Copyright (C) 2015 National Technical University of Athens

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/.
