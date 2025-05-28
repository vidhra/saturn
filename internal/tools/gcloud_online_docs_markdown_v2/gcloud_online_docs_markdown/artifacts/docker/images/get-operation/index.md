# gcloud artifacts docker images get-operation  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/get-operation](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/get-operation)*

**NAME**

: **gcloud artifacts docker images get-operation - get an On-Demand Scanning operation**

**SYNOPSIS**

: **`gcloud artifacts docker images get-operation` (`[OPERATION](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/get-operation#OPERATION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/get-operation#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/get-operation#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get an On-Demand Scanning operation.

**EXAMPLES**

: The following command gets an On-Demand Scanning operation.

```
gcloud artifacts docker images get-operation projects/my-project/locations/europe/operations/ddf40882-0d55-4214-a619-c1c36df5040c
```

**POSITIONAL ARGUMENTS**

: **Operation resource - The scan operation to get. The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`OPERATION`**:
ID of the operation or fully qualified identifier for the operation.
To set the `operation` attribute:

- provide the argument `operation` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Cloud multi-region.
To set the `location` attribute:

- provide the argument `operation` on the command line with a fully
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

: This command uses the `ondemandscanning/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/container-analysis/docs/on-demand-scanning/](https://cloud.google.com/container-analysis/docs/on-demand-scanning/)

**NOTES**

: This variant is also available:

```
gcloud beta artifacts docker images get-operation
```