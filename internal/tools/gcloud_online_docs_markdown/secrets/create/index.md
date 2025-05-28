# gcloud secrets create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/secrets/create](https://cloud.google.com/sdk/gcloud/reference/secrets/create)*

**NAME**

: **gcloud secrets create - create a new secret**

**SYNOPSIS**

: **`gcloud secrets create` `[SECRET](https://cloud.google.com/sdk/gcloud/reference/secrets/create#SECRET)` [`[--data-file](https://cloud.google.com/sdk/gcloud/reference/secrets/create#--data-file)`=`PATH`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/secrets/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--location](https://cloud.google.com/sdk/gcloud/reference/secrets/create#--location)`=`LOCATION`] [`[--regional-kms-key-name](https://cloud.google.com/sdk/gcloud/reference/secrets/create#--regional-kms-key-name)`=`KMS-KEY-NAME`] [`[--set-annotations](https://cloud.google.com/sdk/gcloud/reference/secrets/create#--set-annotations)`=[`KEY`=`VALUE`,…]] [`[--topics](https://cloud.google.com/sdk/gcloud/reference/secrets/create#--topics)`=[`TOPICS`,…]] [`[--version-destroy-ttl](https://cloud.google.com/sdk/gcloud/reference/secrets/create#--version-destroy-ttl)`=`VERSION-DESTROY-TTL`] [`[--expire-time](https://cloud.google.com/sdk/gcloud/reference/secrets/create#--expire-time)`=`EXPIRE-TIME`     | `[--ttl](https://cloud.google.com/sdk/gcloud/reference/secrets/create#--ttl)`=`TTL`] [`[--next-rotation-time](https://cloud.google.com/sdk/gcloud/reference/secrets/create#--next-rotation-time)`=`NEXT_ROTATION_TIME` `[--rotation-period](https://cloud.google.com/sdk/gcloud/reference/secrets/create#--rotation-period)`=`ROTATION_PERIOD`] [`[--replication-policy-file](https://cloud.google.com/sdk/gcloud/reference/secrets/create#--replication-policy-file)`=`REPLICATION-POLICY-FILE`     | `[--kms-key-name](https://cloud.google.com/sdk/gcloud/reference/secrets/create#--kms-key-name)`=`KMS-KEY-NAME` `[--locations](https://cloud.google.com/sdk/gcloud/reference/secrets/create#--locations)`=[`LOCATION`,…] `[--replication-policy](https://cloud.google.com/sdk/gcloud/reference/secrets/create#--replication-policy)`=`POLICY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/secrets/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a secret with the given name and creates a secret version with the given
data, if any. If a secret already exists with the given name, this command will
return an error.

**EXAMPLES**

: Create a secret with an automatic replication policy without creating any
versions:

```
gcloud secrets create my-secret
```

Create a new secret named 'my-secret' with an automatic replication policy and
data from a file:

```
gcloud secrets create my-secret --data-file=/tmp/secret
```

Create a new secret named 'my-secret' in 'us-central1' with data from a file:

```
gcloud secrets create my-secret --data-file=/tmp/secret --replication-policy=user-managed --locations=us-central1
```

Create a new secret named 'my-secret' in 'us-central1' and 'us-east1' with the
value "s3cr3t":

```
printf "s3cr3t" | gcloud secrets create my-secret --data-file=- --replication-policy=user-managed --locations=us-central1,us-east1
```

Create a new secret named 'my-secret' in 'us-central1' and 'us-east1' with the
value "s3cr3t" in PowerShell (Note: PowerShell will add a newline to the
resulting secret):

```
Write-Output "s3cr3t" | gcloud secrets create my-secret --data-file=- --replication-policy=user-managed --locations=us-central1,us-east1
```

Create a secret with an automatic replication policy and a next rotation time:

```
gcloud secrets create my-secret --next-rotation-time="2030-01-01T15:30:00-05:00"
```

Create a secret with an automatic replication policy and a rotation period:

```
gcloud secrets create my-secret --next-rotation-time="2030-01-01T15:30:00-05:00" --rotation-period="7200s"
```

Create a secret with delayed secret version destroy enabled:

```
gcloud secrets create my-secret --version-destroy-ttl="86400s"
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

**FLAGS**

: **--data-file**:
File path from which to read secret data. Set this to "-" to read the secret
data from stdin.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**Location resource - The location to create secret. This represents a Cloud
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

**--regional-kms-key-name**:
Regional KMS key with which to encrypt and decrypt the secret. Only valid for
regional secrets.

**--set-annotations**

**--topics**:
List of Pub/Sub topics to configure on the secret.

**--version-destroy-ttl**:
Secret Version Time To Live (TTL) after destruction request. For secret with
TTL>0, version destruction does not happen immediately on calling destroy;
instead, the version goes to a disabled state and destruction happens after the
TTL expires. See `$ [gcloud
topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on duration formats.

**--expire-time**

**--next-rotation-time**

**--replication-policy-file**

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
gcloud beta secrets create
```