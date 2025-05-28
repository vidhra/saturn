# gcloud compute instance-templates describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/describe](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/describe)*

**NAME**

: **gcloud compute instance-templates describe - describe a virtual machine instance template**

**SYNOPSIS**

: **`gcloud compute instance-templates describe` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/describe#NAME)` [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/describe#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/describe#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instance-templates describe` displays all data
associated with a Google Compute Engine virtual machine instance template.

**EXAMPLES**

: To describe the instance template named 'INSTANCE-TEMPLATE', run:

```
gcloud compute instance-templates describe INSTANCE-TEMPLATE
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the instance template to describe.

**FLAGS**

: **--global**

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
gcloud alpha compute instance-templates describe
```

```
gcloud beta compute instance-templates describe
```