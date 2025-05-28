# gcloud eventarc channel-connections create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/eventarc/channel-connections/create](https://cloud.google.com/sdk/gcloud/reference/eventarc/channel-connections/create)*

**NAME**

: **gcloud eventarc channel-connections create - create an Eventarc channel connection**

**SYNOPSIS**

: **`gcloud eventarc channel-connections create` (`[CHANNEL_CONNECTION](https://cloud.google.com/sdk/gcloud/reference/eventarc/channel-connections/create#CHANNEL_CONNECTION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/eventarc/channel-connections/create#--location)`=`LOCATION`) `[--activation-token](https://cloud.google.com/sdk/gcloud/reference/eventarc/channel-connections/create#--activation-token)`=`ACTIVATION_TOKEN` `[--channel](https://cloud.google.com/sdk/gcloud/reference/eventarc/channel-connections/create#--channel)`=`CHANNEL` [`[--async](https://cloud.google.com/sdk/gcloud/reference/eventarc/channel-connections/create#--async)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/eventarc/channel-connections/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/eventarc/channel-connections/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create an Eventarc channel connection.

**EXAMPLES**

: To create a new channel connection
``my-channel-connection`` for channel
``my-channel`` with activation token
``channel-activation-token``, run:

```
gcloud eventarc channel-connections create my-channel-connection --channel=my-channel --activation-token=channel-activation-token
```

**POSITIONAL ARGUMENTS**

: **Channel connection resource - Channel connection to create. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `channel_connection` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CHANNEL_CONNECTION`**:
ID of the channel connection or fully qualified identifier for the channel
connection.
To set the `channel-connection` attribute:

- provide the argument `channel_connection` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location for the Eventarc channel connection, which should be either
``global`` or one of the supported regions.
Alternatively, set the [eventarc/location] property.
To set the `location` attribute:

- provide the argument `channel_connection` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `eventarc/location`.**

**REQUIRED FLAGS**

: **--activation-token**:
Activation token for the specified channel.

**--channel**:
Subscriber channel for which to create the channel connection. This argument
should be the full channel name, including project, location and the channel id.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--labels**:
Labels to apply to the channel connection.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.