# 1-install_a_package.pp

# Define the package resource for Flask
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Notify the user when the package is installed
notify { 'Flask installed successfully':
  require => Package['Flask'],
}
