# gcloud datastream streams describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/datastream/streams/describe](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/describe)*

**NAME**

: **gcloud datastream streams describe - show details about a Datastream stream resource**

**SYNOPSIS**

: **`gcloud datastream streams describe` (`[STREAM](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/describe#STREAM)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/datastream/streams/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Show details about a Datastream stream resource.

**EXAMPLES**

: To show details about a stream, run:

```
gcloud datastream streams describe my-stream --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Stream resource - The stream you want to get the details of. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `stream` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`STREAM`**:
ID of the stream or fully qualified identifier for the stream.
To set the `stream` attribute:

- provide the argument `stream` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the resources.
To set the `location` attribute:

- provide the argument `stream` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

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

**API REFERENCE**

: This command uses the `datastream/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/datastream/](https://cloud.google.com/datastream/)

**NOTES**

: This variant is also available:

```
gcloud beta datastream streams describe
```