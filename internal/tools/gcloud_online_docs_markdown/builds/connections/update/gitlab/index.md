# gcloud builds connections update gitlab  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/builds/connections/update/gitlab](https://cloud.google.com/sdk/gcloud/reference/builds/connections/update/gitlab)*

**NAME**

: **gcloud builds connections update gitlab - update a Cloud Build Connection of type gitlab.com or GitLab Enterprise**

**SYNOPSIS**

: **`gcloud builds connections update gitlab` (`[CONNECTION](https://cloud.google.com/sdk/gcloud/reference/builds/connections/update/gitlab#CONNECTION)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/builds/connections/update/gitlab#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/builds/connections/update/gitlab#--async)`] [`[--authorizer-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/builds/connections/update/gitlab#--authorizer-token-secret-version)`=`AUTHORIZER_TOKEN_SECRET_VERSION`] [`[--host-uri](https://cloud.google.com/sdk/gcloud/reference/builds/connections/update/gitlab#--host-uri)`=`HOST_URI`] [`[--read-authorizer-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/builds/connections/update/gitlab#--read-authorizer-token-secret-version)`=`READ_AUTHORIZER_TOKEN_SECRET_VERSION`] [`[--service-directory-service](https://cloud.google.com/sdk/gcloud/reference/builds/connections/update/gitlab#--service-directory-service)`=`SERVICE_DIRECTORY_SERVICE`] [`[--ssl-ca-file](https://cloud.google.com/sdk/gcloud/reference/builds/connections/update/gitlab#--ssl-ca-file)`=`SSL_CA_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/builds/connections/update/gitlab#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Cloud Build Connection of type gitlab.com or GitLab Enterprise.

**EXAMPLES**

: To update the ssl_ca, provide the connection name and the ssl_ca file:

```
gcloud builds connections update gitlab my-gle-conn --region=us-west1 --ssl-ca-file=mycertificate.crt
```

To update the authorization token, provide the connection name and the new
authorization token
```
secret version.
```

```
gcloud builds connections update gitlab my-gle-conn --region=us-west1 --authorizer-token-secret-version=projects/myproj/secrets/api-pat/versions/1
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
Secret containing the api personal access token.

**--host-uri**:
URI of the GitLab instance.

**--read-authorizer-token-secret-version**:
Secret containing the read_repository personal access token. Required for GitLab
Enterprise versions older than 13.10.

**--service-directory-service**:
Service Directory service resource to use for accessing the GitLab Enterprise
Server. Necessary only if the server has no public access from the internet.

**--ssl-ca-file**:
File containing the SSL_CA to be used.

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
gcloud alpha builds connections update gitlab
```

```
gcloud beta builds connections update gitlab
```