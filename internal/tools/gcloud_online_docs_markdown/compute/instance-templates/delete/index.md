# gcloud compute instance-templates delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/delete](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/delete)*

**NAME**

: **gcloud compute instance-templates delete - delete Compute Engine virtual machine instance templates**

**SYNOPSIS**

: **`gcloud compute instance-templates delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/delete#NAME)` [`[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/delete#NAME)` …] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/delete#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/delete#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instance-templates delete` deletes one or more
Compute Engine virtual machine instance templates.

**EXAMPLES**

: To delete the instance template named 'INSTANCE-TEMPLATE', run:

```
gcloud compute instance-templates delete INSTANCE-TEMPLATE
```

**POSITIONAL ARGUMENTS**

: **`NAME` [`NAME` …]**:
Names of the instance templates to delete.

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
gcloud alpha compute instance-templates delete
```

```
gcloud beta compute instance-templates delete
```