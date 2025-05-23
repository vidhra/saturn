# registerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opsworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/index.html#cli-aws-opsworks) ]

# register

## Description

Registers an EC2 instance or machine with AWS OpsWorks.

Registering a machine using this command will install the AWS OpsWorks
agent on the target machine and register it with an existing OpsWorks
stack.

## Synopsis

```
register
--stack-id <value>
--infrastructure-class <value>
[--override-hostname <value>]
[--override-private-ip <value>]
[--override-public-ip <value>]
[--override-ssh <value>]
[--ssh-username <value>]
[--ssh-private-key <value>]
[--local]
[--use-instance-profile]
[<target>]
[--debug]
[--endpoint-url <value>]
[--no-verify-ssl]
[--no-paginate]
[--output <value>]
[--query <value>]
[--profile <value>]
[--region <value>]
[--version <value>]
[--color <value>]
[--no-sign-request]
[--ca-bundle <value>]
[--cli-read-timeout <value>]
[--cli-connect-timeout <value>]
[--cli-binary-format <value>]
[--no-cli-pager]
[--cli-auto-prompt]
[--no-cli-auto-prompt]
```

## Options

`--stack-id` (string)
A stack ID. The instance will be registered with the given stack.

`--infrastructure-class` (string)
Specifies whether to register an EC2 instance (ec2) or an on-premises instance (on-premises).

`--override-hostname` (string)
The instance hostname. If not provided, the current hostname of the machine will be used.

`--override-private-ip` (string)
An IP address. If you set this parameter, the given IP address will be used as the private IP address within OpsWorks. Otherwise the private IP address will be determined automatically. Not to be used with EC2 instances.

`--override-public-ip` (string)
An IP address. If you set this parameter, the given IP address will be used as the public IP address within OpsWorks. Otherwise the public IP address will be determined automatically. Not to be used with EC2 instances.

`--override-ssh` (string)
If you set this parameter, the given command will be used to connect to the machine.

`--ssh-username` (string)
If provided, this username will be used to connect to the host.

`--ssh-private-key` (string)
If provided, the given private key file will be used to connect to the machine.

`--local` (boolean)
If given, instead of a remote machine, the local machine will be imported. Cannot be used together with target.

`--use-instance-profile` (boolean)
Use the instance profile instead of creating an IAM user.

`target` (string)
Either the EC2 instance ID or the hostname of the instance or machine to be registered with OpsWorks. Cannot be used together with âlocal.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override commandâs default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To register instances with a stack**

