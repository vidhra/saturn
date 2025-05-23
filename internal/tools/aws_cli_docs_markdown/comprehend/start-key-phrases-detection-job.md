# start-key-phrases-detection-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/start-key-phrases-detection-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/start-key-phrases-detection-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [comprehend](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/index.html#cli-aws-comprehend) ]

# start-key-phrases-detection-job

## Description

Starts an asynchronous key phrase detection job for a collection of documents. Use the operation to track the status of a job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StartKeyPhrasesDetectionJob)

## Synopsis

```
start-key-phrases-detection-job
--input-data-config <value>
--output-data-config <value>
--data-access-role-arn <value>
[--job-name <value>]
--language-code <value>
[--client-request-token <value>]
[--volume-kms-key-id <value>]
[--vpc-config <value>]
[--tags <value>]
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

`--input-data-config` (structure)

Specifies the format and location of the input data for the job.

S3Uri -> (string)

The Amazon S3 URI for the input data. The URI must be in same Region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files.

For example, if you use the URI `S3://bucketName/prefix` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.

InputFormat -> (string)

Specifies how the text in an input file should be processed:

- `ONE_DOC_PER_FILE` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers.
- `ONE_DOC_PER_LINE` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.

DocumentReaderConfig -> (structure)

Provides configuration parameters to override the default actions for extracting text from PDF documents and image files.

DocumentReadAction -> (string)

This field defines the Amazon Textract API operation that Amazon Comprehend uses to extract text from PDF files and image files. Enter one of the following values:

- `TEXTRACT_DETECT_DOCUMENT_TEXT` - The Amazon Comprehend service uses the `DetectDocumentText` API operation.
- `TEXTRACT_ANALYZE_DOCUMENT` - The Amazon Comprehend service uses the `AnalyzeDocument` API operation.

DocumentReadMode -> (string)

Determines the text extraction actions for PDF files. Enter one of the following values:

- `SERVICE_DEFAULT` - use the Amazon Comprehend service defaults for PDF files.
- `FORCE_DOCUMENT_READ_ACTION` - Amazon Comprehend uses the Textract API specified by DocumentReadAction for all PDF files, including digital PDF files.

FeatureTypes -> (list)

Specifies the type of Amazon Textract features to apply. If you chose `TEXTRACT_ANALYZE_DOCUMENT` as the read action, you must specify one or both of the following values:

- `TABLES` - Returns additional information about any tables that are detected in the input document.
- `FORMS` - Returns additional information about any forms that are detected in the input document.

(string)

TABLES or FORMS

Shorthand Syntax:

```
S3Uri=string,InputFormat=string,DocumentReaderConfig={DocumentReadAction=string,DocumentReadMode=string,FeatureTypes=[string,string]}
```

JSON Syntax:

```
{
  "S3Uri": "string",
  "InputFormat": "ONE_DOC_PER_FILE"|"ONE_DOC_PER_LINE",
  "DocumentReaderConfig": {
    "DocumentReadAction": "TEXTRACT_DETECT_DOCUMENT_TEXT"|"TEXTRACT_ANALYZE_DOCUMENT",
    "DocumentReadMode": "SERVICE_DEFAULT"|"FORCE_DOCUMENT_READ_ACTION",
    "FeatureTypes": ["TABLES"|"FORMS", ...]
  }
}
```

`--output-data-config` (structure)

Specifies where to send the output files.

S3Uri -> (string)

When you use the `OutputDataConfig` object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same Region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.

When the topic detection job is finished, the service creates an output file in a directory specific to the job. The `S3Uri` field contains the location of the output file, called `output.tar.gz` . It is a compressed archive that contains the ouput of the operation.

For a PII entity detection job, the output file is plain text, not a compressed archive. The output file name is the same as the input file, with `.out` appended at the end.

KmsKeyId -> (string)

ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt the output results from an analysis job. Specify the Key Id of a symmetric key, because you cannot use an asymmetric key for uploading data to S3.

The KmsKeyId can be one of the following formats:

- KMS Key ID: `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- Amazon Resource Name (ARN) of a KMS Key: `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
- KMS Key Alias: `"alias/ExampleAlias"`
- ARN of a KMS Key Alias: `"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"`

Shorthand Syntax:

```
S3Uri=string,KmsKeyId=string
```

JSON Syntax:

```
{
  "S3Uri": "string",
  "KmsKeyId": "string"
}
```

`--data-access-role-arn` (string)

