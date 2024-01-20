# 1-install_a_package.pp

class { 'python':
  version => 'system',
}

class { 'python::pip':
  version => 'system',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Class['python::pip'],
}

package { 'Werkzeug':
  ensure   => '2.0.2',
  provider => 'pip3',
  require  => Class['python::pip'],
}
