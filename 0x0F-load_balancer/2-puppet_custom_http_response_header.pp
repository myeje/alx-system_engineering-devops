# This puppet file automates thee task of creating a custom HTTP header response
# ...with Puppet

exec { 'update':
  command => 'usr/bin/apt-get update',
}

package { 'nginx':
  ensure => 'present',
}

file_line { 'http_head':
  path  => '/etc/nginx/nginx.conf',
  line  => "\tadd_header X-served-By ${hostname};",
  match => 'http {',
}

exec { 'run':
  command => ''/usr/sbin/service nginx restart'
}