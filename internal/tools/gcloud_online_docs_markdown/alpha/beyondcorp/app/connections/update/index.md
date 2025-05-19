# gcloud alpha beyondcorp app connections update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/connections/update](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/connections/update)*

**NAME**

: **gcloud alpha beyondcorp app connections update - update an existing Beyondcorp application connection**

**SYNOPSIS**

: **`gcloud alpha beyondcorp app connections update` (`[CONNECTION](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/connections/update#CONNECTION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/connections/update#--location)`=`LOCATION`) [`[--application-endpoint](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/connections/update#--application-endpoint)`=`APPLICATION_ENDPOINT`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/connections/update#--async)`] [`[--connectors](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/connections/update#--connectors)`=[`CONNECTORS`,…]] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/connections/update#--display-name)`=`DISPLAY_NAME`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/connections/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/connections/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/connections/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp/app/connections/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update an existing Beyondcorp application connection.

**EXAMPLES**

: To modify the connection ``my-connection`` in
'us-central1' by adding labels 'k0', with value 'value1' and label 'k1' with
value 'value2' and removing labels with key 'k3', run:

```
gcloud alpha beyondcorp app connections update my-connection --location=us-central1 --display-name=new-display-name --connectors={connector1} --application-endpoint=host:port --update-labels=k0=value1,k1=value2 --remove-labels=k3
```

**POSITIONAL ARGUMENTS**

: **App connection resource - The Beyondcorp connection you want to update. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `connection` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CONNECTION`**:
ID of the app connection or fully qualified identifier for the app connection.
To set the `app_connection` attribute:

- provide the argument `connection` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the beyondcorp service.
To set the `location` attribute:

- provide the argument `connection` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--application-endpoint**:
Address of the remote application endpoint for the Beyondcorp Connection in form
of <host>:<port>.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--connectors**:
List of connectors names that are authorised to be associated with this
Connection.

**--display-name**:
An arbitrary user-provided name for the connection. Cannot exceed 64 characters.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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
gcloud beta beyondcorp app connections update
```