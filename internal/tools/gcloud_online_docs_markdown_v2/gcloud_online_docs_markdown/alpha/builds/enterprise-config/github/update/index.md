# gcloud alpha builds enterprise-config github update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update)*

**NAME**

: **gcloud alpha builds enterprise-config github update - update github enterprise config used by Cloud Build**

**SYNOPSIS**

: **`gcloud alpha builds enterprise-config github update` `[CONFIG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update#CONFIG)` [`[--app-id](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update#--app-id)`=`APP_ID`] [`[--host-uri](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update#--host-uri)`=`HOST_URI`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update#--region)`=`REGION`] [`[--webhook-key](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update#--webhook-key)`=`WEBHOOK_KEY`] [[`[--gcs-bucket](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update#--gcs-bucket)`=`GCS_BUCKET` `[--gcs-object](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update#--gcs-object)`=`GCS_OBJECT` : `[--generation](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update#--generation)`=`GENERATION`]     | [`[--oauth-client-id-name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update#--oauth-client-id-name)`=`OAUTH_CLIENT_ID_NAME` `[--oauth-secret-name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update#--oauth-secret-name)`=`OAUTH_SECRET_NAME` `[--private-key-name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update#--private-key-name)`=`PRIVATE_KEY_NAME` `[--webhook-secret-name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update#--webhook-secret-name)`=`WEBHOOK_SECRET_NAME` : `[--oauth-client-id-version-name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update#--oauth-client-id-version-name)`=`OAUTH_CLIENT_ID_VERSION_NAME` `[--oauth-secret-version-name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update#--oauth-secret-version-name)`=`OAUTH_SECRET_VERSION_NAME` `[--private-key-version-name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update#--private-key-version-name)`=`PRIVATE_KEY_VERSION_NAME` `[--webhook-secret-version-name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update#--webhook-secret-version-name)`=`WEBHOOK_SECRET_VERSION_NAME`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/github/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update github enterprise config used by Cloud Build.

**POSITIONAL ARGUMENTS**

: **`CONFIG`**:
The unique identifier of the GitHub Enterprise Config to be updated.

**FLAGS**

: **--app-id**:
The app id of the GitHub app that should be associated with this config.

**--host-uri**:
The host uri of the GitHub Enterprise Server.

**--region**:
The region of the Cloud Build Service to use. Must be set to a supported region
name (e.g. `us-central1`). If unset, `builds/region`,
which is the default region to use when working with Cloud Build resources, is
used. If builds/region is unset, region is set to `global`. Note:
Region must be specified in 2nd gen repo; `global` is not supported.

**--webhook-key**:
The unique identifier that Cloud Build expects to be set as the value for the
query field `webhook_key` on incoming webhook requests.
If this is not set, Cloud Build will generate one on the user's behalf.

**--gcs-bucket**

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