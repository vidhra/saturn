# get-findingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-findings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-findings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [macie2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/index.html#cli-aws-macie2) ]

# get-findings

## Description

Retrieves the details of one or more findings.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/macie2-2020-01-01/GetFindings)

## Synopsis

```
get-findings
--finding-ids <value>
[--sort-criteria <value>]
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

`--finding-ids` (list)

An array of strings that lists the unique identifiers for the findings to retrieve. You can specify as many as 50 unique identifiers in this array.

(string)

Syntax:

```
"string" "string" ...
```

`--sort-criteria` (structure)

The criteria for sorting the results of the request.

attributeName -> (string)

The name of the property to sort the results by. Valid values are: count, createdAt, policyDetails.action.apiCallDetails.firstSeen, policyDetails.action.apiCallDetails.lastSeen, resourcesAffected, severity.score, type, and updatedAt.

orderBy -> (string)

The sort order to apply to the results, based on the value for the property specified by the attributeName property. Valid values are: ASC, sort the results in ascending order; and, DESC, sort the results in descending order.

Shorthand Syntax:

```
attributeName=string,orderBy=string
```

JSON Syntax:

```
{
  "attributeName": "string",
  "orderBy": "ASC"|"DESC"
}
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

## Output

findings -> (list)

An array of objects, one for each finding that matches the criteria specified in the request.

(structure)

Provides the details of a finding.

accountId -> (string)

The unique identifier for the Amazon Web Services account that the finding applies to. This is typically the account that owns the affected resource.

archived -> (boolean)

Specifies whether the finding is archived (suppressed).

category -> (string)

The category of the finding. Possible values are: CLASSIFICATION, for a sensitive data finding; and, POLICY, for a policy finding.

classificationDetails -> (structure)

The details of a sensitive data finding. This value is null for a policy finding.

detailedResultsLocation -> (string)

The path to the folder or file in Amazon S3 that contains the corresponding sensitive data discovery result for the finding. If a finding applies to a large archive or compressed file, this value is the path to a folder. Otherwise, this value is the path to a file.

jobArn -> (string)

The Amazon Resource Name (ARN) of the classification job that produced the finding. This value is null if the origin of the finding (originType) is AUTOMATED_SENSITIVE_DATA_DISCOVERY.

jobId -> (string)

The unique identifier for the classification job that produced the finding. This value is null if the origin of the finding (originType) is AUTOMATED_SENSITIVE_DATA_DISCOVERY.

originType -> (string)

Specifies how Amazon Macie found the sensitive data that produced the finding. Possible values are: SENSITIVE_DATA_DISCOVERY_JOB, for a classification job; and, AUTOMATED_SENSITIVE_DATA_DISCOVERY, for automated sensitive data discovery.

result -> (structure)

The status and other details of the finding.

additionalOccurrences -> (boolean)

Specifies whether Amazon Macie detected additional occurrences of sensitive data in the S3 object. A finding includes location data for a maximum of 15 occurrences of sensitive data.

This value can help you determine whether to investigate additional occurrences of sensitive data in an object. You can do this by referring to the corresponding sensitive data discovery result for the finding (classificationDetails.detailedResultsLocation).

customDataIdentifiers -> (structure)

The custom data identifiers that detected the sensitive data and the number of occurrences of the data that they detected.

detections -> (list)

The custom data identifiers that detected the data, and the number of occurrences of the data that each identifier detected.

(structure)

Provides information about a custom data identifier that produced a sensitive data finding, and the sensitive data that it detected for the finding.

arn -> (string)

The unique identifier for the custom data identifier.

count -> (long)

The total number of occurrences of the sensitive data that the custom data identifier detected.

name -> (string)

The name of the custom data identifier.

occurrences -> (structure)

The location of 1-15 occurrences of the sensitive data that the custom data identifier detected. A finding includes location data for a maximum of 15 occurrences of sensitive data.

cells -> (list)

An array of objects, one for each occurrence of sensitive data in a Microsoft Excel workbook, CSV file, or TSV file. This value is null for all other types of files.

Each Cell object specifies a cell or field that contains the sensitive data.

(structure)

Specifies the location of an occurrence of sensitive data in a Microsoft Excel workbook, CSV file, or TSV file.

cellReference -> (string)

The location of the cell, as an absolute cell reference, that contains the sensitive data, for example Sheet2!C5 for cell C5 on Sheet2 in a Microsoft Excel workbook. This value is null for CSV and TSV files.

