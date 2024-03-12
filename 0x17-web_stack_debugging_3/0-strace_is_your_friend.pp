# puppet fix for code 500

exec { 'fix-wordpress':
  command  => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  provider => shell,
  path     => '/usr/local/sbin:/usr/local/bin:usr/sbin:/usr/bin:/sbin:/bin',
}
