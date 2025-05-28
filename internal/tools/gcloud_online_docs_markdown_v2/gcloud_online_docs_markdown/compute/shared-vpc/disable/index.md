# gcloud compute shared-vpc disable  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/disable](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/disable)*

**NAME**

: **gcloud compute shared-vpc disable - disable the given project as a shared VPC host**

**SYNOPSIS**

: **`gcloud compute shared-vpc disable` `[PROJECT_ID](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/disable#PROJECT_ID)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/disable#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: That is, after running this command, this project will not be able to share VPC
networks to other projects.

**EXAMPLES**

: To disable the project `myproject` as a shared VPC host, run:

```
gcloud compute shared-vpc disable myproject
```

**POSITIONAL ARGUMENTS**

: **`PROJECT_ID`**:
ID for the project to disable as a shared VPC host

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
gcloud alpha compute shared-vpc disable
```

```
gcloud beta compute shared-vpc disable
```