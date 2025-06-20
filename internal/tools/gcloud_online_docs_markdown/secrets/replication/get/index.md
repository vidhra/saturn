# gcloud secrets replication get  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/secrets/replication/get](https://cloud.google.com/sdk/gcloud/reference/secrets/replication/get)*

**NAME**

: **gcloud secrets replication get - describe a secret's replication**

**SYNOPSIS**

: **`gcloud secrets replication get` `[SECRET](https://cloud.google.com/sdk/gcloud/reference/secrets/replication/get#SECRET)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/secrets/replication/get#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a secret's replication

**EXAMPLES**

: To describe the replication of a secret named 'my-secret', run:

```
gcloud secrets replication get my-secret
```

**POSITIONAL ARGUMENTS**

: **Secret resource - The secret to describe. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
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
gcloud beta secrets replication get
```