column -> (long)

The column number of the column that contains the sensitive data. For a Microsoft Excel workbook, this value correlates to the alphabetical character(s) for a column identifier, for example: 1 for column A, 2 for column B, and so on.

columnName -> (string)

The name of the column that contains the sensitive data, if available.

row -> (long)

The row number of the row that contains the sensitive data.

lineRanges -> (list)

An array of objects, one for each occurrence of sensitive data in an email message or a non-binary text file such as an HTML, TXT, or XML file. Each Range object specifies a line or inclusive range of lines that contains the sensitive data, and the position of the data on the specified line or lines.

This value is often null for file types that are supported by Cell, Page, or Record objects. Exceptions are the location of sensitive data in: unstructured sections of an otherwise structured file, such as a comment in a file; a malformed file that Amazon Macie analyzes as plain text; and, a CSV or TSV file that has any column names that contain sensitive data.

(structure)

Specifies the location of an occurrence of sensitive data in an email message or a non-binary text file such as an HTML, TXT, or XML file.

end -> (long)

The number of lines from the beginning of the file to the end of the sensitive data.

start -> (long)

The number of lines from the beginning of the file to the beginning of the sensitive data.

startColumn -> (long)

The number of characters, with spaces and starting from 1, from the beginning of the first line that contains the sensitive data (start) to the beginning of the sensitive data.

offsetRanges -> (list)

Reserved for future use.

(structure)

Specifies the location of an occurrence of sensitive data in an email message or a non-binary text file such as an HTML, TXT, or XML file.

end -> (long)

The number of lines from the beginning of the file to the end of the sensitive data.

start -> (long)

The number of lines from the beginning of the file to the beginning of the sensitive data.

startColumn -> (long)

The number of characters, with spaces and starting from 1, from the beginning of the first line that contains the sensitive data (start) to the beginning of the sensitive data.

pages -> (list)

An array of objects, one for each occurrence of sensitive data in an Adobe Portable Document Format file. This value is null for all other types of files.

Each Page object specifies a page that contains the sensitive data.

(structure)

Specifies the location of an occurrence of sensitive data in an Adobe Portable Document Format file.

lineRange -> (structure)

Reserved for future use.

end -> (long)

The number of lines from the beginning of the file to the end of the sensitive data.

start -> (long)

The number of lines from the beginning of the file to the beginning of the sensitive data.

startColumn -> (long)

The number of characters, with spaces and starting from 1, from the beginning of the first line that contains the sensitive data (start) to the beginning of the sensitive data.

offsetRange -> (structure)

Reserved for future use.

end -> (long)

The number of lines from the beginning of the file to the end of the sensitive data.

start -> (long)

The number of lines from the beginning of the file to the beginning of the sensitive data.

startColumn -> (long)

The number of characters, with spaces and starting from 1, from the beginning of the first line that contains the sensitive data (start) to the beginning of the sensitive data.

pageNumber -> (long)

The page number of the page that contains the sensitive data.

records -> (list)

An array of objects, one for each occurrence of sensitive data in an Apache Avro object container, Apache Parquet file, JSON file, or JSON Lines file. This value is null for all other types of files.

For an Avro object container or Parquet file, each Record object specifies a record index and the path to a field in a record that contains the sensitive data. For a JSON or JSON Lines file, each Record object specifies the path to a field or array that contains the sensitive data. For a JSON Lines file, it also specifies the index of the line that contains the data.

(structure)

Specifies the location of an occurrence of sensitive data in an Apache Avro object container, Apache Parquet file, JSON file, or JSON Lines file.

jsonPath -> (string)

The path, as a JSONPath expression, to the sensitive data. For an Avro object container or Parquet file, this is the path to the field in the record (recordIndex) that contains the data. For a JSON or JSON Lines file, this is the path to the field or array that contains the data. If the data is a value in an array, the path also indicates which value contains the data.

If Amazon Macie detects sensitive data in the name of any element in the path, Macie omits this field. If the name of an element exceeds 240 characters, Macie truncates the name by removing characters from the beginning of the name. If the resulting full path exceeds 250 characters, Macie also truncates the path, starting with the first element in the path, until the path contains 250 or fewer characters.

recordIndex -> (long)

For an Avro object container or Parquet file, the record index, starting from 0, for the record that contains the sensitive data. For a JSON Lines file, the line index, starting from 0, for the line that contains the sensitive data. This value is always 0 for JSON files.

totalCount -> (long)

