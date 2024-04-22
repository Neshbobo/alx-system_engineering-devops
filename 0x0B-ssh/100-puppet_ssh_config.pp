# Set the SSH client configuration file
file { '/etc/ssh/ssh_config':
  ensure  => file,
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => @(SSH_CONFIG),
}

# Define the SSH client configuration content
$ssh_config = @(SSH_CONFIG) {
  'UseKeychain yes'
  'IdentityFile ~/.ssh/school'
  'PasswordAuthentication no'
}

# Generate the SSH client configuration content
$ssh_config = $ssh_config.strip.split("\n").sort.join("\n")

# Define the SSH client configuration content as a variable
define ssh_config ($content) {
  file { '/etc/ssh/ssh_config':
    ensure  => file,
    mode    => '0644',
    owner   => 'root',
    group   => 'root',
    content => $content,
  }
}

# Create the SSH client configuration
ssh_config { $ssh_config: }