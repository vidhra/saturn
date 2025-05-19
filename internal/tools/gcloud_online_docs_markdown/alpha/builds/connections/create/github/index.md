# gcloud alpha builds connections create github  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/github](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/github)*

**NAME**

: **gcloud alpha builds connections create github - create a Cloud Build Connection of type GitHub**

**SYNOPSIS**

: **`gcloud alpha builds connections create github` (`[CONNECTION](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/github#CONNECTION)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/github#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/github#--async)`] [`[--authorizer-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/github#--authorizer-token-secret-version)`=`AUTHORIZER_TOKEN_SECRET_VERSION` : `[--app-installation-id](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/github#--app-installation-id)`=`APP_INSTALLATION_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/create/github#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a Cloud Build Connection of type GitHub (for
github.com).
Connections for github.com can be created either by following an installation
process (that requires manual steps in a web browser) or by providing the
properties of an already-installed application (installation ID and a user
token) as arguments to this command.

**EXAMPLES**

: To create a connection by following the installation process, provide only the
connection name:

```
gcloud alpha builds connections create github myconn --project=myproj --region=us-central1
```

The command will print a URL to be opened in a web browser in order to authorize
Cloud Build (i.e. Cloud Build gets an OAuth token for the github account that
you use). After doing this authorization, you can get the connection's
installation state with the describe command:

```
gcloud alpha builds connections describe myconn
```

The output will include a second link to install the Cloud Build GitHub App.
After doing this, the connection will be in installation state COMPLETE and
repositories can be added to it (see ``gcloud``
alpha builds repositories create).
--
To create a complete connection (e.g. based on an existing user token and
installation), provide both the authorizer secret token and the app installation
id:

```
gcloud alpha builds connections create github myconn --project=myproj --region=us-central1 --authorizer-token-secret-version=projects/myproj/secrets/mytoken/versions/1 --app-installation-id=1234
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--authorizer-token-secret-version**

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
gcloud builds connections create github
```

```
gcloud beta builds connections create github
```