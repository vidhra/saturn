# gcloud colab runtimes create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/colab/runtimes/create](https://cloud.google.com/sdk/gcloud/reference/colab/runtimes/create)*

**NAME**

: **gcloud colab runtimes create - create a notebook runtime**

**SYNOPSIS**

: **`gcloud colab runtimes create` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/colab/runtimes/create#--display-name)`=`DISPLAY_NAME` `[--runtime-template](https://cloud.google.com/sdk/gcloud/reference/colab/runtimes/create#--runtime-template)`=`RUNTIME_TEMPLATE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/colab/runtimes/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/colab/runtimes/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/colab/runtimes/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/colab/runtimes/create#--region)`=`REGION`] [`[--runtime-id](https://cloud.google.com/sdk/gcloud/reference/colab/runtimes/create#--runtime-id)`=`RUNTIME_ID`] [`[--runtime-user](https://cloud.google.com/sdk/gcloud/reference/colab/runtimes/create#--runtime-user)`=`RUNTIME_USER`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/colab/runtimes/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a notebook runtime that can be used to run code from your notebook (IPYNB
file).

**EXAMPLES**

: To create a runtime in region 'us-central1' with the display name 'my-runtime'
and template with id 'my-template', run:

```
gcloud colab runtimes create --region=us-central1 --display-name=my-runtime --runtime-template=my-template
```

To create a runtime for user 'USER@DOMAIN.COM', run:

```
gcloud colab runtimes create --runtime-user=USER@DOMAIN.COM --region=us-central1 --display-name=my-runtime --runtime-template=my-template
```

**REQUIRED FLAGS**

: **--display-name**:
The display name of the runtime to create.

**Runtime template resource - Unique name of the runtime template to configure the
runtime with. This was optionally provided by setting --runtime-template-id in
the create runtime-template command, or was system-generated if unspecified.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--runtime-template` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `region` attribute:

- provide the argument `--runtime-template` on the command line with a
fully specified name;
- provide the argument `--region` on the command line;
- set the property `colab/region`.

This must be specified.

**--runtime-template**:
ID of the runtime template or fully qualified identifier for the runtime
template.
To set the `name` attribute:

- provide the argument `--runtime-template` on the command line.**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
The description

**--labels**:
Add labels to identify and group the runtime template.

**Region resource - Cloud region to create runtime. Please see [https://cloud.google.com/colab/docs/locations](https://cloud.google.com/colab/docs/locations)
for a list of supported regions. This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--region` on the command line with a fully
specified name;
- set the property `colab/region` with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--region**:
ID of the region or fully qualified identifier for the region.
To set the `region` attribute:

- provide the argument `--region` on the command line;
- set the property `colab/region`.**

**--runtime-id**:
The id of the runtime to create. If not specified, a random id will be
generated.

**--runtime-user**:
User email for the runtime owner. Runtimes can only be used by the owner. If a
user is not provided, the gcloud user will be assumed to be the owner. The user
cannot be a service account.

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

: This variant is also available:

```
gcloud beta colab runtimes create
```