# gcloud alpha builds enterprise-config bitbucketserver create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/bitbucketserver/create](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/bitbucketserver/create)*

**NAME**

: **gcloud alpha builds enterprise-config bitbucketserver create - create a Bitbucket Server config for use by Cloud Build**

**SYNOPSIS**

: **`gcloud alpha builds enterprise-config bitbucketserver create` `[--admin-access-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/bitbucketserver/create#--admin-access-token-secret-version)`=`ADMIN_ACCESS_TOKEN_SECRET_VERSION` `[--api-key](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/bitbucketserver/create#--api-key)`=`API_KEY` `[--host-uri](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/bitbucketserver/create#--host-uri)`=`HOST_URI` `[--name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/bitbucketserver/create#--name)`=`NAME` `[--read-access-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/bitbucketserver/create#--read-access-token-secret-version)`=`READ_ACCESS_TOKEN_SECRET_VERSION` `[--user-name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/bitbucketserver/create#--user-name)`=`USER_NAME` `[--webhook-secret-secret-version](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/bitbucketserver/create#--webhook-secret-secret-version)`=`WEBHOOK_SECRET_SECRET_VERSION` [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/bitbucketserver/create#--region)`=`REGION`] [`[--ssl-ca-file](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/bitbucketserver/create#--ssl-ca-file)`=`PATH_TO_FILE`] [`[--peered-network](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/bitbucketserver/create#--peered-network)`=`PEERED_NETWORK` `[--peered-network-ip-range](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/bitbucketserver/create#--peered-network-ip-range)`=`PEERED_NETWORK_IP_RANGE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/bitbucketserver/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a Bitbucket Server config for use by Cloud Build.

**REQUIRED FLAGS**

: **--admin-access-token-secret-version**:
Secret Manager resource containing the admin access token. The secret is
specified in resource URL format
projects/{secret_project}/secrets/{secret_name}/versions/{secret_version}.

**--api-key**:
The Cloud Build API key that should be associated with this config.

**--host-uri**:
The host uri of the Bitbucket Server instance.

**--name**:
The config name of the Bitbucket Server connection.

**--read-access-token-secret-version**:
Secret Manager resource containing the read access token. The secret is
specified in resource URL format
projects/{secret_project}/secrets/{secret_name}/versions/{secret_version}.

**--user-name**:
The Bitbucket Server user name that should be associated with this config.

**--webhook-secret-secret-version**:
Secret Manager resource containing the webhook secret. The secret is specified
in resource URL format
projects/{secret_project}/secrets/{secret_name}/versions/{secret_version}.

**OPTIONAL FLAGS**

: **--region**:
The region of the Cloud Build Service to use. Must be set to a supported region
name (e.g. `us-central1`). If unset, `builds/region`,
which is the default region to use when working with Cloud Build resources, is
used. If builds/region is unset, region is set to `global`. Note:
Region must be specified in 2nd gen repo; `global` is not supported.

**--ssl-ca-file**:
Path to a local file that contains SSL certificate to use for requests to
Bitbucket Server. The certificate should be in PEM format. Use a full or
relative path to a local file containing the value of ssl_ca_file.

**--peered-network**:
VPC network that should be used when making calls to the Bitbucket Server
instance.
If not specified, calls will be made over the public internet.

**--peered-network-ip-range**:
IP range within the peered network. This is specified in CIDR notation with a
slash and the subnet prefix size. Examples: `192.168.0.0/24` or
'/29'.

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