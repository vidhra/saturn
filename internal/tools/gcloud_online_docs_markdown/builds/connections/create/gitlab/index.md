# gcloud builds connections create gitlab  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/gitlab](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/gitlab)*

**NAME**

: **gcloud builds connections create gitlab - create a Cloud Build Connection for gitlab.com or GitLab Enterprise**

**SYNOPSIS**

: **`gcloud builds connections create gitlab` (`[CONNECTION](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/gitlab#CONNECTION)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/gitlab#--region)`=`REGION`) `[--authorizer-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/gitlab#--authorizer-token-secret-version)`=`AUTHORIZER_TOKEN_SECRET_VERSION` `[--read-authorizer-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/gitlab#--read-authorizer-token-secret-version)`=`READ_AUTHORIZER_TOKEN_SECRET_VERSION` `[--webhook-secret-secret-version](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/gitlab#--webhook-secret-secret-version)`=`WEBHOOK_SECRET_SECRET_VERSION` [`[--async](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/gitlab#--async)`] [`[--host-uri](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/gitlab#--host-uri)`=`HOST_URI`] [`[--service-directory-service](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/gitlab#--service-directory-service)`=`SERVICE_DIRECTORY_SERVICE` : `[--ssl-ca-file](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/gitlab#--ssl-ca-file)`=`SSL_CA_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/gitlab#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Cloud Build Connection for gitlab.com or GitLab Enterprise.
A gitlab.com or GitLab Enterprise Connection can be created by using a personal
access token with `api` scope permission. A
`read_repository` scoped personal access token will also be required
on gitlab.com or if the self-hosted GitLab server doesn't support project access
token (GitLab Enterprise server version < 13.10).
If the GitLab Enterprise server can only be accessed within a VPC, a Service
Directory service resource can be provided for connecting to it.

**EXAMPLES**

: To create a GitLab connection for gitlab.com, provide all the required
parameters:

```
gcloud builds connections create gitlab my-gitlab-conn --project=myproj --region=us-central1 --read-authorizer-token-secret-version=projects/myproj/secrets/read-pat/versions/1 --authorizer-token-secret-version=projects/myproj/secrets/api-pat/versions/1 --webhook-secret-secret-version=projects/myproj/secrets/whsecret/versions/1
```

To create a GitLab connection for a GitLab server, provide host-uri parameter as
well:

```
gcloud builds connections create gitlab my-gle-conn --host-uri=https://my.gle-server.net --project=myproj --region=us-central1 --authorizer-token-secret-version=projects/myproj/secrets/api-pat/versions/1 --read-authorizer-token-secret-version=projects/myproj/secrets/read-pat/versions/1 --webhook-secret-secret-version=projects/myproj/secrets/whsecret/versions/1
```

To create a GitLab connection for a private GitLab server. provide the
service-directory-service and ssl-ca-file as well:

```
gcloud builds connections create gitlab my-gle-conn --host-uri=https://my.private-gle-server.net --project=myproj --region=us-central1 --service-directory-service=projects/myproj/namespaces/x/services/mysds --ssl-ca-file=mycertificate.crt --authorizer-token-secret-version=projects/myproj/secrets/api-pat/versions/1 --read-authorizer-token-secret-version=projects/myproj/secrets/read-pat/versions/1 --webhook-secret-secret-version=projects/myproj/secrets/whsecret/versions/1
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
Secret containing the api personal access token.

**--read-authorizer-token-secret-version**:
Secret containing the read_api personal access token.

**--webhook-secret-secret-version**:
Secret containing the webhook secret string for validating webhook events sent
by GitLab.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--host-uri**:
URI of the GitLab instance.

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

: These variants are also available:

```
gcloud alpha builds connections create gitlab
```

```
gcloud beta builds connections create gitlab
```