The total number of occurrences of the data that was detected by the custom data identifiers and produced the finding.

mimeType -> (string)

The type of content, as a MIME type, that the finding applies to. For example, application/gzip, for a GNU Gzip compressed archive file, or application/pdf, for an Adobe Portable Document Format file.

sensitiveData -> (list)

The category, types, and number of occurrences of the sensitive data that produced the finding.

(structure)

Provides information about the category, types, and occurrences of sensitive data that produced a sensitive data finding.

category -> (string)

The category of sensitive data that was detected. For example: CREDENTIALS, for credentials data such as private keys or Amazon Web Services secret access keys; FINANCIAL_INFORMATION, for financial data such as credit card numbers; or, PERSONAL_INFORMATION, for personal health information, such as health insurance identification numbers, or personally identifiable information, such as passport numbers.

detections -> (list)

An array of objects, one for each type of sensitive data that was detected. Each object reports the number of occurrences of a specific type of sensitive data that was detected, and the location of up to 15 of those occurrences.

(structure)

Provides information about a type of sensitive data that was detected by a managed data identifier and produced a sensitive data finding.

count -> (long)

The total number of occurrences of the type of sensitive data that was detected.

occurrences -> (structure)

The location of 1-15 occurrences of the sensitive data that was detected. A finding includes location data for a maximum of 15 occurrences of sensitive data.

cells -> (list)

An array of objects, one for each occurrence of sensitive data in a Microsoft Excel workbook, CSV file, or TSV file. This value is null for all other types of files.

Each Cell object specifies a cell or field that contains the sensitive data.

(structure)

Specifies the location of an occurrence of sensitive data in a Microsoft Excel workbook, CSV file, or TSV file.

cellReference -> (string)

The location of the cell, as an absolute cell reference, that contains the sensitive data, for example Sheet2!C5 for cell C5 on Sheet2 in a Microsoft Excel workbook. This value is null for CSV and TSV files.

column -> (long)

The column number of the column that contains the sensitive data. For a Microsoft Excel workbook, this value correlates to the alphabetical character(s) for a column identifier, for example: 1 for column A, 2 for column B, and so on.

columnName -> (string)

The name of the column that contains the sensitive data, if available.

row -> (long)

The row number of the row that contains the sensitive data.

lineRanges -> (list)

An array of objects, one for each occurrence of sensitive data in an email message or a non-binary text file such as an HTML, TXT, or XML file. Each Range object specifies a line or inclusive range of lines that contains the sensitive data, and the position of the data on the specified line or lines.

This value is often null for file types that are supported by Cell, Page, or Record objects. Exceptions are the location of sensitive data in: unstructured sections of an otherwise structured file, such as a comment in a file; a malformed file that Amazon Macie analyzes as plain text; and, a CSV or TSV file that has any column names that contain sensitive data.

(structure)

Specifies the location of an occurrence of sensitive data in an email message or a non-binary text file such as an HTML, TXT, or XML file.

end -> (long)

The number of lines from the beginning of the file to the end of the sensitive data.

start -> (long)

The number of lines from the beginning of the file to the beginning of the sensitive data.

startColumn -> (long)

The number of characters, with spaces and starting from 1, from the beginning of the first line that contains the sensitive data (start) to the beginning of the sensitive data.

offsetRanges -> (list)

Reserved for future use.

(structure)

Specifies the location of an occurrence of sensitive data in an email message or a non-binary text file such as an HTML, TXT, or XML file.

end -> (long)

The number of lines from the beginning of the file to the end of the sensitive data.

start -> (long)

The number of lines from the beginning of the file to the beginning of the sensitive data.

startColumn -> (long)

The number of characters, with spaces and starting from 1, from the beginning of the first line that contains the sensitive data (start) to the beginning of the sensitive data.

pages -> (list)

An array of objects, one for each occurrence of sensitive data in an Adobe Portable Document Format file. This value is null for all other types of files.

Each Page object specifies a page that contains the sensitive data.

(structure)

Specifies the location of an occurrence of sensitive data in an Adobe Portable Document Format file.

lineRange -> (structure)

Reserved for future use.

end -> (long)

The number of lines from the beginning of the file to the end of the sensitive data.

start -> (long)

The number of lines from the beginning of the file to the beginning of the sensitive data.

startColumn -> (long)

The number of characters, with spaces and starting from 1, from the beginning of the first line that contains the sensitive data (start) to the beginning of the sensitive data.

