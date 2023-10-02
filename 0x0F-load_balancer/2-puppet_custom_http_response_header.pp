class nginx_customization {
  file_line { 'add_x_served_by_header':
    path    => '/etc/nginx/sites-enabled/default',
    line    => "    add_header X-Served-By ${hostname};",
    match   => "/server_name _;/",
    ensure  => present,
    require => Service['nginx'],
  }

  service { 'nginx':
    ensure    => 'running',
    enable    => true,
    subscribe => File_line['add_x_served_by_header'],
  }
}

include nginx_customization
