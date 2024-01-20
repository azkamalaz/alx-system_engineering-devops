package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  install_options => ['-I'],  # Ignore installed version and force installation
}