offsetRange -> (structure)

Reserved for future use.

end -> (long)

The number of lines from the beginning of the file to the end of the sensitive data.

start -> (long)

The number of lines from the beginning of the file to the beginning of the sensitive data.

startColumn -> (long)

The number of characters, with spaces and starting from 1, from the beginning of the first line that contains the sensitive data (start) to the beginning of the sensitive data.

pageNumber -> (long)

The page number of the page that contains the sensitive data.

records -> (list)

An array of objects, one for each occurrence of sensitive data in an Apache Avro object container, Apache Parquet file, JSON file, or JSON Lines file. This value is null for all other types of files.

For an Avro object container or Parquet file, each Record object specifies a record index and the path to a field in a record that contains the sensitive data. For a JSON or JSON Lines file, each Record object specifies the path to a field or array that contains the sensitive data. For a JSON Lines file, it also specifies the index of the line that contains the data.

(structure)

Specifies the location of an occurrence of sensitive data in an Apache Avro object container, Apache Parquet file, JSON file, or JSON Lines file.

jsonPath -> (string)

The path, as a JSONPath expression, to the sensitive data. For an Avro object container or Parquet file, this is the path to the field in the record (recordIndex) that contains the data. For a JSON or JSON Lines file, this is the path to the field or array that contains the data. If the data is a value in an array, the path also indicates which value contains the data.

If Amazon Macie detects sensitive data in the name of any element in the path, Macie omits this field. If the name of an element exceeds 240 characters, Macie truncates the name by removing characters from the beginning of the name. If the resulting full path exceeds 250 characters, Macie also truncates the path, starting with the first element in the path, until the path contains 250 or fewer characters.

recordIndex -> (long)

For an Avro object container or Parquet file, the record index, starting from 0, for the record that contains the sensitive data. For a JSON Lines file, the line index, starting from 0, for the line that contains the sensitive data. This value is always 0 for JSON files.

type -> (string)

The type of sensitive data that was detected. For example, AWS_CREDENTIALS, PHONE_NUMBER, or ADDRESS.

totalCount -> (long)

The total number of occurrences of the sensitive data that was detected.

sizeClassified -> (long)

The total size, in bytes, of the data that the finding applies to.

status -> (structure)

The status of the finding.

code -> (string)

The status of the finding. Possible values are:

- COMPLETE - Amazon Macie successfully completed its analysis of the S3 object that the finding applies to.
- PARTIAL - Macie analyzed only a subset of the data in the S3 object that the finding applies to. For example, the object is an archive file that contains files in an unsupported format.
- SKIPPED - Macie wasnât able to analyze the S3 object that the finding applies to. For example, the object is a file that uses an unsupported format.

reason -> (string)

A brief description of the status of the finding. This value is null if the status (code) of the finding is COMPLETE.

Amazon Macie uses this value to notify you of any errors, warnings, or considerations that might impact your analysis of the finding and the affected S3 object. Possible values are:

