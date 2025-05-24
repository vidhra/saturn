# update-keyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/update-key.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/update-key.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [location](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/location/index.html#cli-aws-location) ]

# update-key

## Description

Updates the specified properties of a given API key resource.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/location-2020-11-19/UpdateKey)

## Synopsis

```
update-key
--key-name <value>
[--description <value>]
[--expire-time <value>]
[--no-expiry | --no-no-expiry]
[--force-update | --no-force-update]
[--restrictions <value>]
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

`--key-name` (string)

The name of the API key resource to update.

`--description` (string)

Updates the description for the API key resource.

`--expire-time` (timestamp)

Updates the timestamp for when the API key resource will expire in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ` .

`--no-expiry` | `--no-no-expiry` (boolean)

Whether the API key should expire. Set to `true` to set the API key to have no expiration time.

`--force-update` | `--no-force-update` (boolean)

The boolean flag to be included for updating `ExpireTime` or `Restrictions` details.

Must be set to `true` to update an API key resource that has been used in the past 7 days.

`False` if force update is not preferred

Default value: `False`

`--restrictions` (structure)

Updates the API key restrictions for the API key resource.

AllowActions -> (list)

A list of allowed actions that an API key resource grants permissions to perform. You must have at least one action for each type of resource. For example, if you have a place resource, you must include at least one place action.

The following are valid values for the actions.

- **Map actions**
- `geo:GetMap*` - Allows all actions needed for map rendering.
- **Place actions**
- `geo:SearchPlaceIndexForText` - Allows geocoding.
- `geo:SearchPlaceIndexForPosition` - Allows reverse geocoding.
- `geo:SearchPlaceIndexForSuggestions` - Allows generating suggestions from text.
- `GetPlace` - Allows finding a place by place ID.
- **Route actions**
- `geo:CalculateRoute` - Allows point to point routing.
- `geo:CalculateRouteMatrix` - Allows calculating a matrix of routes.

### Note

You must use these strings exactly. For example, to provide access to map rendering, the only valid action is `geo:GetMap*` as an input to the list. `["geo:GetMap*"]` is valid but `["geo:GetMapTile"]` is not. Similarly, you cannot use `["geo:SearchPlaceIndexFor*"]` - you must list each of the Place actions separately.

(string)

AllowResources -> (list)

A list of allowed resource ARNs that a API key bearer can perform actions on.

- The ARN must be the correct ARN for a map, place, or route ARN. You may include wildcards in the resource-id to match multiple resources of the same type.
- The resources must be in the same `partition` , `region` , and `account-id` as the key that is being created.
- Other than wildcards, you must include the full ARN, including the `arn` , `partition` , `service` , `region` , `account-id` and `resource-id` delimited by colons (:).
- No spaces allowed, even with wildcards. For example, `arn:aws:geo:region:*account-id* :map/ExampleMap*` .

For more information about ARN format, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

(string)

AllowReferers -> (list)

An optional list of allowed HTTP referers for which requests must originate from. Requests using this API key from other domains will not be allowed.

Requirements:

- Contain only alphanumeric characters (AâZ, aâz, 0â9) or any symbols in this list `$\-._+!*`(),;/?:@=&`
- May contain a percent (%) if followed by 2 hexadecimal digits (A-F, a-f, 0-9); this is used for URL encoding purposes.
- May contain wildcard characters question mark (?) and asterisk (*). Question mark (?) will replace any single character (including hexadecimal digits). Asterisk (*) will replace any multiple characters (including multiple hexadecimal digits).
- No spaces allowed. For example, `https://example.com` .

(string)

Shorthand Syntax:

```
AllowActions=string,string,AllowResources=string,string,AllowReferers=string,string
```

JSON Syntax:

```
{
  "AllowActions": ["string", ...],
  "AllowResources": ["string", ...],
  "AllowReferers": ["string", ...]
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

KeyArn -> (string)

The Amazon Resource Name (ARN) for the API key resource. Used when you need to specify a resource across all Amazon Web Services.

- Format example: `arn:aws:geo:region:account-id:key/ExampleKey`

KeyName -> (string)

The name of the API key resource.

UpdateTime -> (timestamp)

The timestamp for when the API key resource was last updated in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ` .