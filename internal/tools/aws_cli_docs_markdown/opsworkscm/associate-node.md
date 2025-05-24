# associate-nodeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/associate-node.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/associate-node.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opsworkscm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/index.html#cli-aws-opsworkscm) ]

# associate-node

## Description

Associates a new node with the server. For more information about how to disassociate a node, see  DisassociateNode .

On a Chef server: This command is an alternative to `knife bootstrap` .

Example (Chef): `aws opsworks-cm associate-node --server-name *MyServer* --node-name *MyManagedNode* --engine-attributes "Name=*CHEF_ORGANIZATION* ,Value=default" "Name=*CHEF_NODE_PUBLIC_KEY* ,Value=*public-key-pem* "`

On a Puppet server, this command is an alternative to the `puppet cert sign` command that signs a Puppet node CSR.

Example (Puppet): `aws opsworks-cm associate-node --server-name *MyServer* --node-name *MyManagedNode* --engine-attributes "Name=*PUPPET_NODE_CSR* ,Value=*csr-pem* "`

A node can can only be associated with servers that are in a `HEALTHY` state. Otherwise, an `InvalidStateException` is thrown. A `ResourceNotFoundException` is thrown when the server does not exist. A `ValidationException` is raised when parameters of the request are not valid. The AssociateNode API call can be integrated into Auto Scaling configurations, AWS Cloudformation templates, or the user data of a serverâs instance.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/AssociateNode)

## Synopsis

```
associate-node
--server-name <value>
--node-name <value>
--engine-attributes <value>
[--cli-input-json | --cli-input-yaml]
[--generate-cli-skeleton <value>]
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

`--server-name` (string)

The name of the server with which to associate the node.

`--node-name` (string)

The name of the node.

`--engine-attributes` (list)

Engine attributes used for associating the node.

**Attributes accepted in a AssociateNode request for Chef**

- `CHEF_ORGANIZATION` : The Chef organization with which the node is associated. By default only one organization named `default` can exist.
- `CHEF_NODE_PUBLIC_KEY` : A PEM-formatted public key. This key is required for the `chef-client` agent to access the Chef API.

**Attributes accepted in a AssociateNode request for Puppet**

- `PUPPET_NODE_CSR` : A PEM-formatted certificate-signing request (CSR) that is created by the node.

(structure)

A name and value pair that is specific to the engine of the server.

Name -> (string)

The name of the engine attribute.

Value -> (string)

The value of the engine attribute.

Shorthand Syntax:

```
Name=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Value": "string"
  }
  ...
]
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--generate-cli-skeleton` (string)
Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

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

**To associate nodes**

The following `associate-node` command associates a node named `i-44de882p` with
a Chef Automate server named `automate-06`, meaning that the `automate-06` server
manages the node, and communicates recipe commands to the node through `chef-client` agent software
that is installed on the node by the associate-node command. Valid node names are EC2 instance IDs.:

```
aws opsworks-cm associate-node --server-name "automate-06" --node-name "i-43de882p" --engine-attributes "Name=CHEF_ORGANIZATION,Value='MyOrganization' Name=CHEF_NODE_PUBLIC_KEY,Value='Public_key_contents'"
```

The output returned by the command resembles the following.
*Output*:

```
{
 "NodeAssociationStatusToken": "AHUY8wFe4pdXtZC5DiJa5SOLp5o14DH//rHRqHDWXxwVoNBxcEy4V7R0NOFymh7E/1HumOBPsemPQFE6dcGaiFk"
}
```

**More Information**

For more information, see [Adding Nodes Automatically in AWS OpsWorks for Chef Automate](http://docs.aws.amazon.com/opsworks/latest/userguide/opscm-unattend-assoc.html) in the *AWS OpsWorks User Guide*.

## Output

NodeAssociationStatusToken -> (string)

Contains a token which can be passed to the `DescribeNodeAssociationStatus` API call to get the status of the association request.