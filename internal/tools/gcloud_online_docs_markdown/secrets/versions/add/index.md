# gcloud secrets versions add  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/secrets/versions/add](https://cloud.google.com/sdk/gcloud/reference/secrets/versions/add)*

**NAME**

: **gcloud secrets versions add - create a new version of an existing secret**

**SYNOPSIS**

: **`gcloud secrets versions add` `[SECRET](https://cloud.google.com/sdk/gcloud/reference/secrets/versions/add#SECRET)` `[--data-file](https://cloud.google.com/sdk/gcloud/reference/secrets/versions/add#--data-file)`=`PATH` [`[--location](https://cloud.google.com/sdk/gcloud/reference/secrets/versions/add#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/secrets/versions/add#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new version of an existing secret with the provided data. The command
will return an error if no such secret exists.

**EXAMPLES**

: Create a new version of an existing secret named 'my-secret' with secret data
"s3cr3t":

```
printf "s3cr3t" | gcloud secrets versions add my-secret --data-file=-
```

Create a new version of an existing secret named 'my-secret' with secret data
"s3cr3t" using PowerShell (Note: PowerShell will add a newline to the resulting
secret):

```
Write-Output "s3cr3t" | gcloud secrets versions add my-secret --data-file=-
```

Create a new version of an existing secret named 'my-secret' with secret data
from a file:

```
gcloud secrets versions add my-secret --data-file=/tmp/secret
```

**POSITIONAL ARGUMENTS**

: **Secret resource - The secret to create. This represents a Cloud resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `SECRET` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SECRET`**:
ID of the secret or fully qualified identifier for the secret.
To set the `secret` attribute:

- provide the argument `SECRET` on the command line.**

**REQUIRED FLAGS**

: **--data-file**:
File path from which to read secret data. Set this to "-" to read the secret
data from stdin.

**OPTIONAL FLAGS**

: **Location resource - The location to create secret version. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line.**

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
gcloud beta secrets versions add
```