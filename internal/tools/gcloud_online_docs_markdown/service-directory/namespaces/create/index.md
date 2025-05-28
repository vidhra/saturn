# gcloud service-directory namespaces create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/service-directory/namespaces/create](https://cloud.google.com/sdk/gcloud/reference/service-directory/namespaces/create)*

**NAME**

: **gcloud service-directory namespaces create - creates a namespace**

**SYNOPSIS**

: **`gcloud service-directory namespaces create` (`[NAMESPACE](https://cloud.google.com/sdk/gcloud/reference/service-directory/namespaces/create#NAMESPACE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/service-directory/namespaces/create#--location)`=`LOCATION`) [`[--labels](https://cloud.google.com/sdk/gcloud/reference/service-directory/namespaces/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/service-directory/namespaces/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a namespace.

**EXAMPLES**

: To create a Service Directory namespace, run:

```
gcloud service-directory namespaces create my-namespace --location=us-east1 --labels=a=b,c=d
```

**POSITIONAL ARGUMENTS**

: **Namespace resource - The Service Directory namespace to create. The namespace id
must be 1-63 characters long and match the regular expression
`[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?` which means the first character
must be a lowercase letter, and all following characters must be a dash,
lowercase letter, or digit, except the last character, which cannot be a dash.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `namespace` on the command line with a fully
specified name;
- set the property `core/project`.

This must be specified.

**`NAMESPACE`**:
ID of the namespace or fully qualified identifier for the namespace.
To set the `namespace` attribute:

- provide the argument `namespace` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The name of the region for the namespace.
To set the `location` attribute:

- provide the argument `namespace` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--labels**:
Resource labels associated with the namespace.

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

: These variants are also available:

```
gcloud alpha service-directory namespaces create
```

```
gcloud beta service-directory namespaces create
```