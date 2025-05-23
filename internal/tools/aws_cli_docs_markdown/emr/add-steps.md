# add-stepsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/add-steps.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/add-steps.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/index.html#cli-aws-emr) ]

# add-steps

## Description

Add a list of steps to a cluster.

## Synopsis

```
add-steps
--cluster-id <value>
--steps <value> [<value>...]
[--execution-role-arn <value>]
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

`--cluster-id` (string)

A unique string that identifies a cluster. The `create-cluster` command returns this identifier. You can use the `list-clusters` command to get cluster IDs.

`--steps` (list)

Specifies a list of steps to be executed by the cluster. Steps run only on the master node after applications are installed and are used to submit work to a cluster. A step can be specified using the shorthand syntax, by referencing a JSON file or by specifying an inline JSON structure. `Args` supplied with steps should be a comma-separated list of values (`Args=arg1,arg2,arg3` ) or a bracket-enclosed list of values and key-value pairs (`Args=[arg1,arg2=value,arg4` ).

(structure)

Type -> (string)

The type of a step to be added to the cluster.

Name -> (string)

The name of the step.

ActionOnFailure -> (string)

The action to take if the cluster step fails.

Jar -> (string)

A path to a JAR file run during the step.

Args -> (list)

A list of command line arguments to pass to the step.

(string)

MainClass -> (string)

The name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.

Properties -> (string)

A list of Java properties that are set when the step runs. You can use these properties to pass key value pairs to your main function.

Shorthand Syntax:

```
Type=string,Name=string,ActionOnFailure=string,Jar=string,Args=string,string,MainClass=string,Properties=string ...
```

JSON Syntax:

```
[
  {
    "Type": "CUSTOM_JAR"|"STREAMING"|"HIVE"|"PIG"|"IMPALA",
    "Name": "string",
    "ActionOnFailure": "TERMINATE_CLUSTER"|"CANCEL_AND_WAIT"|"CONTINUE",
    "Jar": "string",
    "Args": ["string", ...],
    "MainClass": "string",
    "Properties": "string"
  }
  ...
]
```

`--execution-role-arn` (string)

You must grant the execution role the permissions needed to access the same IAM resources that the step can access. The execution role can be a cross-account IAM Role.

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

**1. To add Custom JAR steps to a cluster**

- Command:

```
aws emr add-steps --cluster-id j-XXXXXXXX --steps Type=CUSTOM_JAR,Name=CustomJAR,ActionOnFailure=CONTINUE,Jar=s3://amzn-s3-demo-bucket/mytest.jar,Args=arg1,arg2,arg3 Type=CUSTOM_JAR,Name=CustomJAR,ActionOnFailure=CONTINUE,Jar=s3://amzn-s3-demo-bucket/mytest.jar,MainClass=mymainclass,Args=arg1,arg2,arg3
```
- Required parameters:

```
Jar
```
- Optional parameters:

```
Type, Name, ActionOnFailure, Args
```
- Output:

```
{
    "StepIds":[
        "s-XXXXXXXX",
        "s-YYYYYYYY"
    ]
}
```

**2. To add Streaming steps to a cluster**

- Command:

```
aws emr add-steps --cluster-id j-XXXXXXXX --steps Type=STREAMING,Name='Streaming Program',ActionOnFailure=CONTINUE,Args=[-files,s3://elasticmapreduce/samples/wordcount/wordSplitter.py,-mapper,wordSplitter.py,-reducer,aggregate,-input,s3://elasticmapreduce/samples/wordcount/input,-output,s3://amzn-s3-demo-bucket/wordcount/output]
```
- Required parameters:

```
Type, Args
```
- Optional parameters:

```
Name, ActionOnFailure
```
- JSON equivalent (contents of step.json):

```
[
  {
    "Name": "JSON Streaming Step",
    "Args": ["-files","s3://elasticmapreduce/samples/wordcount/wordSplitter.py","-mapper","wordSplitter.py","-reducer","aggregate","-input","s3://elasticmapreduce/samples/wordcount/input","-output","s3://amzn-s3-demo-bucket/wordcount/output"],
    "ActionOnFailure": "CONTINUE",
    "Type": "STREAMING"
  }
]
```

NOTE: JSON arguments must include options and values as their own items in the list.

- Command (using step.json):

```
aws emr add-steps --cluster-id j-XXXXXXXX --steps file://./step.json
```
- Output:

```
{
    "StepIds":[
        "s-XXXXXXXX",
        "s-YYYYYYYY"
    ]
}
```

**3. To add a Streaming step with multiple files to a cluster (JSON only)**

- JSON (multiplefiles.json):

```
[
  {
     "Name": "JSON Streaming Step",
     "Type": "STREAMING",
     "ActionOnFailure": "CONTINUE",
     "Args": [
         "-files",
         "s3://amzn-s3-demo-bucket/mapper.py,s3://amzn-s3-demo-bucket/reducer.py",
         "-mapper",
         "mapper.py",
         "-reducer",
         "reducer.py",
         "-input",
         "s3://amzn-s3-demo-bucket/input",
         "-output",
         "s3://amzn-s3-demo-bucket/output"]
  }
]
```
- Command:

```
aws emr add-steps --cluster-id j-XXXXXXXX  --steps file://./multiplefiles.json
```
- Required parameters:

```
Type, Args
```
- Optional parameters:

```
Name, ActionOnFailure
```
- Output:

```
{
    "StepIds":[
        "s-XXXXXXXX",
    ]
}
```

**4. To add Hive steps to a cluster**

- Command:

```
aws emr add-steps --cluster-id j-XXXXXXXX --steps Type=HIVE,Name='Hive program',ActionOnFailure=CONTINUE,Args=[-f,s3://amzn-s3-demo-bucket/myhivescript.q,-d,INPUT=s3://amzn-s3-demo-bucket/myhiveinput,-d,OUTPUT=s3://amzn-s3-demo-bucket/myhiveoutput,arg1,arg2] Type=HIVE,Name='Hive steps',ActionOnFailure=TERMINATE_CLUSTER,Args=[-f,s3://elasticmapreduce/samples/hive-ads/libs/model-build.q,-d,INPUT=s3://elasticmapreduce/samples/hive-ads/tables,-d,OUTPUT=s3://amzn-s3-demo-bucket/hive-ads/output/2014-04-18/11-07-32,-d,LIBS=s3://elasticmapreduce/samples/hive-ads/libs]
```
- Required parameters:

```
Type, Args
```
- Optional parameters:

```
Name, ActionOnFailure
```
- Output:

```
{
    "StepIds":[
        "s-XXXXXXXX",
        "s-YYYYYYYY"
    ]
}
```

**5. To add Pig steps to a cluster**

- Command:

```
aws emr add-steps --cluster-id j-XXXXXXXX --steps Type=PIG,Name='Pig program',ActionOnFailure=CONTINUE,Args=[-f,s3://amzn-s3-demo-bucket/mypigscript.pig,-p,INPUT=s3://amzn-s3-demo-bucket/mypiginput,-p,OUTPUT=s3://amzn-s3-demo-bucket/mypigoutput,arg1,arg2] Type=PIG,Name='Pig program',Args=[-f,s3://elasticmapreduce/samples/pig-apache/do-reports2.pig,-p,INPUT=s3://elasticmapreduce/samples/pig-apache/input,-p,OUTPUT=s3://amzn-s3-demo-bucket/pig-apache/output,arg1,arg2]
```
- Required parameters:

```
Type, Args
```
- Optional parameters:

```
Name, ActionOnFailure
```
- Output:

```
{
    "StepIds":[
        "s-XXXXXXXX",
        "s-YYYYYYYY"
    ]
}
```

**6. To add Impala steps to a cluster**

- Command:

```
aws emr add-steps --cluster-id j-XXXXXXXX --steps Type=IMPALA,Name='Impala program',ActionOnFailure=CONTINUE,Args=--impala-script,s3://myimpala/input,--console-output-path,s3://myimpala/output
```
- Required parameters:

```
Type, Args
```
- Optional parameters:

```
Name, ActionOnFailure
```
- Output:

```
{
    "StepIds":[
        "s-XXXXXXXX",
        "s-YYYYYYYY"
    ]
}
```