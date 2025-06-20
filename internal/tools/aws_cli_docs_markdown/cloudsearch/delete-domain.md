# delete-domainÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/delete-domain.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/delete-domain.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudsearch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/index.html#cli-aws-cloudsearch) ]

# delete-domain

## Description

Permanently deletes a search domain and all of its data. Once a domain has been deleted, it cannot be recovered. For more information, see [Deleting a Search Domain](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/deleting-domains.html) in the *Amazon CloudSearch Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudsearch-2013-01-01/DeleteDomain)

## Synopsis

```
delete-domain
--domain-name <value>
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

`--domain-name` (string)

The name of the domain you want to permanently delete.

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

DomainStatus -> (structure)

The current status of the search domain.

DomainId -> (string)

An internally generated unique identifier for a domain.

DomainName -> (string)

A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

ARN -> (string)

The Amazon Resource Name (ARN) of the search domain. See [Identifiers for IAM Entities](http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html) in *Using AWS Identity and Access Management* for more information.

Created -> (boolean)

True if the search domain is created. It can take several minutes to initialize a domain when  CreateDomain is called. Newly created search domains are returned from  DescribeDomains with a false value for Created until domain creation is complete.

Deleted -> (boolean)

True if the search domain has been deleted. The system must clean up resources dedicated to the search domain when  DeleteDomain is called. Newly deleted search domains are returned from  DescribeDomains with a true value for IsDeleted for several minutes until resource cleanup is complete.

DocService -> (structure)

The service endpoint for updating documents in a search domain.

Endpoint -> (string)

The endpoint to which service requests can be submitted. For example, `search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com` or `doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com` .

SearchService -> (structure)

The service endpoint for requesting search results from a search domain.

Endpoint -> (string)

The endpoint to which service requests can be submitted. For example, `search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com` or `doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.cloudsearch.amazonaws.com` .

RequiresIndexDocuments -> (boolean)

True if  IndexDocuments needs to be called to activate the current domain configuration.

Processing -> (boolean)

True if processing is being done to activate the current domain configuration.

SearchInstanceType -> (string)

The instance type that is being used to process search requests.

SearchPartitionCount -> (integer)

The number of partitions across which the search index is spread.

SearchInstanceCount -> (integer)

The number of search instances that are available to process search requests.

Limits -> (structure)

MaximumReplicationCount -> (integer)

MaximumPartitionCount -> (integer)