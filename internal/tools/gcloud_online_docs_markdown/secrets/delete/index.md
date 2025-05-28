# gcloud secrets delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/secrets/delete](https://cloud.google.com/sdk/gcloud/reference/secrets/delete)*

**NAME**

: **gcloud secrets delete - delete a secret**

**SYNOPSIS**

: **`gcloud secrets delete` `[SECRET](https://cloud.google.com/sdk/gcloud/reference/secrets/delete#SECRET)` [`[--etag](https://cloud.google.com/sdk/gcloud/reference/secrets/delete#--etag)`=`ETAG`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/secrets/delete#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/secrets/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a secret and destroy all secret versions. This action is irreversible. If
the given secret does not exist, this command will succeed, but the operation
will be a no-op.

**EXAMPLES**

: Delete a secret `my-secret`:

```
gcloud secrets delete my-secret
```

Delete a secret `my-secret` using an etag:

```
gcloud secrets delete my-secret --etag=123
```

**POSITIONAL ARGUMENTS**

: **Secret resource - The secret to delete. This represents a Cloud resource. (NOTE)
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

**FLAGS**

: **--etag**:
Current entity tag (ETag) of the secret. If specified, the secret is deleted
only if the ETag provided matches the current secret's ETag.

**Location resource - The location to delete secret. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
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
gcloud beta secrets delete
```