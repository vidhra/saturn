# gcloud alpha auth application-default set-quota-project  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/auth/application-default/set-quota-project](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/application-default/set-quota-project)*

**NAME**

: **gcloud alpha auth application-default set-quota-project - update or add a quota project in application default credentials (ADC)**

**SYNOPSIS**

: **`gcloud alpha auth application-default set-quota-project` `[QUOTA_PROJECT_ID](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/application-default/set-quota-project#QUOTA_PROJECT_ID)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/application-default/set-quota-project#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` A quota project is a Google Cloud Project that will be used
for billing and quota limits.
Before running this command, an ADC must already be generated using $ [gcloud auth
application-default login](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login). The quota project defined in the ADC will be used
by the Google client libraries. The existing application default credentials
must have the `serviceusage.services.use` permission on the given
project.

**EXAMPLES**

: To update the quota project in application default credentials to
`my-quota-project`, run:

```
gcloud alpha auth application-default set-quota-project my-quota-project
```

**POSITIONAL ARGUMENTS**

: **`QUOTA_PROJECT_ID`**:
Quota project ID to add to application default credentials. If a quota project
already exists, it will be updated.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud auth application-default set-quota-project
```

```
gcloud beta auth application-default set-quota-project
```