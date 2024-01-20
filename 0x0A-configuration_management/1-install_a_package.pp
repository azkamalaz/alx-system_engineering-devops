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
