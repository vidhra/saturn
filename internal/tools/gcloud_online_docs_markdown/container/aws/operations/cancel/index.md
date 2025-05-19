# gcloud container aws operations cancel  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/aws/operations/cancel](https://cloud.google.com/sdk/gcloud/reference/container/aws/operations/cancel)*

**NAME**

: **gcloud container aws operations cancel - cancel an operation**

**SYNOPSIS**

: **`gcloud container aws operations cancel` (`[OPERATION_ID](https://cloud.google.com/sdk/gcloud/reference/container/aws/operations/cancel#OPERATION_ID)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/aws/operations/cancel#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/aws/operations/cancel#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Cancel an operation.
This command is deprecated. See [https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement)
for more details.

**EXAMPLES**

: To cancel an operation in location
``us-west1``, run:

```
gcloud container aws operations cancel OPERATION_ID --location=us-west1
```

**POSITIONAL ARGUMENTS**

: **Operation resource - operation to cancel. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `operation_id` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`OPERATION_ID`**:
ID of the operation or fully qualified identifier for the operation.
To set the `name` attribute:

- provide the argument `operation_id` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Google Cloud location for the operation.
To set the `location` attribute:

- provide the argument `operation_id` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `container_aws/location`.**

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

: This variant is also available:

```
gcloud alpha container aws operations cancel
```