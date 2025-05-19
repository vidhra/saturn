# gcloud alpha builds enterprise-config github create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/create](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/create)*

**NAME**

: **gcloud alpha builds enterprise-config github create - create a GitHub Enterprise Config for use by Cloud Build**

**SYNOPSIS**

: **`gcloud alpha builds enterprise-config github create` `[--app-id](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/create#--app-id)`=`APP_ID` `[--host-uri](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/create#--host-uri)`=`HOST_URI` ([`[--gcs-bucket](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/create#--gcs-bucket)`=`GCS_BUCKET` `[--gcs-object](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/create#--gcs-object)`=`GCS_OBJECT` : `[--generation](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/create#--generation)`=`GENERATION`]     | [`[--oauth-client-id-name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/create#--oauth-client-id-name)`=`OAUTH_CLIENT_ID_NAME` `[--oauth-secret-name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/create#--oauth-secret-name)`=`OAUTH_SECRET_NAME` `[--private-key-name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/create#--private-key-name)`=`PRIVATE_KEY_NAME` `[--webhook-secret-name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/create#--webhook-secret-name)`=`WEBHOOK_SECRET_NAME` : `[--oauth-client-id-version-name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/create#--oauth-client-id-version-name)`=`OAUTH_CLIENT_ID_VERSION_NAME` `[--oauth-secret-version-name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/create#--oauth-secret-version-name)`=`OAUTH_SECRET_VERSION_NAME` `[--private-key-version-name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/create#--private-key-version-name)`=`PRIVATE_KEY_VERSION_NAME` `[--webhook-secret-version-name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/create#--webhook-secret-version-name)`=`WEBHOOK_SECRET_VERSION_NAME`]) [`[--peered-network](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/create#--peered-network)`=`PEERED_NETWORK`] [`[--webhook-key](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/create#--webhook-key)`=`WEBHOOK_KEY`] [`[--name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/create#--name)`=`NAME` `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/create#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a GitHub Enterprise Config for use by Cloud Build.

**REQUIRED FLAGS**

: **--app-id**:
The app id of the GitHub app that should be associated with this config.

**--host-uri**:
The host uri of the GitHub Enterprise Server.

**--gcs-bucket**

**OPTIONAL FLAGS**

: **--peered-network**:
VPC network that should be used when making calls to the GitHub Enterprise
Server.
If not specified, calls will be made over the public internet.

**--webhook-key**:
The unique identifier that Cloud Build expects to be set as the value for the
query field `webhook_key` on incoming webhook requests.
If this is not set, Cloud Build will generate one on the user's behalf.

**--name**:
The name of the GitHub Enterprise config.

**--region**:
The region of the Cloud Build Service to use. Must be set to a supported region
name (e.g. `us-central1`). If unset, `builds/region`,
which is the default region to use when working with Cloud Build resources, is
used. If builds/region is unset, region is set to `global`.

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
allowlist.