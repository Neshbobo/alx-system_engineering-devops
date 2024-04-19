# 1-install_a_package.pp
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
}
package { 'python3-pip':
  ensure => installed,
}

exec { 'update-alternatives':
  command => '/usr/bin/python3.8 /usr/bin/python3',
  onlyif  => 'alternatives --display python | grep -q "link currently points to /usr/bin/python3.8"',
}