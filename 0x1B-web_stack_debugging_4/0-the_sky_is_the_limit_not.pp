# Fixing web server that's not doing well

file { 'fix-request':
  ensure  => 'file',
  path    => '/usr/local/bin/:/bin/',
  command => 'sed -i "s/15/4096/" /etc/default/nginx'
}

# Restarting Nginx
-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
