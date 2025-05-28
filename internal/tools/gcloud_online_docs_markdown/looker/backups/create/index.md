# gcloud looker backups create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/looker/backups/create](https://cloud.google.com/sdk/gcloud/reference/looker/backups/create)*

**NAME**

: **gcloud looker backups create - create a backup of a Looker instance**

**SYNOPSIS**

: **`gcloud looker backups create` `[--instance](https://cloud.google.com/sdk/gcloud/reference/looker/backups/create#--instance)`=`INSTANCE` `[--region](https://cloud.google.com/sdk/gcloud/reference/looker/backups/create#--region)`=`REGION` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/looker/backups/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a backup of a Looker instance.

**EXAMPLES**

: To create a backup of an instance with the name my-looker-instance, in region
us-central1 run:

```
gcloud looker backups create --instance='my-looker-instance' --region='us-central1'
```

**REQUIRED FLAGS**

: **--instance**:
ID of the instance or fully qualified identifier for the instance. To set the
instance attribute:

- provide the argument --instance on the command line.

**--region**:
The name of the Looker region of the instance. Overrides the default
looker/region property value for this command invocation.

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
gcloud alpha looker backups create
```