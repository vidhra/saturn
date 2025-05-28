# gcloud ids endpoints delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ids/endpoints/delete](https://cloud.google.com/sdk/gcloud/reference/ids/endpoints/delete)*

**NAME**

: **gcloud ids endpoints delete - delete a Cloud IDS endpoint**

**SYNOPSIS**

: **`gcloud ids endpoints delete` (`[ENDPOINT](https://cloud.google.com/sdk/gcloud/reference/ids/endpoints/delete#ENDPOINT)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/ids/endpoints/delete#--zone)`=`ZONE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/ids/endpoints/delete#--async)`] [`[--max-wait](https://cloud.google.com/sdk/gcloud/reference/ids/endpoints/delete#--max-wait)`=`MAX_WAIT`; default="60m"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ids/endpoints/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Cloud IDS endpoint.

**EXAMPLES**

: To delete an endpoint called `my-ep` in project
`my-project` and zone `us-central1-a`, run:

```
gcloud ids endpoints delete my-ep --project=my-project --zone=us-central1-a
```

OR

```
gcloud ids endpoints delete projects/myproject/locations/us-central1-a/endpoints/my-ep
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
gcloud alpha ids endpoints delete
```

```
gcloud beta ids endpoints delete
```