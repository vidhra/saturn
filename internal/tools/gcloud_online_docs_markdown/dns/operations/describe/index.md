# gcloud dns operations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/operations/describe](https://cloud.google.com/sdk/gcloud/reference/dns/operations/describe)*

**NAME**

: **gcloud dns operations describe - describe an operation**

**SYNOPSIS**

: **`gcloud dns operations describe` `[OPERATION_ID](https://cloud.google.com/sdk/gcloud/reference/dns/operations/describe#OPERATION_ID)` `[--zone](https://cloud.google.com/sdk/gcloud/reference/dns/operations/describe#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/dns/operations/describe#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/dns/operations/describe#ZONE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/operations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command displays the details of a single managed-zone operation.

**EXAMPLES**

: To describe a managed-zone operation:

```
gcloud dns operations describe 1234 --zone=my_zone
```

**POSITIONAL ARGUMENTS**

: **`OPERATION_ID`**:
The id of the operation to display.

**REQUIRED FLAGS**

: **--zone**:
Name of zone to get operations from.

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
gcloud alpha dns operations describe
```

```
gcloud beta dns operations describe
```