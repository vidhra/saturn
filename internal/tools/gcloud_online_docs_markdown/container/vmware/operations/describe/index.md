# gcloud container vmware operations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/vmware/operations/describe](https://cloud.google.com/sdk/gcloud/reference/container/vmware/operations/describe)*

**NAME**

: **gcloud container vmware operations describe - describe an operation**

**SYNOPSIS**

: **`gcloud container vmware operations describe` (`[OPERATION_ID](https://cloud.google.com/sdk/gcloud/reference/container/vmware/operations/describe#OPERATION_ID)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/vmware/operations/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/vmware/operations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe an operation.

**EXAMPLES**

: To describe an operation in location
``us-west1``, run:

```
gcloud container vmware operations describe OPERATION_ID --location=us-west1
```

**POSITIONAL ARGUMENTS**

: **Operation resource - operation to describe. The arguments in this group can be
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
- set the property `container_vmware/location`.**

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
gcloud alpha container vmware operations describe
```

```
gcloud beta container vmware operations describe
```