- ARCHIVE_CONTAINS_UNPROCESSED_FILES - The object is an archive file and Macie extracted and analyzed only some or none of the files in the archive. To determine which files Macie analyzed, if any, refer to the corresponding sensitive data discovery result for the finding (classificationDetails.detailedResultsLocation).
- ARCHIVE_EXCEEDS_SIZE_LIMIT - The object is an archive file whose total storage size exceeds the size quota for this type of archive.
- ARCHIVE_NESTING_LEVEL_OVER_LIMIT - The object is an archive file whose nested depth exceeds the quota for the maximum number of nested levels that Macie analyzes for this type of archive.
- ARCHIVE_TOTAL_BYTES_EXTRACTED_OVER_LIMIT - The object is an archive file that exceeds the quota for the maximum amount of data that Macie extracts and analyzes for this type of archive.
- ARCHIVE_TOTAL_DOCUMENTS_PROCESSED_OVER_LIMIT - The object is an archive file that contains more than the maximum number of files that Macie extracts and analyzes for this type of archive.
- FILE_EXCEEDS_SIZE_LIMIT - The storage size of the object exceeds the size quota for this type of file.
- INVALID_ENCRYPTION - The object is encrypted using server-side encryption but Macie isnât allowed to use the key. Macie canât decrypt and analyze the object.
- INVALID_KMS_KEY - The object is encrypted with an KMS key that was disabled or is being deleted. Macie canât decrypt and analyze the object.
- INVALID_OBJECT_STATE - The object doesnât use a supported Amazon S3 storage class.
- JSON_NESTING_LEVEL_OVER_LIMIT - The object contains JSON data and the nested depth of the data exceeds the quota for the number of nested levels that Macie analyzes for this type of file.
- MALFORMED_FILE - The object is a malformed or corrupted file. An error occurred when Macie attempted to detect the fileâs type or extract data from the file.
- MALFORMED_OR_FILE_SIZE_EXCEEDS_LIMIT - The object is a Microsoft Office file that is malformed or exceeds the size quota for this type of file. If the file is malformed, an error occurred when Macie attempted to extract data from the file.
- NO_SUCH_BUCKET_AVAILABLE - The object was in a bucket that was deleted shortly before or when Macie attempted to analyze the object.
- OBJECT_VERSION_MISMATCH - The object was changed while Macie was analyzing it.
- OOXML_UNCOMPRESSED_RATIO_EXCEEDS_LIMIT - The object is an Office Open XML file whose compression ratio exceeds the compression quota for this type of file.
- OOXML_UNCOMPRESSED_SIZE_EXCEEDS_LIMIT - The object is an Office Open XML file that exceeds the size quota for this type of file.
- PERMISSION_DENIED - Macie isnât allowed to access the object. The objectâs permissions settings prevent Macie from analyzing the object.
- SOURCE_OBJECT_NO_LONGER_AVAILABLE - The object was deleted shortly before or when Macie attempted to analyze it.
- TIME_CUT_OFF_REACHED - Macie started analyzing the object but additional analysis would exceed the time quota for analyzing an object.
- UNABLE_TO_PARSE_FILE - The object is a file that contains structured data and an error occurred when Macie attempted to parse the data.
- UNSUPPORTED_FILE_TYPE_EXCEPTION - The object is a file that uses an unsupported file or storage format.

