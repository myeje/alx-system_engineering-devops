# This executes a bash command

exec { 'killme':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin']
}