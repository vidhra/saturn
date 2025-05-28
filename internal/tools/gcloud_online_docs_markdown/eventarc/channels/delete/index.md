# gcloud eventarc channels delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/eventarc/channels/delete](https://cloud.google.com/sdk/gcloud/reference/eventarc/channels/delete)*

**NAME**

: **gcloud eventarc channels delete - delete an Eventarc channel**

**SYNOPSIS**

: **`gcloud eventarc channels delete` (`[CHANNEL](https://cloud.google.com/sdk/gcloud/reference/eventarc/channels/delete#CHANNEL)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/eventarc/channels/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/eventarc/channels/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/eventarc/channels/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete an Eventarc channel.

**EXAMPLES**

: To delete the channel `my-channel` in location
`us-central1`, run:

```
gcloud eventarc channels delete my-channel --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Channel resource - Channel to delete. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `channel` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CHANNEL`**:
ID of the channel or fully qualified identifier for the channel.
To set the `channel` attribute:

- provide the argument `channel` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location for the Eventarc channel, which should be either
``global`` or one of the supported regions.
Alternatively, set the [eventarc/location] property.
To set the `location` attribute:

- provide the argument `channel` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `eventarc/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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