# gcloud alpha builds connections create bitbucket-data-center  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/bitbucket-data-center](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/bitbucket-data-center)*

**NAME**

: **gcloud alpha builds connections create bitbucket-data-center - create a Cloud Build Connection for Bitbucket Data Center**

**SYNOPSIS**

: **`gcloud alpha builds connections create bitbucket-data-center` (`[CONNECTION](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/bitbucket-data-center#CONNECTION)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/bitbucket-data-center#--region)`=`REGION`) `[--authorizer-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/bitbucket-data-center#--authorizer-token-secret-version)`=`AUTHORIZER_TOKEN_SECRET_VERSION` `[--read-authorizer-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/bitbucket-data-center#--read-authorizer-token-secret-version)`=`READ_AUTHORIZER_TOKEN_SECRET_VERSION` `[--webhook-secret-secret-version](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/bitbucket-data-center#--webhook-secret-secret-version)`=`WEBHOOK_SECRET_SECRET_VERSION` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/bitbucket-data-center#--async)`] [`[--host-uri](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/bitbucket-data-center#--host-uri)`=`HOST_URI`] [`[--service-directory-service](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/bitbucket-data-center#--service-directory-service)`=`SERVICE_DIRECTORY_SERVICE` : `[--ssl-ca-file](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/bitbucket-data-center#--ssl-ca-file)`=`SSL_CA_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/bitbucket-data-center#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a Cloud Build Connection for Bitbucket Data Center.
A Bitbucket Data Center Connection can be created by using a personal access
token with `REPO_ADMIN` scope permission. A `REPO_READ`
scoped personal access token will also be required.
If the Bitbucket Data Center can only be accessed within a VPC, a Service
Directory service resource can be provided for connecting to it.

**EXAMPLES**

: To create a Bitbucket Data Center connection, provide all the required
parameters:

```
gcloud alpha builds connections create bitbucket-data-center my-bitbucket-conn --project=myproj --region=us-central1 --host-uri=https://bitbucket-server.net --read-authorizer-token-secret-version=projects/myproj/secrets/read-pat/versions/1 --authorizer-token-secret-version=projects/myproj/secrets/admin-pat/versions/1 --webhook-secret-secret-version=projects/myproj/secrets/whsecret/versions/1
```

To create a Bitbucket Data Center connection for a private Bitbucket Data Center
server. Provide the service-directory-service and ssl-ca-file as well:

```
gcloud alpha builds connections create bitbucket-data-center my-private-bitbucket-conn --host-uri=https://my.private-bitbucket-server.net --project=myproj --region=us-central1 --service-directory-service=projects/myproj/namespaces/x/services/mysds --ssl-ca-file=mycertificate.crt --authorizer-token-secret-version=projects/myproj/secrets/admin-pat/versions/1 --read-authorizer-token-secret-version=projects/myproj/secrets/read-pat/versions/1 --webhook-secret-secret-version=projects/myproj/secrets/whsecret/versions/1
```

**POSITIONAL ARGUMENTS**

: **Connection resource - Connection to create. The arguments in this group can be
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

**REQUIRED FLAGS**

: **--authorizer-token-secret-version**:
Secret containing the REPO_ADMIN personal access token.

**--read-authorizer-token-secret-version**:
Secret containing the REPO_READ personal access token.

**--webhook-secret-secret-version**:
Secret containing the webhook secret string for validating webhook events sent
by Bitbucket Data Center.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--host-uri**:
URI of the Bitbucket Data Center instance.

**--service-directory-service**

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
gcloud builds connections create bitbucket-data-center
```

```
gcloud beta builds connections create bitbucket-data-center
```