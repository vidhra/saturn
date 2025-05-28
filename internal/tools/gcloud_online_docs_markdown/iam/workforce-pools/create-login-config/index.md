# gcloud iam workforce-pools create-login-config  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-login-config](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-login-config)*

**NAME**

: **gcloud iam workforce-pools create-login-config - create a login configuration file to enable sign-in via a web-based authorization flow using Workforce Identity Federation**

**SYNOPSIS**

: **`gcloud iam workforce-pools create-login-config` `[AUDIENCE](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-login-config#AUDIENCE)` `[--output-file](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-login-config#--output-file)`=`OUTPUT_FILE` [`[--activate](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-login-config#--activate)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-login-config#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command creates a configuration file to enable browser based third-party
sign in with Workforce Identity Federation through `gcloud auth login
--login-config=/path/to/config.json`.

**EXAMPLES**

: To create a login configuration for your project, run:

```
gcloud iam workforce-pools create-login-config locations/global/workforcePools/$WORKFORCE_POOL_ID/providers/$PROVIDER_ID --output-file=login-config.json
```

**POSITIONAL ARGUMENTS**

: **`AUDIENCE`**:
Workforce pool provider resource name.

**REQUIRED FLAGS**

: **--output-file**:
Location to store the generated login configuration file.

**OPTIONAL FLAGS**

: **--activate**:
Sets the property `auth/login_config_file` to the created login
configuration file. Calling `[gcloud auth login](https://cloud.google.com/sdk/gcloud/reference/auth/login)` will
automatically use this login configuration unless it is explicitly unset.

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
gcloud alpha iam workforce-pools create-login-config
```

```
gcloud beta iam workforce-pools create-login-config
```