# Fixing web server that's not doing well

exec { 'fix--for-nginx':
  ensure => 'file',
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/etc/default/nginx'
}

-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
