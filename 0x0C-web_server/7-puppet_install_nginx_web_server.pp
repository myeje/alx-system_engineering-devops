# This puppet file installs and configures an Nginx server using Puppet
package { 'nginx':
  ensure => installed,
}

execute { ''}