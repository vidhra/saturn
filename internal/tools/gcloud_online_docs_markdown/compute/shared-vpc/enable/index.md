# gcloud compute shared-vpc enable  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/enable](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/enable)*

**NAME**

: **gcloud compute shared-vpc enable - enable the given project as a shared VPC host**

**SYNOPSIS**

: **`gcloud compute shared-vpc enable` `[PROJECT_ID](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/enable#PROJECT_ID)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/enable#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: That is, after running this command, one `can` enable another project
to use the VPC networks shared by this project.

**EXAMPLES**

: To enable the project `myproject` as a shared VPC host, run:

```
gcloud compute shared-vpc enable myproject
```

**POSITIONAL ARGUMENTS**

: **`PROJECT_ID`**:
ID for the project to enable as a shared VPC host

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
gcloud alpha compute shared-vpc enable
```

```
gcloud beta compute shared-vpc enable
```