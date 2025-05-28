# gcloud ids endpoints update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ids/endpoints/update](https://cloud.google.com/sdk/gcloud/reference/ids/endpoints/update)*

**NAME**

: **gcloud ids endpoints update - update an existing Cloud IDS endpoint**

**SYNOPSIS**

: **`gcloud ids endpoints update` (`[ENDPOINT](https://cloud.google.com/sdk/gcloud/reference/ids/endpoints/update#ENDPOINT)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/ids/endpoints/update#--zone)`=`ZONE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/ids/endpoints/update#--async)`] [`[--max-wait](https://cloud.google.com/sdk/gcloud/reference/ids/endpoints/update#--max-wait)`=`MAX_WAIT`; default="60m"] [`[--threat-exceptions](https://cloud.google.com/sdk/gcloud/reference/ids/endpoints/update#--threat-exceptions)`=[`exc1`,`exc2`,…,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ids/endpoints/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the endpoint for the specified VPC network. Check the progress of
endpoint update by using `gcloud alpha ids endpoints list`.
For more examples, refer to the EXAMPLES section below.

**EXAMPLES**

: To update an endpoint called `my-endpoint`, excluding threat IDs 1000
and 2000, run:

```
gcloud ids endpoints update my-endpoint --threat-exceptions=1000,2000
```

To update an endpoint called `my-endpoint`, clearing the excluded
threat list, run:

```
gcloud ids endpoints update my-endpoint --threat-exceptions=
```

**POSITIONAL ARGUMENTS**

: **Endpoint resource - endpoint. The arguments in this group can be used to specify
the attributes of this resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `endpoint` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ENDPOINT`**:
ID of the endpoint or fully qualified identifier for the endpoint.
To set the `endpoint` attribute:

- provide the argument `endpoint` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--zone**:
Zone of the endpoint.
To set the `zone` attribute:

- provide the argument `endpoint` on the command line with a fully
specified name;
- provide the argument `--zone` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--max-wait**:
Time to synchronously wait for the operation to complete, after which the
operation continues asynchronously. Ignored if --no-async isn't specified. See $
[gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on time formats.

**--threat-exceptions**:
List of threat IDs to be excepted from alerting. Passing empty list clears the
exceptions.

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

**NOTES**

: These variants are also available:

```
gcloud alpha ids endpoints update
```

```
gcloud beta ids endpoints update
```