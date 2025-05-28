# gcloud network-connectivity spokes delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/delete](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/delete)*

**NAME**

: **gcloud network-connectivity spokes delete - delete a spoke**

**SYNOPSIS**

: **`gcloud network-connectivity spokes delete` `[SPOKE](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/delete#SPOKE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/delete#--async)`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/delete#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/delete#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete the specified spoke.

**EXAMPLES**

: To delete a spoke named ``myspoke`` in the
``us-central1`` region, run:

```
gcloud network-connectivity spokes delete myspoke --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Spoke resource - Name of the spoke to delete. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `spoke` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `spoke` on the command line with a fully
specified name;
- provide the argument `--global` on the command line;
- provide the argument `--region` on the command line.

This must be specified.

**`SPOKE`**:
ID of the spoke or fully qualified identifier for the spoke.
To set the `spoke` attribute:

- provide the argument `spoke` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--global**

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

: This command uses the networkconnectivity/v1 API. The full documentation for
this API can be found at: [https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest](https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest)

**NOTES**

: These variants are also available:

```
gcloud alpha network-connectivity spokes delete
```

```
gcloud beta network-connectivity spokes delete
```