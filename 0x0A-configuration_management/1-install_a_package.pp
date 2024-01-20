# 1-install_a_package.pp

# Define the package resource for flask
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  install_options => ['-I'],  # Ignore installed version and force installation
}
