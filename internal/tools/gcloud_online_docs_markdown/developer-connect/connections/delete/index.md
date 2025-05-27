# gcloud developer-connect connections delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/delete](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/delete)*

**NAME**

: **gcloud developer-connect connections delete - delete a single connection**

**SYNOPSIS**

: **`gcloud developer-connect connections delete` (`[CONNECTION](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/delete#CONNECTION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/delete#--async)`] [`[--etag](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/delete#--etag)`=`ETAG`] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/delete#--request-id)`=`REQUEST_ID`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/delete#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a single connection.

**EXAMPLES**

: To delete a connection `my-comection` in location
`us-central1` run:

```
gcloud developer-connect connections delete my-connection --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Connection resource - Name of the resource The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `connection` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CONNECTION`**:
ID of the connection or fully qualified identifier for the connection.
To set the `connection` attribute:

- provide the argument `connection` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location id of the connection resource.
To set the `location` attribute:

- provide the argument `connection` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--etag**:
The current etag of the Connection. If an etag is provided and does not match
the current etag of the Connection, deletion will be blocked and an ABORTED
error will be returned.

**--request-id**:
An optional request ID to identify requests. Specify a unique request ID so that
if you must retry your request, the server will know to ignore the request if it
has already been completed. The server will guarantee that for at least 60
minutes after the first request.
For example, consider a situation where you make an initial request and the
request times out. If you make the request again with the same request ID, the
server can check if original operation with the same request ID was received,
and if so, will ignore the second request. This prevents clients from
accidentally creating duplicate commitments.
The request ID must be a valid UUID with the exception that zero UUID is not
supported (00000000-0000-0000-0000-000000000000).

**--validate-only**:
If set, validate the request, but do not actually post it.

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

: This command uses the `developerconnect/v1` API. The full
documentation for this API can be found at: [http://cloud.google.com/developer-connect/docs/overview](http://cloud.google.com/developer-connect/docs/overview)

**NOTES**

: These variants are also available:

```
gcloud alpha developer-connect connections delete
```

```
gcloud beta developer-connect connections delete
```