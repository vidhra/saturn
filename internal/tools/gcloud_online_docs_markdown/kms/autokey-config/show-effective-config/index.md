# gcloud kms autokey-config show-effective-config  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/autokey-config/show-effective-config](https://cloud.google.com/sdk/gcloud/reference/kms/autokey-config/show-effective-config)*

**NAME**

: **gcloud kms autokey-config show-effective-config - gets the effective Cloud KMS AutokeyConfig for a given project**

**SYNOPSIS**

: **`gcloud kms autokey-config show-effective-config` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/autokey-config/show-effective-config#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud kms autokey-config show-effective-config can be used to get the effective
Cloud KMS AutokeyConfig for a given project.

**EXAMPLES**

: The following command retrieves the effective Cloud KMS AutokeyConfig for a
given project `my-project`:

```
gcloud kms autokey-config show-effective-config --project=my-project
```

If --project flag is not provided, then the current project will be used.

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
gcloud alpha kms autokey-config show-effective-config
```

```
gcloud beta kms autokey-config show-effective-config
```