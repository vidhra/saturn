# gcloud alpha builds connections update github  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/update/github](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/update/github)*

**NAME**

: **gcloud alpha builds connections update github - update a Cloud Build Connection of type GitHub**

**SYNOPSIS**

: **`gcloud alpha builds connections update github` (`[CONNECTION](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/update/github#CONNECTION)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/update/github#--region)`=`REGION`) [`[--app-installation-id](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/update/github#--app-installation-id)`=`APP_INSTALLATION_ID`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/update/github#--async)`] [`[--authorizer-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/update/github#--authorizer-token-secret-version)`=`AUTHORIZER_TOKEN_SECRET_VERSION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/update/github#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update a Cloud Build Connection of type GitHub (for
github.com).

**EXAMPLES**

: To update the authorizer token, provide the connection name and the authorizer
token secret:

```
gcloud alpha builds connections update github myconn --region=us-central1 --authorizer-token-secret-version=projects/myproj/secrets/mytoken/versions/1
```

To update the installation id, provide the connection name and the installation
id of the Cloud Build GitHub app.

```
gcloud alpha builds connections update github myconn --region=us-central1 --app-installation-id=1234
```

**POSITIONAL ARGUMENTS**

: **Connection resource - Connection to update. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `connection` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CONNECTION`**:
ID of the connection or fully qualified identifier for the connection.
To set the `connection` attribute:

- provide the argument `connection` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The Google Cloud region.
To set the `region` attribute:

- provide the argument `connection` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `builds/region`.**

**FLAGS**

: **--app-installation-id**:
Installation ID of the Cloud Build GitHub App.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--authorizer-token-secret-version**:
Secret containing the authorizer user's token.

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

**API REFERENCE**

: This command uses the `cloudbuild/v2` API. The full documentation for
this API can be found at: [https://cloud.google.com/cloud-build/docs/](https://cloud.google.com/cloud-build/docs/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud builds connections update github
```

```
gcloud beta builds connections update github
```