The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data. For more information, see [Role-based permissions](https://docs.aws.amazon.com/comprehend/latest/dg/security_iam_id-based-policy-examples.html#auth-role-permissions) .

`--job-name` (string)

The identifier of the job.

`--language-code` (string)

The language of the input documents. You can specify any of the primary languages supported by Amazon Comprehend. All documents must be in the same language.

Possible values:

- `en`
- `es`
- `fr`
- `de`
- `it`
- `pt`
- `ar`
- `hi`
- `ja`
- `ko`
- `zh`
- `zh-TW`

`--client-request-token` (string)

A unique identifier for the request. If you donât set the client request token, Amazon Comprehend generates one.

`--volume-kms-key-id` (string)

ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:

- KMS Key ID: `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- Amazon Resource Name (ARN) of a KMS Key: `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`

`--vpc-config` (structure)

Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your key phrases detection job. For more information, see [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) .

SecurityGroupIds -> (list)

The ID number for a security group on an instance of your private VPC. Security groups on your VPC function serve as a virtual firewall to control inbound and outbound traffic and provides security for the resources that youâll be accessing on the VPC. This ID number is preceded by âsg-â, for instance: âsg-03b388029b0a285eaâ. For more information, see [Security Groups for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) .

(string)

Subnets -> (list)

The ID for each subnet being used in your private VPC. This subnet is a subset of the a range of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPCâs Region. This ID number is preceded by âsubnet-â, for instance: âsubnet-04ccf456919e69055â. For more information, see [VPCs and Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) .

(string)

Shorthand Syntax:

```
SecurityGroupIds=string,string,Subnets=string,string
```

JSON Syntax:

```
{
  "SecurityGroupIds": ["string", ...],
  "Subnets": ["string", ...]
}
```

`--tags` (list)

Tags to associate with the key phrases detection job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with âSalesâ as the key might be added to a resource to indicate its use by the sales department.

(structure)

A key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with the key-value pair âDepartmentâ:âSalesâ might be added to a resource to indicate its use by a particular department.

Key -> (string)

The initial part of a key-value pair that forms a tag associated with a given resource. For instance, if you want to show which resources are used by which departments, you might use âDepartmentâ as the key portion of the pair, with multiple possible values such as âsales,â âlegal,â and âadministration.â

Value -> (string)

The second part of a key-value pair that forms a tag associated with a given resource. For instance, if you want to show which resources are used by which departments, you might use âDepartmentâ as the initial (key) portion of the pair, with a value of âsalesâ to indicate the sales department.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
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

**To start a key phrases detection job**

The following `start-key-phrases-detection-job` example starts an asynchronous key phrases detection job for all files located at the address specified by
the `--input-data-config` tag. The S3 bucket in this example contains `Sampletext1.txt`, `Sampletext2.txt`, and `Sampletext3.txt`.
When the job is completed, the folder, `output`, is placed in the location specified by the `--output-data-config` tag. The folder contains
the file `output.txt` which contains all the key phrases detected within each text file and the pre-trained modelâs confidence score for each prediction.
The Json output is printed on one line per file, but is formatted here for readability.

```
aws comprehend start-key-phrases-detection-job \
    --job-name keyphrasesanalysistest1 \
    --language-code en \
    --input-data-config "S3Uri=s3://amzn-s3-demo-bucket/" \
    --output-data-config "S3Uri=s3://amzn-s3-demo-destination-bucket/testfolder/" \
    --data-access-role-arn "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role" \
    --language-code en
```

Contents of `Sampletext1.txt`:

```
"Hello Zhang Wei, I am John. Your AnyCompany Financial Services, LLC credit card account 1111-XXXX-1111-XXXX has a minimum payment of $24.53 that is due by July 31st."
```

Contents of `Sampletext2.txt`:

```
"Dear Max, based on your autopay settings for your account Internet.org account, we will withdraw your payment on the due date from your bank account number XXXXXX1111 with the routing number XXXXX0000. "
```

Contents of `Sampletext3.txt`:

```
"Jane, please submit any customer feedback from this weekend to Sunshine Spa, 123 Main St, Anywhere and send comments to Alice at AnySpa@example.com."
```

Output:

```
{
    "JobId": "123456abcdeb0e11022f22a11EXAMPLE",
    "JobArn": "arn:aws:comprehend:us-west-2:111122223333:key-phrases-detection-job/123456abcdeb0e11022f22a11EXAMPLE",
    "JobStatus": "SUBMITTED"
}
```

Contents of `output.txt` with line indents for readibility:

```
{
    "File": "SampleText1.txt",
    "KeyPhrases": [
        {
        "BeginOffset": 6,
        "EndOffset": 15,
        "Score": 0.9748965572679326,
        "Text": "Zhang Wei"
        },
        {
        "BeginOffset": 22,
        "EndOffset": 26,
        "Score": 0.9997344722354619,
        "Text": "John"
        },
        {
        "BeginOffset": 28,
        "EndOffset": 62,
        "Score": 0.9843791074032948,
        "Text": "Your AnyCompany Financial Services"
        },
        {
        "BeginOffset": 64,
        "EndOffset": 107,
        "Score": 0.8976122401721824,
        "Text": "LLC credit card account 1111-XXXX-1111-XXXX"
        },
        {
        "BeginOffset": 112,
        "EndOffset": 129,
        "Score": 0.9999612982629748,
        "Text": "a minimum payment"
        },
        {
        "BeginOffset": 133,
        "EndOffset": 139,
        "Score": 0.99975728947036,
        "Text": "$24.53"
        },
        {
        "BeginOffset": 155,
        "EndOffset": 164,
        "Score": 0.9940866241449973,
        "Text": "July 31st"
        }
    ],
    "Line": 0
    }
    {
    "File": "SampleText2.txt",
    "KeyPhrases": [
        {
        "BeginOffset": 0,
        "EndOffset": 8,
        "Score": 0.9974021100118472,
        "Text": "Dear Max"
        },
        {
        "BeginOffset": 19,
        "EndOffset": 40,
        "Score": 0.9961120519515884,
        "Text": "your autopay settings"
        },
        {
        "BeginOffset": 45,
        "EndOffset": 78,
        "Score": 0.9980620070116009,
        "Text": "your account Internet.org account"
        },
        {
        "BeginOffset": 97,
        "EndOffset": 109,
        "Score": 0.999919660140754,
        "Text": "your payment"
        },
        {
        "BeginOffset": 113,
        "EndOffset": 125,
        "Score": 0.9998370719754205,
        "Text": "the due date"
        },
        {
        "BeginOffset": 131,
        "EndOffset": 166,
        "Score": 0.9955068678502509,
        "Text": "your bank account number XXXXXX1111"
        },
        {
        "BeginOffset": 172,
        "EndOffset": 200,
        "Score": 0.8653433315829526,
        "Text": "the routing number XXXXX0000"
        }
    ],
    "Line": 0
    }
    {
    "File": "SampleText3.txt",
    "KeyPhrases": [
        {
        "BeginOffset": 0,
        "EndOffset": 4,
        "Score": 0.9142947833681668,
        "Text": "Jane"
        },
        {
        "BeginOffset": 20,
        "EndOffset": 41,
        "Score": 0.9984325676596763,
        "Text": "any customer feedback"
        },
        {
        "BeginOffset": 47,
        "EndOffset": 59,
        "Score": 0.9998782448150636,
        "Text": "this weekend"
        },
        {
        "BeginOffset": 63,
        "EndOffset": 75,
        "Score": 0.99866741830757,
        "Text": "Sunshine Spa"
        },
        {
        "BeginOffset": 77,
        "EndOffset": 88,
        "Score": 0.9695803485466054,
        "Text": "123 Main St"
        },
        {
        "BeginOffset": 108,
        "EndOffset": 116,
        "Score": 0.9997065928550928,
        "Text": "comments"
        },
        {
        "BeginOffset": 120,
        "EndOffset": 125,
        "Score": 0.9993466833825161,
        "Text": "Alice"
        },
        {
        "BeginOffset": 129,
        "EndOffset": 144,
        "Score": 0.9654563612885667,
        "Text": "AnySpa@example.com"
        }
    ],
    "Line": 0
}
```

For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html) in the *Amazon Comprehend Developer Guide*.

## Output

JobId -> (string)

The identifier generated for the job. To get the status of a job, use this identifier with the operation.

JobArn -> (string)

The Amazon Resource Name (ARN) of the key phrase detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:

`arn:<partition>:comprehend:<region>:<account-id>:key-phrases-detection-job/<job-id>`

The following is an example job ARN:

`arn:aws:comprehend:us-west-2:111122223333:key-phrases-detection-job/1234abcd12ab34cd56ef1234567890ab`

JobStatus -> (string)

The status of the job.

- SUBMITTED - The job has been received and is queued for processing.
- IN_PROGRESS - Amazon Comprehend is processing the job.
- COMPLETED - The job was successfully completed and the output is available.
- FAILED - The job did not complete. To get details, use the operation.