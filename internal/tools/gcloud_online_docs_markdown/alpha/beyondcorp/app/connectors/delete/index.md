# gcloud alpha beyondcorp app connectors delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/connectors/delete](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/connectors/delete)*

**NAME**

: **gcloud alpha beyondcorp app connectors delete - delete a single Connector**

**SYNOPSIS**

: **`gcloud alpha beyondcorp app connectors delete` (`[CONNECTOR](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/connectors/delete#CONNECTOR)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/connectors/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/connectors/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/connectors/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Delete a single Connector.

**EXAMPLES**

: To delete a connector ``my-connector`` run:

```
gcloud alpha beyondcorp app connectors delete my-connector --project={project} --location={location}
```

**POSITIONAL ARGUMENTS**

: **App connector resource - The Beyondcorp connector you want to delete. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `connector` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CONNECTOR`**:
ID of the app connector or fully qualified identifier for the app connector.
To set the `app_connector` attribute:

- provide the argument `connector` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the beyondcorp service.
To set the `location` attribute:

- provide the argument `connector` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

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

: This command uses the `beyondcorp/v1alpha` API. The full
documentation for this API can be found at: [https://cloud.google.com/](https://cloud.google.com/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud beta beyondcorp app connectors delete
```