# gcloud container azure clients create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/azure/clients/create](https://cloud.google.com/sdk/gcloud/reference/container/azure/clients/create)*

**NAME**

: **gcloud container azure clients create - create an Azure client**

**SYNOPSIS**

: **`gcloud container azure clients create` (`[CLIENT](https://cloud.google.com/sdk/gcloud/reference/container/azure/clients/create#CLIENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/azure/clients/create#--location)`=`LOCATION`) `[--application-id](https://cloud.google.com/sdk/gcloud/reference/container/azure/clients/create#--application-id)`=`APP_ID` `[--tenant-id](https://cloud.google.com/sdk/gcloud/reference/container/azure/clients/create#--tenant-id)`=`TENANT_ID` [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/azure/clients/create#--async)`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/container/azure/clients/create#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/azure/clients/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Create an Azure client.
This command is deprecated. See [https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement)
for more details.

**EXAMPLES**

: To create an Azure client named ``my-client``
in location ``us-west1``, run:

```
gcloud container azure clients create my-client --location=us-west1 --application-id=APP_ID --tenant-id=TENANT_ID
```

**POSITIONAL ARGUMENTS**

: **Client resource - Azure client to create. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `client` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CLIENT`**:
ID of the client or fully qualified identifier for the client.
To set the `client` attribute:

- provide the argument `client` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Google Cloud location for the client.
To set the `location` attribute:

- provide the argument `client` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `container_azure/location`.**

**REQUIRED FLAGS**

: **--application-id**:
Azure Active Directory (AAD) Application/Client ID (GUID).

**--tenant-id**:
Azure Active Directory (AAD) tenant ID (GUID) to associate with the client.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--validate-only**:
Validate the creation of the client, but don't actually perform it.

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
gcloud alpha container azure clients create
```