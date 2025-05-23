# search-usersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/search-users.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/search-users.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# search-users

## Description

Searches for UserIDs within a collection based on a `FaceId` or `UserId` . This API can be used to find the closest UserID (with a highest similarity) to associate a face. The request must be provided with either `FaceId` or `UserId` . The operation returns an array of UserID that match the `FaceId` or `UserId` , ordered by similarity score with the highest similarity first.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/SearchUsers)

## Synopsis

```
search-users
--collection-id <value>
[--user-id <value>]
[--face-id <value>]
[--user-match-threshold <value>]
[--max-users <value>]
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

`--collection-id` (string)

The ID of an existing collection containing the UserID, used with a UserId or FaceId. If a FaceId is provided, UserId isnât required to be present in the Collection.

`--user-id` (string)

ID for the existing User.

`--face-id` (string)

ID for the existing face.

`--user-match-threshold` (float)

Optional value that specifies the minimum confidence in the matched UserID to return. Default value of 80.

`--max-users` (integer)

Maximum number of identities to return.

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

UserMatches -> (list)

An array of UserMatch objects that matched the input face along with the confidence in the match. Array will be empty if there are no matches.

(structure)

Provides UserID metadata along with the confidence in the match of this UserID with the input face.

Similarity -> (float)

Describes the UserID metadata.

User -> (structure)

Confidence in the match of this UserID with the input face.

UserId -> (string)

A provided ID for the UserID. Unique within the collection.

UserStatus -> (string)

The status of the user matched to a provided FaceID.

FaceModelVersion -> (string)

Version number of the face detection model associated with the input CollectionId.

SearchedFace -> (structure)

Contains the ID of a face that was used to search for matches in a collection.

FaceId -> (string)

Unique identifier assigned to the face.

SearchedUser -> (structure)

Contains the ID of the UserID that was used to search for matches in a collection.

UserId -> (string)

A provided ID for the UserID. Unique within the collection.