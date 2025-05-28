# gcloud secrets replication set  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/secrets/replication/set](https://cloud.google.com/sdk/gcloud/reference/secrets/replication/set)*

**NAME**

: **gcloud secrets replication set - set a secret's replication**

**SYNOPSIS**

: **`gcloud secrets replication set` `[SECRET](https://cloud.google.com/sdk/gcloud/reference/secrets/replication/set#SECRET)` `[--replication-policy-file](https://cloud.google.com/sdk/gcloud/reference/secrets/replication/set#--replication-policy-file)`=`REPLICATION-POLICY-FILE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/secrets/replication/set#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Sets the replication policy for the given secret as defined in a JSON or YAML
file. The locations that a Secret is replicated to cannot be changed.

**EXAMPLES**

: To set the replication of a secret named 'my-secret' to the contents of
my-file.json, run:

```
gcloud secrets replication set my-secret --replication-policy-file=my-file.json
```

**POSITIONAL ARGUMENTS**

: **Secret resource - The secret to update. This represents a Cloud resource. (NOTE)
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

: **--replication-policy-file**:
JSON or YAML file to use to read the replication policy. The file must conform
to [https://cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets#replication.Set](https://cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets#replication.Set)
this to "-" to read from stdin.

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
gcloud beta secrets replication set
```