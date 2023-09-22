#!/usr/bin/pup
# Using Puppet, install flask from pip3.
package { 'flask':
    ensure   => 'installed',
    version  => '2.1.0',
    provider => 'pip',
}