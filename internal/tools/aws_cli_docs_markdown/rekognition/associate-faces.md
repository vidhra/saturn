# associate-facesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/associate-faces.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/associate-faces.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# associate-faces

## Description

Associates one or more faces with an existing UserID. Takes an array of `FaceIds` . Each `FaceId` that are present in the `FaceIds` list is associated with the provided UserID. The maximum number of total `FaceIds` per UserID is 100.

The `UserMatchThreshold` parameter specifies the minimum user match confidence required for the face to be associated with a UserID that has at least one `FaceID` already associated. This ensures that the `FaceIds` are associated with the right UserID. The value ranges from 0-100 and default value is 75.

If successful, an array of `AssociatedFace` objects containing the associated `FaceIds` is returned. If a given face is already associated with the given `UserID` , it will be ignored and will not be returned in the response. If a given face is already associated to a different `UserID` , isnât found in the collection, doesnât meet the `UserMatchThreshold` , or there are already 100 faces associated with the `UserID` , it will be returned as part of an array of `UnsuccessfulFaceAssociations.`

The `UserStatus` reflects the status of an operation which updates a UserID representation with a list of given faces. The `UserStatus` can be:

- ACTIVE - All associations or disassociations of FaceID(s) for a UserID are complete.
- CREATED - A UserID has been created, but has no FaceID(s) associated with it.
- UPDATING - A UserID is being updated and there are current associations or disassociations of FaceID(s) taking place.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/AssociateFaces)

## Synopsis

```
associate-faces
--collection-id <value>
--user-id <value>
--face-ids <value>
[--user-match-threshold <value>]
[--client-request-token <value>]
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

The ID of an existing collection containing the UserID.

`--user-id` (string)

The ID for the existing UserID.

`--face-ids` (list)

An array of FaceIDs to associate with the UserID.

(string)

Syntax:

```
"string" "string" ...
```

`--user-match-threshold` (float)

An optional value specifying the minimum confidence in the UserID match to return. The default value is 75.

`--client-request-token` (string)

Idempotent token used to identify the request to `AssociateFaces` . If you use the same token with multiple `AssociateFaces` requests, the same response is returned. Use ClientRequestToken to prevent the same request from being processed more than once.

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

AssociatedFaces -> (list)

An array of AssociatedFace objects containing FaceIDs that have been successfully associated with the UserID. Returned if the AssociateFaces action is successful.

(structure)

Provides face metadata for the faces that are associated to a specific UserID.

FaceId -> (string)

Unique identifier assigned to the face.

UnsuccessfulFaceAssociations -> (list)

An array of UnsuccessfulAssociation objects containing FaceIDs that are not successfully associated along with the reasons. Returned if the AssociateFaces action is successful.

(structure)

Contains metadata like FaceId, UserID, and Reasons, for a face that was unsuccessfully associated.

FaceId -> (string)

A unique identifier assigned to the face.

UserId -> (string)

A provided ID for the UserID. Unique within the collection.

Confidence -> (float)

Match confidence with the UserID, provides information regarding if a face association was unsuccessful because it didnât meet UserMatchThreshold.

Reasons -> (list)

The reason why the association was unsuccessful.

(string)

UserStatus -> (string)

The status of an update made to a UserID. Reflects if the UserID has been updated for every requested change.