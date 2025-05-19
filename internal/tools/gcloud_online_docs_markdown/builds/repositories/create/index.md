# gcloud builds repositories create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/builds/repositories/create](https://cloud.google.com/sdk/gcloud/reference/builds/repositories/create)*

**NAME**

: **gcloud builds repositories create - create a Cloud Build repository**

**SYNOPSIS**

: **`gcloud builds repositories create` (`[REPOSITORY](https://cloud.google.com/sdk/gcloud/reference/builds/repositories/create#REPOSITORY)` : `[--connection](https://cloud.google.com/sdk/gcloud/reference/builds/repositories/create#--connection)`=`CONNECTION` `[--region](https://cloud.google.com/sdk/gcloud/reference/builds/repositories/create#--region)`=`REGION`) `[--remote-uri](https://cloud.google.com/sdk/gcloud/reference/builds/repositories/create#--remote-uri)`=`REMOTE_URI` [`[--async](https://cloud.google.com/sdk/gcloud/reference/builds/repositories/create#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/builds/repositories/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Cloud Build repository in a connection.

**EXAMPLES**

: To Create a repository with name ``my-repo`` in
the connection ``my-conn``, run the following
command:

```
gcloud builds repositories create my-repo --remote-uri=https://github.com/octocat/Hello-World.git --connection=my-conn --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Repository resource - Repository to create. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `repository` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`REPOSITORY`**:
ID of the repository or fully qualified identifier for the repository.
To set the `repository` attribute:

- provide the argument `repository` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--connection**:
Connection ID.
To set the `connection` attribute:

- provide the argument `repository` on the command line with a fully
specified name;
- provide the argument `--connection` on the command line.

**--region**:
The Google Cloud region.
To set the `region` attribute:

- provide the argument `repository` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `builds/region`.**

**REQUIRED FLAGS**

: **--remote-uri**:
The remote git clone URL of the repository.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud alpha builds repositories create
```

```
gcloud beta builds repositories create
```