For information about quotas, supported storage classes, and supported file and storage formats, see [Quotas](https://docs.aws.amazon.com/macie/latest/user/macie-quotas.html) and [Supported storage classes and formats](https://docs.aws.amazon.com/macie/latest/user/discovery-supported-storage.html) in the *Amazon Macie User Guide* .

count -> (long)

The total number of occurrences of the finding. For sensitive data findings, this value is always 1. All sensitive data findings are considered unique.

createdAt -> (timestamp)

The date and time, in UTC and extended ISO 8601 format, when Amazon Macie created the finding.

description -> (string)

The description of the finding.

id -> (string)

The unique identifier for the finding. This is a random string that Amazon Macie generates and assigns to a finding when it creates the finding.

partition -> (string)

The Amazon Web Services partition that Amazon Macie created the finding in.

policyDetails -> (structure)

The details of a policy finding. This value is null for a sensitive data finding.

action -> (structure)

The action that produced the finding.

actionType -> (string)

The type of action that occurred for the affected resource. This value is typically AWS_API_CALL, which indicates that an entity invoked an API operation for the resource.

apiCallDetails -> (structure)

The invocation details of the API operation that an entity invoked for the affected resource, if the value for the actionType property is AWS_API_CALL.

api -> (string)

The name of the operation that was invoked most recently and produced the finding.

apiServiceName -> (string)

The URL of the Amazon Web Services service that provides the operation, for example: s3.amazonaws.com.

firstSeen -> (timestamp)

The first date and time, in UTC and extended ISO 8601 format, when any operation was invoked and produced the finding.

lastSeen -> (timestamp)

The most recent date and time, in UTC and extended ISO 8601 format, when the specified operation (api) was invoked and produced the finding.

actor -> (structure)

The entity that performed the action that produced the finding.

domainDetails -> (structure)

The domain name of the device that the entity used to perform the action on the affected resource.

domainName -> (string)

The name of the domain.

ipAddressDetails -> (structure)

The IP address and related details about the device that the entity used to perform the action on the affected resource. The details can include information such as the owner and geographic location of the IP address.

ipAddressV4 -> (string)

The Internet Protocol version 4 (IPv4) address of the device.

ipCity -> (structure)

The city that the IP address originated from.

name -> (string)

The name of the city.

ipCountry -> (structure)

The country that the IP address originated from.

code -> (string)

The two-character code, in ISO 3166-1 alpha-2 format, for the country that the IP address originated from. For example, US for the United States.

name -> (string)

The name of the country that the IP address originated from.

ipGeoLocation -> (structure)

The geographic coordinates of the location that the IP address originated from.

lat -> (double)

The latitude coordinate of the location, rounded to four decimal places.

lon -> (double)

The longitude coordinate of the location, rounded to four decimal places.

ipOwner -> (structure)

The registered owner of the IP address.

asn -> (string)

The autonomous system number (ASN) for the autonomous system that included the IP address.

asnOrg -> (string)

The organization identifier thatâs associated with the autonomous system number (ASN) for the autonomous system that included the IP address.

isp -> (string)

The name of the internet service provider (ISP) that owned the IP address.

org -> (string)

The name of the organization that owned the IP address.

userIdentity -> (structure)

The type and other characteristics of the entity that performed the action on the affected resource. This value is null if the action was performed by an anonymous (unauthenticated) entity.

assumedRole -> (structure)

If the action was performed with temporary security credentials that were obtained using the AssumeRole operation of the Security Token Service (STS) API, the identifiers, session context, and other details about the identity.

accessKeyId -> (string)

The Amazon Web Services access key ID that identifies the credentials.

accountId -> (string)

The unique identifier for the Amazon Web Services account that owns the entity that was used to get the credentials.

arn -> (string)

The Amazon Resource Name (ARN) of the entity that was used to get the credentials.

principalId -> (string)

The unique identifier for the entity that was used to get the credentials.

sessionContext -> (structure)

The details of the session that was created for the credentials, including the entity that issued the session.

attributes -> (structure)

The date and time when the credentials were issued, and whether the credentials were authenticated with a multi-factor authentication (MFA) device.

creationDate -> (timestamp)

The date and time, in UTC and ISO 8601 format, when the credentials were issued.

mfaAuthenticated -> (boolean)

Specifies whether the credentials were authenticated with a multi-factor authentication (MFA) device.

sessionIssuer -> (structure)

The source and type of credentials that were issued to the entity.

accountId -> (string)

The unique identifier for the Amazon Web Services account that owns the entity that was used to get the credentials.

arn -> (string)

The Amazon Resource Name (ARN) of the source account, Identity and Access Management (IAM) user, or role that was used to get the credentials.

principalId -> (string)

The unique identifier for the entity that was used to get the credentials.

type -> (string)

The source of the temporary security credentials, such as Root, IAMUser, or Role.

userName -> (string)

The name or alias of the user or role that issued the session. This value is null if the credentials were obtained from a root account that doesnât have an alias.

awsAccount -> (structure)

If the action was performed using the credentials for another Amazon Web Services account, the details of that account.

accountId -> (string)

The unique identifier for the Amazon Web Services account.

principalId -> (string)

The unique identifier for the entity that performed the action.

awsService -> (structure)

If the action was performed by an Amazon Web Services account that belongs to an Amazon Web Services service, the name of the service.

invokedBy -> (string)

The name of the Amazon Web Service that performed the action.

federatedUser -> (structure)

If the action was performed with temporary security credentials that were obtained using the GetFederationToken operation of the Security Token Service (STS) API, the identifiers, session context, and other details about the identity.

accessKeyId -> (string)

The Amazon Web Services access key ID that identifies the credentials.

accountId -> (string)

The unique identifier for the Amazon Web Services account that owns the entity that was used to get the credentials.

arn -> (string)

The Amazon Resource Name (ARN) of the entity that was used to get the credentials.

principalId -> (string)

The unique identifier for the entity that was used to get the credentials.

sessionContext -> (structure)

The details of the session that was created for the credentials, including the entity that issued the session.

attributes -> (structure)

The date and time when the credentials were issued, and whether the credentials were authenticated with a multi-factor authentication (MFA) device.

creationDate -> (timestamp)

The date and time, in UTC and ISO 8601 format, when the credentials were issued.

mfaAuthenticated -> (boolean)

Specifies whether the credentials were authenticated with a multi-factor authentication (MFA) device.

sessionIssuer -> (structure)

The source and type of credentials that were issued to the entity.

accountId -> (string)

The unique identifier for the Amazon Web Services account that owns the entity that was used to get the credentials.

arn -> (string)

The Amazon Resource Name (ARN) of the source account, Identity and Access Management (IAM) user, or role that was used to get the credentials.

principalId -> (string)

The unique identifier for the entity that was used to get the credentials.

type -> (string)

The source of the temporary security credentials, such as Root, IAMUser, or Role.

userName -> (string)

The name or alias of the user or role that issued the session. This value is null if the credentials were obtained from a root account that doesnât have an alias.

iamUser -> (structure)

If the action was performed using the credentials for an Identity and Access Management (IAM) user, the name and other details about the user.

accountId -> (string)

The unique identifier for the Amazon Web Services account thatâs associated with the IAM user who performed the action.

arn -> (string)

The Amazon Resource Name (ARN) of the principal that performed the action. The last section of the ARN contains the name of the user who performed the action.

principalId -> (string)

The unique identifier for the IAM user who performed the action.

userName -> (string)

The username of the IAM user who performed the action.

root -> (structure)

If the action was performed using the credentials for your Amazon Web Services account, the details of your account.

accountId -> (string)

The unique identifier for the Amazon Web Services account.

arn -> (string)

The Amazon Resource Name (ARN) of the principal that performed the action. The last section of the ARN contains the name of the user or role that performed the action.

principalId -> (string)

The unique identifier for the entity that performed the action.

type -> (string)

The type of entity that performed the action.

region -> (string)

The Amazon Web Services Region that Amazon Macie created the finding in.

resourcesAffected -> (structure)

The resources that the finding applies to.

s3Bucket -> (structure)

The details of the S3 bucket that the finding applies to.

allowsUnencryptedObjectUploads -> (string)

Specifies whether the bucket policy for the bucket requires server-side encryption of objects when objects are added to the bucket. Possible values are:

- FALSE - The bucket policy requires server-side encryption of new objects. PutObject requests must include a valid server-side encryption header.
- TRUE - The bucket doesnât have a bucket policy or it has a bucket policy that doesnât require server-side encryption of new objects. If a bucket policy exists, it doesnât require PutObject requests to include a valid server-side encryption header.
- UNKNOWN - Amazon Macie canât determine whether the bucket policy requires server-side encryption of new objects.

Valid server-side encryption headers are: x-amz-server-side-encryption with a value of AES256 or aws:kms, and x-amz-server-side-encryption-customer-algorithm with a value of AES256.

arn -> (string)

The Amazon Resource Name (ARN) of the bucket.

createdAt -> (timestamp)

The date and time, in UTC and extended ISO 8601 format, when the bucket was created. This value can also indicate when changes such as edits to the bucketâs policy were most recently made to the bucket, relative to when the finding was created or last updated.

defaultServerSideEncryption -> (structure)

The default server-side encryption settings for the bucket.

encryptionType -> (string)

The server-side encryption algorithm thatâs used when storing data in the bucket or object. If default encryption settings arenât configured for the bucket or the object isnât encrypted using server-side encryption, this value is NONE.

kmsMasterKeyId -> (string)

The Amazon Resource Name (ARN) or unique identifier (key ID) for the KMS key thatâs used to encrypt data in the bucket or the object. This value is null if an KMS key isnât used to encrypt the data.

name -> (string)

The name of the bucket.

owner -> (structure)

The display name and canonical user ID for the Amazon Web Services account that owns the bucket.

displayName -> (string)

The display name of the account that owns the bucket.

id -> (string)

The canonical user ID for the account that owns the bucket.

publicAccess -> (structure)

The permissions settings that determine whether the bucket is publicly accessible.

effectivePermission -> (string)

Specifies whether the bucket is publicly accessible due to the combination of permissions settings that apply to the bucket. Possible values are:

- NOT_PUBLIC - The bucket isnât publicly accessible.
- PUBLIC - The bucket is publicly accessible.
- UNKNOWN - Amazon Macie canât determine whether the bucket is publicly accessible.

permissionConfiguration -> (structure)

The account-level and bucket-level permissions settings for the bucket.

accountLevelPermissions -> (structure)

The account-level permissions settings that apply to the bucket.

blockPublicAccess -> (structure)

The block public access settings for the Amazon Web Services account that owns the bucket.

blockPublicAcls -> (boolean)

Specifies whether Amazon S3 blocks public access control lists (ACLs) for the bucket and objects in the bucket.

blockPublicPolicy -> (boolean)

Specifies whether Amazon S3 blocks public bucket policies for the bucket.

ignorePublicAcls -> (boolean)

Specifies whether Amazon S3 ignores public ACLs for the bucket and objects in the bucket.

restrictPublicBuckets -> (boolean)

Specifies whether Amazon S3 restricts public bucket policies for the bucket.

bucketLevelPermissions -> (structure)

The bucket-level permissions settings for the bucket.

accessControlList -> (structure)

The permissions settings of the access control list (ACL) for the bucket. This value is null if an ACL hasnât been defined for the bucket.

allowsPublicReadAccess -> (boolean)

Specifies whether the ACL grants the general public with read access permissions for the bucket.

allowsPublicWriteAccess -> (boolean)

Specifies whether the ACL grants the general public with write access permissions for the bucket.

blockPublicAccess -> (structure)

The block public access settings for the bucket.

blockPublicAcls -> (boolean)

Specifies whether Amazon S3 blocks public access control lists (ACLs) for the bucket and objects in the bucket.

blockPublicPolicy -> (boolean)

Specifies whether Amazon S3 blocks public bucket policies for the bucket.

ignorePublicAcls -> (boolean)

Specifies whether Amazon S3 ignores public ACLs for the bucket and objects in the bucket.

restrictPublicBuckets -> (boolean)

Specifies whether Amazon S3 restricts public bucket policies for the bucket.

bucketPolicy -> (structure)

The permissions settings of the bucket policy for the bucket. This value is null if a bucket policy hasnât been defined for the bucket.

allowsPublicReadAccess -> (boolean)

Specifies whether the bucket policy allows the general public to have read access to the bucket.

allowsPublicWriteAccess -> (boolean)

Specifies whether the bucket policy allows the general public to have write access to the bucket.

tags -> (list)

The tags that are associated with the bucket.

(structure)

Provides information about the tags that are associated with an S3 bucket or object. Each tag consists of a required tag key and an associated tag value.

key -> (string)

One part of a key-value pair that comprises a tag. A tag key is a general label that acts as a category for more specific tag values.

value -> (string)

One part of a key-value pair that comprises a tag. A tag value acts as a descriptor for a tag key. A tag value can be an empty string.

s3Object -> (structure)

The details of the S3 object that the finding applies to.

bucketArn -> (string)

The Amazon Resource Name (ARN) of the bucket that contains the object.

eTag -> (string)

The entity tag (ETag) that identifies the affected version of the object. If the object was overwritten or changed after Amazon Macie produced the finding, this value might be different from the current ETag for the object.

extension -> (string)

The file name extension of the object. If the object doesnât have a file name extension, this value is ââ.

key -> (string)

The full name (*key* ) of the object, including the objectâs prefix if applicable.

lastModified -> (timestamp)

The date and time, in UTC and extended ISO 8601 format, when the object was last modified.

path -> (string)

The full path to the affected object, including the name of the affected bucket and the objectâs name (key).

publicAccess -> (boolean)

Specifies whether the object is publicly accessible due to the combination of permissions settings that apply to the object.

serverSideEncryption -> (structure)

The type of server-side encryption that was used to encrypt the object.

encryptionType -> (string)

The server-side encryption algorithm thatâs used when storing data in the bucket or object. If default encryption settings arenât configured for the bucket or the object isnât encrypted using server-side encryption, this value is NONE.

kmsMasterKeyId -> (string)

The Amazon Resource Name (ARN) or unique identifier (key ID) for the KMS key thatâs used to encrypt data in the bucket or the object. This value is null if an KMS key isnât used to encrypt the data.

size -> (long)

The total storage size, in bytes, of the object.

storageClass -> (string)

The storage class of the object.

tags -> (list)

The tags that are associated with the object.

(structure)

Provides information about the tags that are associated with an S3 bucket or object. Each tag consists of a required tag key and an associated tag value.

key -> (string)

One part of a key-value pair that comprises a tag. A tag key is a general label that acts as a category for more specific tag values.

value -> (string)

One part of a key-value pair that comprises a tag. A tag value acts as a descriptor for a tag key. A tag value can be an empty string.

versionId -> (string)

The identifier for the affected version of the object.

sample -> (boolean)

Specifies whether the finding is a sample finding. A *sample finding* is a finding that uses example data to demonstrate what a finding might contain.

schemaVersion -> (string)

The version of the schema that was used to define the data structures in the finding.

severity -> (structure)

The severity level and score for the finding.

description -> (string)

The qualitative representation of the findingâs severity, ranging from Low (least severe) to High (most severe).

score -> (long)

The numerical representation of the findingâs severity, ranging from 1 (least severe) to 3 (most severe).

title -> (string)

The brief description of the finding.

type -> (string)

The type of the finding.

updatedAt -> (timestamp)

The date and time, in UTC and extended ISO 8601 format, when Amazon Macie last updated the finding. For sensitive data findings, this value is the same as the value for the createdAt property. All sensitive data findings are considered new.