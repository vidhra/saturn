# gcloud alpha builds connections update bitbucket-cloud  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/update/bitbucket-cloud](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/update/bitbucket-cloud)*

**NAME**

: **gcloud alpha builds connections update bitbucket-cloud - update a Cloud Build Connection of type Bitbucket Cloud**

**SYNOPSIS**

: **`gcloud alpha builds connections update bitbucket-cloud` (`[CONNECTION](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/update/bitbucket-cloud#CONNECTION)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/update/bitbucket-cloud#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/update/bitbucket-cloud#--async)`] [`[--authorizer-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/update/bitbucket-cloud#--authorizer-token-secret-version)`=`AUTHORIZER_TOKEN_SECRET_VERSION`] [`[--read-authorizer-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/update/bitbucket-cloud#--read-authorizer-token-secret-version)`=`READ_AUTHORIZER_TOKEN_SECRET_VERSION`] [`[--webhook-secret-secret-version](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/update/bitbucket-cloud#--webhook-secret-secret-version)`=`WEBHOOK_SECRET_SECRET_VERSION`] [`[--workspace](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/update/bitbucket-cloud#--workspace)`=`WORKSPACE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/update/bitbucket-cloud#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update a Cloud Build Connection of type Bitbucket Cloud.

**EXAMPLES**

: To update the workspace, provide the connection name and the workspace name:

```
gcloud alpha builds connections update bitbucket-cloud my-bbc-conn --region=us-west1 --workspace=my-workspace
```

To update the authorization token, provide the connection name and the new
authorization token
```
secret version.
```

```
gcloud alpha builds connections update bitbucket-cloud my-bbc-conn --region=us-west1 --authorizer-token-secret-version=projects/myproj/secrets/admin-pat/versions/1
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

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--authorizer-token-secret-version**:
Secret containing the
`repository_read`,`repository_admin`,
`pullrequest_read`, `webhook` access token. It can be a
repository, project or workspace access token.

**--read-authorizer-token-secret-version**:
Secret containing the `repository_read` access token. It can be a
repository, project or workspace access token.

**--webhook-secret-secret-version**:
Secret containing the webhook secret string for validating webhook events sent
by Bitbucket Cloud.

**--workspace**:
Workspace of the Bitbucket Cloud instance.

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
gcloud builds connections update bitbucket-cloud
```

```
gcloud beta builds connections update bitbucket-cloud
```