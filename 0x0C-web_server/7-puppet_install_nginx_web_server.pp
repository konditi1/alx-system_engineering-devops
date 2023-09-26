# Ensure Nginx is installed and service is running
class { 'nginx':
  ensure         => 'installed',
  enable         => true,
  service_ensure => 'running',
}

# Define a default server block for port 80
nginx::resource::vhost { 'default_server':
  ensure      => present,
  listen_port => 80,
  server_name => '_',
  root        => '/var/www/html',
  index       => ['index.html', 'index.htm', 'index.nginx-debian.html'],
  access_log  => '/var/log/nginx/access.log',
  error_log   => '/var/log/nginx/error.log',
}

# Create a custom HTML file for redirection
file { '/var/www/html/redirect_me.html':
  ensure  => present,
  content => '<html><head><meta http-equiv="refresh" content="0;URL=https://www.youtube.com/watch?v=QH2-TGUlwu4"></head></html>',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

# Configure the 301 redirection for /redirect_me
nginx::resource::location { 'redirect_me':
  ensure   => present,
  location => '/redirect_me',
  server   => 'default_server',
  proxy    => 'http://www.youtube.com/watch?v=QH2-TGUlwu4',
}

# Create a custom 404 page
file { '/var/www/html/404.html':
  ensure  => present,
  content => 'Ceci n\'est pas une page',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}
