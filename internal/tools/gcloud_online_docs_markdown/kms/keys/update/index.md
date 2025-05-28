# gcloud kms keys update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/keys/update](https://cloud.google.com/sdk/gcloud/reference/kms/keys/update)*

**NAME**

: **gcloud kms keys update - update a key**

**SYNOPSIS**

: **`gcloud kms keys update` (`[KEY](https://cloud.google.com/sdk/gcloud/reference/kms/keys/update#KEY)` : `[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/keys/update#--keyring)`=`KEYRING` `[--location](https://cloud.google.com/sdk/gcloud/reference/kms/keys/update#--location)`=`LOCATION`) [`[--allowed-access-reasons](https://cloud.google.com/sdk/gcloud/reference/kms/keys/update#--allowed-access-reasons)`=[`ALLOWED_ACCESS_REASONS`,…]] [`[--default-algorithm](https://cloud.google.com/sdk/gcloud/reference/kms/keys/update#--default-algorithm)`=`DEFAULT_ALGORITHM`] [`[--next-rotation-time](https://cloud.google.com/sdk/gcloud/reference/kms/keys/update#--next-rotation-time)`=`NEXT_ROTATION_TIME`] [`[--primary-version](https://cloud.google.com/sdk/gcloud/reference/kms/keys/update#--primary-version)`=`PRIMARY_VERSION`] [`[--remove-key-access-justifications-policy](https://cloud.google.com/sdk/gcloud/reference/kms/keys/update#--remove-key-access-justifications-policy)`] [`[--remove-rotation-schedule](https://cloud.google.com/sdk/gcloud/reference/kms/keys/update#--remove-rotation-schedule)`] [`[--rotation-period](https://cloud.google.com/sdk/gcloud/reference/kms/keys/update#--rotation-period)`=`ROTATION_PERIOD`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/kms/keys/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/kms/keys/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/kms/keys/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/keys/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: 1. Update the rotation schedule for the given key.
Updates the rotation schedule for the given key. The schedule automatically
creates a new primary version for the key according to
`next-rotation-time` and `rotation-period` flags.
Flag `next-rotation-time` must be in ISO 8601 or RFC3339 format, and
`rotation-period` must be in the form INTEGER[UNIT], where units can
be one of seconds (s), minutes (m), hours (h) or days (d).
Key rotations performed manually via `update-primary-version` and the
version `create` do not affect the stored
`next-rotation-time`.
2. Remove the rotation schedule for the given key with
`remove-rotation-schedule` flag.
3. Update/Remove the labels for the given key with `update-labels`
and/or `remove-labels` flags.
4. Update the primary version for the given key with
`primary-version` flag.
5. Update the Key Access Justifications policy for the given key with
`allowed-access-reasons` flag to allow specified reasons. The key
must be enrolled in Key Access Justifications to use this flag.
6. Remove the Key Access Justifications policy for the given key with
`remove-key-access-justifications-policy` flag. The key must be
enrolled in Key Access Justifications to use this flag.
7. Update the Key Access Justifications policy for the given key with
`allowed_access_reasons` flag to allow zero access reasons. This
effectively disables the key, because a policy is configured to reject all
access reasons. The key must be enrolled in Key Access Justifications to use
this flag.

**EXAMPLES**

: The following command sets a 30 day rotation period for the key named
`frodo` within the keyring `fellowship` and location
`global` starting at the specified time:

```
gcloud kms keys update frodo --location=global --keyring=fellowship --rotation-period=30d --next-rotation-time=2017-10-12T12:34:56.1234Z
```

The following command removes the rotation schedule for the key named
`frodo` within the keyring `fellowship` and location
`global`:

```
gcloud kms keys update frodo --location=global --keyring=fellowship --remove-rotation-schedule
```

The following command updates the labels value for the key named
`frodo` within the keyring `fellowship` and location
`global`. If the label key does not exist at the time, it will be
added:

```
gcloud kms keys update frodo --location=global --keyring=fellowship --update-labels=k1=v1
```

The following command removes labels k1 and k2 from the key named
`frodo` within the keyring `fellowship` and location
`global`:

```
gcloud kms keys update frodo --location=global --keyring=fellowship --remove-labels=k1,k2
```

The following command updates the primary version for the key named
`frodo` within the keyring `fellowship` and location
`global`:

```
gcloud kms keys update frodo --location=global --keyring=fellowship --primary-version=1
```

The following command updates the default algorithm for the key named
`frodo` within the keyring `fellowship` and location
`global`, assuming the key originally has purpose
'asymmetric-encryption' and algorithm 'rsa-decrypt-oaep-2048-sha256':

```
gcloud kms keys update frodo --location=global --keyring=fellowship --default-algorithm=rsa-decrypt-oaep-4096-sha256
```

The following command updates the Key Access Justifications policy for the key
named `frodo` within the keyring
``fellowship`` and location
``global`` to allow only
``customer-initiated-access`` and
``google-initiated-system-operation``:

```
gcloud kms keys update frodo --location=global --keyring=fellowship --allowed-access-reasons=customer-initiated-access,google-initiated-system-operation
```

The following command removes the Key Access Justifications policy for the key
named `frodo` within the keyring
``fellowship`` and location
``global``, which results in all access reasons
being allowed:

```
gcloud kms keys update frodo --location=global --keyring=fellowship --remove-key-access-justifications-policy
```

The following command updates the Key Access Justifications policy for the key
named `frodo` within the keyring
``fellowship`` and location
``global`` to allow only zero access reasons,
effectively disabling the key:

```
gcloud kms keys update frodo --location=global --keyring=fellowship --allowed-access-reasons=
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

: **--allowed-access-reasons**:
The list of allowed Key Access Justifications access reasons on the key. The key
must be enrolled in Key Access Justifications to configure this field. By
default, this field is absent, and all justification codes are allowed. For more
information about justification codes, see [https://cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes](https://cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes).
`ALLOWED_ACCESS_REASONS` must be one of:
`customer-authorized-workflow-servicing`,
`customer-initiated-access`, `customer-initiated-support`,
`google-initiated-review`, `google-initiated-service`,
`google-initiated-system-operation`,
`google-response-to-production-alert`,
`modified-customer-initiated-access`,
`modified-google-initiated-system-operation`,
`reason-not-expected`, `reason-unspecified`,
`third-party-data-request`.

**--default-algorithm**:
The default algorithm for the crypto key. For more information about choosing an
algorithm, see [https://cloud.google.com/kms/docs/algorithms](https://cloud.google.com/kms/docs/algorithms).
`DEFAULT_ALGORITHM` must be one of:
`aes-128-cbc`, `aes-128-ctr`, `aes-128-gcm`,
`aes-256-cbc`, `aes-256-ctr`, `aes-256-gcm`,
`ec-sign-ed25519`, `ec-sign-p256-sha256`,
`ec-sign-p384-sha384`, `ec-sign-secp256k1-sha256`,
`external-symmetric-encryption`,
`google-symmetric-encryption`, `hmac-sha1`,
`hmac-sha224`, `hmac-sha256`, `hmac-sha384`,
`hmac-sha512`, `pq-sign-ml-dsa-65`,
`pq-sign-slh-dsa-sha2-128s`, `rsa-decrypt-oaep-2048-sha1`,
`rsa-decrypt-oaep-2048-sha256`,
`rsa-decrypt-oaep-3072-sha1`,
`rsa-decrypt-oaep-3072-sha256`,
`rsa-decrypt-oaep-4096-sha1`,
`rsa-decrypt-oaep-4096-sha256`,
`rsa-decrypt-oaep-4096-sha512`,
`rsa-sign-pkcs1-2048-sha256`,
`rsa-sign-pkcs1-3072-sha256`,
`rsa-sign-pkcs1-4096-sha256`,
`rsa-sign-pkcs1-4096-sha512`, `rsa-sign-pss-2048-sha256`,
`rsa-sign-pss-3072-sha256`, `rsa-sign-pss-4096-sha256`,
`rsa-sign-pss-4096-sha512`, `rsa-sign-raw-pkcs1-2048`,
`rsa-sign-raw-pkcs1-3072`, `rsa-sign-raw-pkcs1-4096`.

**--next-rotation-time**:
Next automatic rotation time of the key. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on time formats.

**--primary-version**:
Primary version to make primary.

**--remove-key-access-justifications-policy**:
Removes the Key Access Justifications policy on the key, making all
justification codes allowed.

**--remove-rotation-schedule**:
Remove any existing rotation schedule on the key.

**--rotation-period**:
Automatic rotation period of the key. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

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

**NOTES**

: These variants are also available:

```
gcloud alpha kms keys update
```

```
gcloud beta kms keys update
```