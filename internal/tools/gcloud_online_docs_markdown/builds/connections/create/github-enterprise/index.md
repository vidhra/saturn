# gcloud builds connections create github-enterprise  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/github-enterprise](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/github-enterprise)*

**NAME**

: **gcloud builds connections create github-enterprise - create a Cloud Build Connection of type GitHub Enterprise**

**SYNOPSIS**

: **`gcloud builds connections create github-enterprise` (`[CONNECTION](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/github-enterprise#CONNECTION)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/github-enterprise#--region)`=`REGION`) `[--host-uri](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/github-enterprise#--host-uri)`=`HOST_URI` [`[--async](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/github-enterprise#--async)`] [`[--app-id](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/github-enterprise#--app-id)`=`APP_ID` `[--app-slug](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/github-enterprise#--app-slug)`=`APP_SLUG` `[--private-key-secret-version](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/github-enterprise#--private-key-secret-version)`=`PRIVATE_KEY_SECRET_VERSION` `[--webhook-secret-secret-version](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/github-enterprise#--webhook-secret-secret-version)`=`WEBHOOK_SECRET_SECRET_VERSION` : `[--app-installation-id](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/github-enterprise#--app-installation-id)`=`APP_INSTALLATION_ID`] [`[--service-directory-service](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/github-enterprise#--service-directory-service)`=`SERVICE_DIRECTORY_SERVICE` : `[--ssl-ca-file](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/github-enterprise#--ssl-ca-file)`=`SSL_CA_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/builds/connections/create/github-enterprise#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Cloud Build Connection of type GitHub Enterprise.
Connections for GitHub Enterprise can be created either by following an
intallation process (that requires manual steps in a web browser) or by
providing all the properties of an already-installed application as arguments to
this command.
If the GitHub Enterprise server can only be accessed within a VPC, a Service
Directory service resource can be provided for connecting to it.

**EXAMPLES**

: To create a connection by following the installation process, provide only the
connection name and the host URI. If the server can only be accessed within a
VPC, provide also the Service Directory service resource:

```
gcloud builds connections create github-enterprise my-ghe-conn --project=myproj --region=us-central1 --host-uri=https://my.ghe-server.net --service-directory-service=projects/myproj/namespaces/x/services/mysds
```

The command will print a URL to be opened in a web browser in order create and
install a GitHub App in that server. After following the URL, you can get the
connection's installation state with The
``describe`` command:

```
gcloud alpha builds connections describe my-ghe-conn --region=us-central1
```

If the connection's installation state is not COMPLETE yet, it will provide a
link to continue the installation process. Once the connection is in
installation state COMPLETE, repositories can be added to it (see
``gcloud`` alpha builds repositories create).
--
To create a complete connection (e.g. based on an existing installation),
provide all the parameters:

```
gcloud builds connections create github-enterprise my-ghe-conn --project=myproj --region=us-central1 --app-id=111 --app-slug=gcb-app --service-directory-service=projects/myproj/namespaces/x/services/mysds --private-key-secret-version=projects/myproj/secrets/pk/versions/1 --webhook-secret-secret-version=projects/myproj/secrets/whsecret/versions/1 --app-slug=myapp --app-installation-id=1234
```

Above command creates the connection in installation state COMPLETE, ready for
adding repositories.

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

: **--host-uri**:
URI of the GitHub Enterprise server.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--app-id**

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
gcloud alpha builds connections create github-enterprise
```

```
gcloud beta builds connections create github-enterprise
```