# 1-install_a_package.pp

# Define the package resource for flask
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Notify the user when the package is installed
notify { 'flask installed successfully':
  require => Package['flask'],
}
