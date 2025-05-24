# create-deploymentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-deployment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-deployment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opsworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/index.html#cli-aws-opsworks) ]

# create-deployment

## Description

Runs deployment or stack commands. For more information, see [Deploying Apps](https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-deploying.html) and [Run Stack Commands](https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-commands.html) .

**Required Permissions** : To use this action, an IAM user must have a Deploy or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see [Managing User Permissions](https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateDeployment)

## Synopsis

```
create-deployment
--stack-id <value>
[--app-id <value>]
[--instance-ids <value>]
[--layer-ids <value>]
--command <value>
[--comment <value>]
[--custom-json <value>]
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

`--stack-id` (string)

The stack ID.

`--app-id` (string)

The app ID. This parameter is required for app deployments, but not for other deployment commands.

`--instance-ids` (list)

The instance IDs for the deployment targets.

(string)

Syntax:

```
"string" "string" ...
```

`--layer-ids` (list)

The layer IDs for the deployment targets.

(string)

Syntax:

```
"string" "string" ...
```

`--command` (structure)

A `DeploymentCommand` object that specifies the deployment command and any associated arguments.

Name -> (string)

Specifies the operation. You can specify only one command.

For stacks, the following commands are available:

- `execute_recipes` : Execute one or more recipes. To specify the recipes, set an `Args` parameter named `recipes` to the list of recipes to be executed. For example, to execute `phpapp::appsetup` , set `Args` to `{"recipes":["phpapp::appsetup"]}` .
- `install_dependencies` : Install the stackâs dependencies.
- `update_custom_cookbooks` : Update the stackâs custom cookbooks.
- `update_dependencies` : Update the stackâs dependencies.

### Note

The update_dependencies and install_dependencies commands are supported only for Linux instances. You can run the commands successfully on Windows instances, but they do nothing.

For apps, the following commands are available:

- `deploy` : Deploy an app. Ruby on Rails apps have an optional `Args` parameter named `migrate` . Set `Args` to {âmigrateâ:[âtrueâ]} to migrate the database. The default setting is {âmigrateâ:[âfalseâ]}.
- `rollback` Roll the app back to the previous version. When you update an app, OpsWorks Stacks stores the previous version, up to a maximum of five versions. You can use this command to roll an app back as many as four versions.
- `start` : Start the appâs web or application server.
- `stop` : Stop the appâs web or application server.
- `restart` : Restart the appâs web or application server.
- `undeploy` : Undeploy the app.

Args -> (map)

The arguments of those commands that take arguments. It should be set to a JSON object with the following format:

`{"arg_name1" : ["value1", "value2", ...], "arg_name2" : ["value1", "value2", ...], ...}`

The `update_dependencies` command takes two arguments:

- `upgrade_os_to` - Specifies the Amazon Linux version that you want instances to run, such as `Amazon Linux 2` . You must also set the `allow_reboot` argument to true.
- `allow_reboot` - Specifies whether to allow OpsWorks Stacks to reboot the instances if necessary, after installing the updates. This argument can be set to either `true` or `false` . The default value is `false` .

For example, to upgrade an instance to Amazon Linux 2018.03, set `Args` to the following.

`{ "upgrade_os_to":["Amazon Linux 2018.03"], "allow_reboot":["true"] }`

key -> (string)

value -> (list)

(string)

Shorthand Syntax:

```
Name=string,Args={KeyName1=string,string,KeyName2=string,string}
```

JSON Syntax:

```
{
  "Name": "install_dependencies"|"update_dependencies"|"update_custom_cookbooks"|"execute_recipes"|"configure"|"setup"|"deploy"|"rollback"|"start"|"stop"|"restart"|"undeploy",
  "Args": {"string": ["string", ...]
    ...}
}
```

`--comment` (string)

A user-defined comment.

`--custom-json` (string)

A string that contains user-defined, custom JSON. You can use this parameter to override some corresponding default stack configuration JSON values. The string should be in the following format:

`"{\"key1\": \"value1\", \"key2\": \"value2\",...}"`

For more information about custom JSON, see [Use Custom JSON to Modify the Stack Configuration Attributes](https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-json.html) and [Overriding Attributes With Custom JSON](https://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook-json-override.html) .

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

**Example 1: To deploy apps and run stack commands**

The following examples show how to use the `create-deployment` command to deploy apps and run stack commands.  Notice that the quote (`"`) characters in the JSON object that specifies the command are all preceded by escape characters (\). Without the escape characters, the command might return an invalid JSON error.

The following `create-deployment` example deploys an app to a specified stack.

```
aws opsworks create-deployment \
    --stack-id cfb7e082-ad1d-4599-8e81-de1c39ab45bf \
    --app-id 307be5c8-d55d-47b5-bd6e-7bd417c6c7eb
    --command "{\"Name\":\"deploy\"}"
```

Output:

```
{
    "DeploymentId": "5746c781-df7f-4c87-84a7-65a119880560"
}
```

**Example 2: To deploy a Rails App and Migrate the Database**

The following `create-deployment` command deploys a Ruby on Rails app to a specified stack and migrates the database.

```
aws opsworks create-deployment \
    --stack-id cfb7e082-ad1d-4599-8e81-de1c39ab45bf \
    --app-id 307be5c8-d55d-47b5-bd6e-7bd417c6c7eb \
    --command "{\"Name\":\"deploy\", \"Args\":{\"migrate\":[\"true\"]}}"
```

Output:

```
{
    "DeploymentId": "5746c781-df7f-4c87-84a7-65a119880560"
}
```

For more information on deployment, see [Deploying Apps](https://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-deploying.html) in the *AWS OpsWorks User Guide*.

**Example 3: Run a Recipe**

The following `create-deployment` command runs a custom recipe, `phpapp::appsetup`, on the instances in a specified stack.

```
aws opsworks create-deployment \
    --stack-id 935450cc-61e0-4b03-a3e0-160ac817d2bb \
    --command "{\"Name\":\"execute_recipes\", \"Args\":{\"recipes\":[\"phpapp::appsetup\"]}}"
```

Output:

```
{
    "DeploymentId": "5cbaa7b9-4e09-4e53-aa1b-314fbd106038"
}
```

For more information, see [Run Stack Commands](https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-commands.html) in the *AWS OpsWorks User Guide*.

**Example 4: Install Dependencies**

The following `create-deployment` command installs dependencies, such as packages or Ruby gems, on the instances in a
specified stack.

```
aws opsworks create-deployment \
    --stack-id 935450cc-61e0-4b03-a3e0-160ac817d2bb \
    --command "{\"Name\":\"install_dependencies\"}"
```

Output:

```
{
    "DeploymentId": "aef5b255-8604-4928-81b3-9b0187f962ff"
}
```

For more information, see [Run Stack Commands](https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-commands.html) in the *AWS OpsWorks User Guide*.

## Output

DeploymentId -> (string)

The deployment ID, which can be used with other requests to identify the deployment.