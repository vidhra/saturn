# gcloud alpha builds enterprise-config gitlab update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/update](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/update)*

**NAME**

: **gcloud alpha builds enterprise-config gitlab update - update a GitLab Enterprise config for use by Cloud Build**

**SYNOPSIS**

: **`gcloud alpha builds enterprise-config gitlab update` (`[CONFIG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/update#CONFIG)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/update#--region)`=`REGION`) [`[--api-access-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/update#--api-access-token-secret-version)`=`API_ACCESS_TOKEN_SECRET_VERSION`] [`[--api-key-secret-version](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/update#--api-key-secret-version)`=`API_KEY_SECRET_VERSION`] [`[--host-uri](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/update#--host-uri)`=`HOST_URI`] [`[--read-access-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/update#--read-access-token-secret-version)`=`READ_ACCESS_TOKEN_SECRET_VERSION`] [`[--service-directory-service](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/update#--service-directory-service)`=`SERVICE_DIRECTORY_SERVICE`] [`[--ssl-ca-file](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/update#--ssl-ca-file)`=`PATH_TO_FILE`] [`[--user-name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/update#--user-name)`=`USER_NAME`] [`[--webhook-secret-secret-version](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/update#--webhook-secret-secret-version)`=`WEBHOOK_SECRET_SECRET_VERSION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/enterprise-config/gitlab/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update a GitLab Enterprise config for use by Cloud Build.

**POSITIONAL ARGUMENTS**

: **GitLabConfig resource - GitLab Enterprise config. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `CONFIG` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CONFIG`**:
ID of the gitLabConfig or fully qualified identifier for the gitLabConfig.
To set the `config` attribute:

- provide the argument `CONFIG` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The Cloud location for the gitLabConfig.
To set the `region` attribute:

- provide the argument `CONFIG` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `builds/region`.**

**FLAGS**

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

**--read-access-token-secret-version**:
Secret Manager resource containing the read access token. The secret is
specified in resource URL format
projects/{secret_project}/secrets/{secret_name}/versions/{secret_version}.

**--service-directory-service**:
Service Directory service that should be used when making calls to the GitLab
Enterprise instance.
If not specified, calls will be made over the public internet.

**--ssl-ca-file**:
Path to a local file that contains SSL certificate to use for requests to GitLab
Enterprise. The certificate should be in PEM format. Use a full or relative path
to a local file containing the value of ssl_ca_file.

**--user-name**:
The GitLab user name that should be associated with this config.

**--webhook-secret-secret-version**:
Secret Manager resource containing the webhook secret. The secret is specified
in resource URL format
projects/{secret_project}/secrets/{secret_name}/versions/{secret_version}.

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