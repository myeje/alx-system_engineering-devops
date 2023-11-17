# This puppet script changes 0S confirguration

exec { 'rep':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  path     => '/usr/local/bin/:/bin/'
}

exec { 'rep-1':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
  path     => '/usr/local/bin/:/bin/'
}
