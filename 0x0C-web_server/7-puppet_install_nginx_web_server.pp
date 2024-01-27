# Setup New Ubuntu server with Nginx

# Update system
exec { 'update system':
  command => '/usr/bin/apt-get update',
}

# Install Nginx package
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system'],
}

# Create Hello World index page
file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure redirect for /redirect_me
nginx::resource::location { '/redirect_me':
  ensure          => present,
  location        => '^/redirect_me$',
  www_root        => '/var/www/html',
  index_files     => ['index.html'],
  rewrite_to      => 'https://www.youtube.com/watch?v=QH2-TGUlwu4',
  rewrite_options => 'permanent',
  require         => Package['nginx'],
}

# Start Nginx service
service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}