The following examples show a variety of ways to register instances with a stack that were created outside of AWS Opsworks.
You can run `register` from the instance to be registered, or from a separate workstation.
For more information, see [Registering Amazon EC2 and On-premises Instances](http://docs.aws.amazon.com/opsworks/latest/userguide/registered-instances-register-registering.html) in the *AWS OpsWorks User Guide*.

**Note**: For brevity, the examples omit the `region` argument.

*To register an Amazon EC2 instance*

To indicate that you are registering an EC2 instance, set the `--infrastructure-class` argument
to `ec2`.

The following example registers an EC2 instance with the specified stack from a separate workstation.
The instance is identified by its EC2 ID, `i-12345678`. The example uses the workstationâs default SSH username and attempts
to log in to the instance using authentication techniques that do not require a password,
such as a default private SSH key. If that fails, `register` queries for the password.

```
aws opsworks register --infrastructure-class=ec2 --stack-id 935450cc-61e0-4b03-a3e0-160ac817d2bb i-12345678
```

The following example registers an EC2 instance with the specifed stack from a separate workstation.
It uses the `--ssh-username` and `--ssh-private-key` arguments to explicitly
specify the SSH username and private key file that the command uses to log into the instance.
`ec2-user` is the standard username for Amazon Linux instances. Use `ubuntu` for Ubuntu instances.

```
aws opsworks register --infrastructure-class=ec2 --stack-id 935450cc-61e0-4b03-a3e0-160ac817d2bb --ssh-username ec2-user --ssh-private-key ssh_private_key i-12345678
```

The following example registers the EC2 instance that is running the `register` command.
Log in to the instance with SSH and run `register` with the `--local` argument instead of an instance ID or hostname.

```
aws opsworks register --infrastructure-class ec2 --stack-id 935450cc-61e0-4b03-a3e0-160ac817d2bb --local
```

*To register an on-premises instance*

To indicate that you are registering an on-premises instance, set the `--infrastructure-class` argument
to `on-premises`.

The following example registers an existing on-premises instance with a specified stack from a separate workstation.
The instance is identified by its IP address, `192.0.2.3`. The example uses the workstationâs default SSH username and attempts
to log in to the instance using authentication techniques that do not require a password,
such as a default private SSH key. If that fails, `register` queries for the password.

```
aws opsworks register --infrastructure-class on-premises --stack-id 935450cc-61e0-4b03-a3e0-160ac817d2bb 192.0.2.3
```

The following example registers an on-premises instance with a specified stack from a separate workstation.
The instance is identified by its hostname, `host1`. The `--override-...` arguments direct AWS OpsWorks
to display `webserver1` as the host name and `192.0.2.3` and `10.0.0.2` as the instanceâs public and
private IP addresses, respectively.

```
aws opsworks register --infrastructure-class on-premises --stack-id 935450cc-61e0-4b03-a3e0-160ac817d2bb --override-hostname webserver1 --override-public-ip 192.0.2.3 --override-private-ip 10.0.0.2 host1
```

The following example registers an on-premises instance with a specified stack from a separate workstation.
The instance is identified by its IP address. `register` logs into the instance using the specified SSH username and private key file.

```
aws opsworks register --infrastructure-class on-premises --stack-id 935450cc-61e0-4b03-a3e0-160ac817d2bb --ssh-username admin --ssh-private-key ssh_private_key 192.0.2.3
```

The following example registers an existing on-premises instance with a specified stack from a separate workstation.
The command logs into the instance using a custom SSH command string that specifies
the SSH password and the instanceâs IP address.

```
aws opsworks register --infrastructure-class on-premises --stack-id 935450cc-61e0-4b03-a3e0-160ac817d2bb --override-ssh "sshpass -p 'mypassword' ssh your-user@192.0.2.3"
```

The following example registers the on-premises instance that is running the `register` command.
Log in to the instance with SSH and run `register` with the `--local` argument instead of an instance ID or hostname.

```
aws opsworks register --infrastructure-class on-premises --stack-id 935450cc-61e0-4b03-a3e0-160ac817d2bb --local
```

*Output*: The following is typical output for registering an EC2 instance.

```
Warning: Permanently added '52.11.41.206' (ECDSA) to the list of known hosts.
% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                               Dload  Upload   Total   Spent    Left  Speed
100 6403k  100 6403k    0     0  2121k      0  0:00:03  0:00:03 --:--:-- 2121k
[Tue, 24 Feb 2015 20:48:37 +0000] opsworks-init: Initializing AWS OpsWorks environment
[Tue, 24 Feb 2015 20:48:37 +0000] opsworks-init: Running on Ubuntu
[Tue, 24 Feb 2015 20:48:37 +0000] opsworks-init: Checking if OS is supported
[Tue, 24 Feb 2015 20:48:37 +0000] opsworks-init: Running on supported OS
[Tue, 24 Feb 2015 20:48:37 +0000] opsworks-init: Setup motd
[Tue, 24 Feb 2015 20:48:37 +0000] opsworks-init: Executing: ln -sf --backup /etc/motd.opsworks-static /etc/motd
[Tue, 24 Feb 2015 20:48:37 +0000] opsworks-init: Enabling multiverse repositories
[Tue, 24 Feb 2015 20:48:37 +0000] opsworks-init: Customizing APT environment
[Tue, 24 Feb 2015 20:48:37 +0000] opsworks-init: Installing system packages
[Tue, 24 Feb 2015 20:48:37 +0000] opsworks-init: Executing: dpkg --configure -a
[Tue, 24 Feb 2015 20:48:37 +0000] opsworks-init: Executing with retry: apt-get update
[Tue, 24 Feb 2015 20:49:13 +0000] opsworks-init: Executing: apt-get install -y ruby ruby-dev libicu-dev libssl-dev libxslt-dev libxml2-dev libyaml-dev monit
[Tue, 24 Feb 2015 20:50:13 +0000] opsworks-init: Using assets bucket from environment: 'opsworks-instance-assets-us-east-1.s3.amazonaws.com'.
[Tue, 24 Feb 2015 20:50:13 +0000] opsworks-init: Installing Ruby for the agent
[Tue, 24 Feb 2015 20:50:13 +0000] opsworks-init: Executing: /tmp/opsworks-agent-installer.YgGq8wF3UUre6yDy/opsworks-agent-installer/opsworks-agent/bin/installer_wrapper.sh -r -R opsworks-instance-assets-us-east-1.s3.amazonaws.com
[Tue, 24 Feb 2015 20:50:44 +0000] opsworks-init: Starting the installer
Instance successfully registered. Instance ID: 4d6d1710-ded9-42a1-b08e-b043ad7af1e2
Connection to 52.11.41.206 closed.
```

**More Information**

For more information, see [Registering an Instance with an AWS OpsWorks Stack](http://docs.aws.amazon.com/opsworks/latest/userguide/registered-instances-register.html) in the *AWS OpsWorks User Guide*.