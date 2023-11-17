# Fixing web server that's not doing well

file { 'fix-request':
  ensure => 'file',
  command => inline_template('<%= File.read("/etc/default/nginx").gsub(/15/, "4096") %>'),
  path    => '/etc/default/nginx'
}

# Restart Nginx
-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
