# gcloud alpha builds enterprise-config gitlab create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/create](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/create)*

**NAME**

: **gcloud alpha builds enterprise-config gitlab create - create a GitLab Enterprise config for use by Cloud Build**

**SYNOPSIS**

: **`gcloud alpha builds enterprise-config gitlab create` `[--api-access-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/create#--api-access-token-secret-version)`=`API_ACCESS_TOKEN_SECRET_VERSION` `[--api-key-secret-version](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/create#--api-key-secret-version)`=`API_KEY_SECRET_VERSION` `[--host-uri](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/create#--host-uri)`=`HOST_URI` `[--name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/create#--name)`=`NAME` `[--read-access-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/create#--read-access-token-secret-version)`=`READ_ACCESS_TOKEN_SECRET_VERSION` `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/create#--region)`=`REGION` `[--user-name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/create#--user-name)`=`USER_NAME` `[--webhook-secret-secret-version](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/create#--webhook-secret-secret-version)`=`WEBHOOK_SECRET_SECRET_VERSION` [`[--service-directory-service](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/create#--service-directory-service)`=`SERVICE_DIRECTORY_SERVICE`] [`[--ssl-ca-file](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/create#--ssl-ca-file)`=`PATH_TO_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a GitLab Enterprise config for use by Cloud Build.

**REQUIRED FLAGS**

: **--api-access-token-secret-version**:
Secret Manager resource containing the API access token. The secret is specified
in resource URL format
projects/{secret_project}/secrets/{secret_name}/versions/{secret_version}.

**--api-key-secret-version**:
Secret Manager resource containing the Cloud Build API key that should be
associated with this config. The secret is specified in resource URL format
projects/{secret_project}/secrets/{secret_name}/versions/{secret_version}.

**--host-uri**:
The host uri of the GitLab Enterprise instance.

**--name**:
The name of the GitLab config.

**--read-access-token-secret-version**:
Secret Manager resource containing the read access token. The secret is
specified in resource URL format
projects/{secret_project}/secrets/{secret_name}/versions/{secret_version}.

**--region**:
The Cloud location of the GitLab config.

**--user-name**:
The GitLab user name that should be associated with this config.

**--webhook-secret-secret-version**:
Secret Manager resource containing the webhook secret. The secret is specified
in resource URL format
projects/{secret_project}/secrets/{secret_name}/versions/{secret_version}.

**OPTIONAL FLAGS**

: **--service-directory-service**:
Service Directory service that should be used when making calls to the GitLab
Enterprise instance.
If not specified, calls will be made over the public internet.

**--ssl-ca-file**:
Path to a local file that contains SSL certificate to use for requests to GitLab
Enterprise. The certificate should be in PEM format. Use a full or relative path
to a local file containing the value of ssl_ca_file.

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