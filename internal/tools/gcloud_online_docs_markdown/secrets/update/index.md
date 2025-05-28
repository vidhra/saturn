# gcloud secrets update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/secrets/update](https://cloud.google.com/sdk/gcloud/reference/secrets/update)*

**NAME**

: **gcloud secrets update - update a secret's metadata**

**SYNOPSIS**

: **`gcloud secrets update` `[SECRET](https://cloud.google.com/sdk/gcloud/reference/secrets/update#SECRET)` [`[--etag](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--etag)`=`ETAG`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--location)`=`LOCATION`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--add-topics](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--add-topics)`=[`ADD-TOPICS`,…]     | `[--clear-topics](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--clear-topics)`     | `[--remove-topics](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--remove-topics)`=[`REMOVE-TOPICS`,…]] [`[--clear-annotations](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--clear-annotations)`     | `[--remove-annotations](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--remove-annotations)`=[`KEY`,…]     | `[--update-annotations](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--update-annotations)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--remove-labels)`=[`KEY`,…]] [`[--clear-version-aliases](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--clear-version-aliases)`     | `[--remove-version-aliases](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--remove-version-aliases)`=[`KEY`,…]     | `[--update-version-aliases](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--update-version-aliases)`=[`KEY`=`VALUE`,…]] [`[--expire-time](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--expire-time)`=`EXPIRE-TIME`     | `[--remove-expiration](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--remove-expiration)`     | `[--ttl](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--ttl)`=`TTL`] [`[--next-rotation-time](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--next-rotation-time)`=`NEXT_ROTATION_TIME` `[--remove-next-rotation-time](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--remove-next-rotation-time)` `[--remove-rotation-period](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--remove-rotation-period)` `[--remove-rotation-schedule](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--remove-rotation-schedule)` `[--rotation-period](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--rotation-period)`=`ROTATION_PERIOD`] [`[--regional-kms-key-name](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--regional-kms-key-name)`=`REGIONAL-KMS-KEY-NAME`     | `[--remove-regional-kms-key-name](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--remove-regional-kms-key-name)`] [`[--remove-version-destroy-ttl](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--remove-version-destroy-ttl)`     | `[--version-destroy-ttl](https://cloud.google.com/sdk/gcloud/reference/secrets/update#--version-destroy-ttl)`=`VERSION-DESTROY-TTL`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/secrets/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a secret's metadata (e.g. labels). This command will return an error if
given a secret that does not exist.

**EXAMPLES**

: Update the label of a secret named `my-secret`.

```
gcloud secrets update my-secret --update-labels=foo=bar
```

Update the label of a secret using an etag.

```
gcloud secrets update my-secret --update-labels=foo=bar --etag=123
```

Update a secret to have a next-rotation-time:

```
gcloud secrets update my-secret --next-rotation-time="2030-01-01T15:30:00-05:00"
```

Update a secret to have a next-rotation-time and rotation-period:

```
gcloud secrets update my-secret --next-rotation-time="2030-01-01T15:30:00-05:00" --rotation-period="7200s"
```

Update a secret to remove the next-rotation-time:

```
gcloud secrets update my-secret --remove-next-rotation-time
```

Update a secret to clear rotation policy:

```
gcloud secrets update my-secret --remove-rotation-schedule
```

Update version destroy ttl of a secret:

```
gcloud secrets update my-secret --version-destroy-ttl="86400s"
```

Disable delayed secret version destroy:

```
gcloud secrets update my-secret --remove-version-destroy-ttl
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

**FLAGS**

: **--etag**:
Current entity tag (ETag) of the secret. If specified, the secret is updated
only if the ETag provided matches the current secret's ETag.

**Location resource - The location to update secret. This represents a Cloud
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

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--add-topics**

**--clear-annotations**

**--clear-labels**

**--clear-version-aliases**

**--expire-time**

**--next-rotation-time**

**--regional-kms-key-name**

**--remove-version-destroy-ttl**

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
gcloud beta secrets update
```