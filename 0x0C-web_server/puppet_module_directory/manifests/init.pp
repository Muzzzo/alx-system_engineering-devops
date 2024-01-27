# puppet_module_directory/manifests/init.pp

# Setup New Ubuntu server with nginx

exec { 'update system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('your_module_name/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

nginx::resource::location { '/redirect_me':
  ensure          => present,
  location        => '^/redirect_me$',
  www_root        => '/var/www/html',
  index_files     => ['index.html'],
  rewrite_to      => 'https://www.youtube.com/watch?v=QH2-TGUlwu4',
  rewrite_options => 'permanent',
  require         => File['/etc/nginx/sites-available/default'],
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}

