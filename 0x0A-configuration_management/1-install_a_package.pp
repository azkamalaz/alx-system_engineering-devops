# Puppet code to install a package puppet-lint

package { 'puppet-lint':
  ensure   => '2.1.0',
  provider => 'gem'
}
