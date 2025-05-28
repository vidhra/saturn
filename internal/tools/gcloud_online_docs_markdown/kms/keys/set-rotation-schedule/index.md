# gcloud kms keys set-rotation-schedule  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-rotation-schedule](https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-rotation-schedule)*

**NAME**

: **gcloud kms keys set-rotation-schedule - update the rotation schedule for a key**

**SYNOPSIS**

: **`gcloud kms keys set-rotation-schedule` (`[KEY](https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-rotation-schedule#KEY)` : `[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-rotation-schedule#--keyring)`=`KEYRING` `[--location](https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-rotation-schedule#--location)`=`LOCATION`) [`[--next-rotation-time](https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-rotation-schedule#--next-rotation-time)`=`NEXT_ROTATION_TIME`] [`[--rotation-period](https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-rotation-schedule#--rotation-period)`=`ROTATION_PERIOD`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-rotation-schedule#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates the rotation schedule for the given key. The schedule automatically
creates a new primary version for the key according to the
`--next-rotation-time` and `--rotation-period` flags.
The flag `--next-rotation-time` must be in ISO or RFC3339 format, and
`--rotation-period` must be in the form INTEGER[UNIT], where units
can be one of seconds (s), minutes (m), hours (h) or days (d).
Key rotations performed manually via `update-primary-version` and the
version `create` do not affect the stored
`--next-rotation-time`.

**EXAMPLES**

: The following command sets a 30 day rotation period for the key named
`frodo` within the keyring `fellowship` and location
`global` starting at the specified time:

```
gcloud kms keys set-rotation-schedule frodo --location=global --keyring=fellowship --rotation-period=30d --next-rotation-time=2017-10-12T12:34:56.1234Z
```

**POSITIONAL ARGUMENTS**

: **Key resource - The KMS key resource. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `key` on the command line with a fully specified
name;
- set the property `core/project`.

This must be specified.

**`KEY`**:
ID of the key or fully qualified identifier for the key.
To set the `key` attribute:

- provide the argument `key` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--keyring**:
The KMS keyring of the key.
To set the `keyring` attribute:

- provide the argument `key` on the command line with a fully specified
name;
- provide the argument `--keyring` on the command line.

**--location**:
The Google Cloud location for the key.
To set the `location` attribute:

- provide the argument `key` on the command line with a fully specified
name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--next-rotation-time**:
Next automatic rotation time of the key. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on time formats.

**--rotation-period**:
Automatic rotation period of the key. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

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
gcloud alpha kms keys set-rotation-schedule
```

```
gcloud beta kms keys set-rotation-schedule
```