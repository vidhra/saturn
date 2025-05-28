# gcloud kms keys create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/keys/create](https://cloud.google.com/sdk/gcloud/reference/kms/keys/create)*

**NAME**

: **gcloud kms keys create - create a new key**

**SYNOPSIS**

: **`gcloud kms keys create` (`[KEY](https://cloud.google.com/sdk/gcloud/reference/kms/keys/create#KEY)` : `[--keyring](https://cloud.google.com/sdk/gcloud/reference/kms/keys/create#--keyring)`=`KEYRING` `[--location](https://cloud.google.com/sdk/gcloud/reference/kms/keys/create#--location)`=`LOCATION`) `[--purpose](https://cloud.google.com/sdk/gcloud/reference/kms/keys/create#--purpose)`=`PURPOSE` [`[--allowed-access-reasons](https://cloud.google.com/sdk/gcloud/reference/kms/keys/create#--allowed-access-reasons)`=[`ALLOWED_ACCESS_REASONS`,…]] [`[--crypto-key-backend](https://cloud.google.com/sdk/gcloud/reference/kms/keys/create#--crypto-key-backend)`=`CRYPTO_KEY_BACKEND`] [`[--default-algorithm](https://cloud.google.com/sdk/gcloud/reference/kms/keys/create#--default-algorithm)`=`DEFAULT_ALGORITHM`] [`[--destroy-scheduled-duration](https://cloud.google.com/sdk/gcloud/reference/kms/keys/create#--destroy-scheduled-duration)`=`DESTROY_SCHEDULED_DURATION`] [`[--import-only](https://cloud.google.com/sdk/gcloud/reference/kms/keys/create#--import-only)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/kms/keys/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--next-rotation-time](https://cloud.google.com/sdk/gcloud/reference/kms/keys/create#--next-rotation-time)`=`NEXT_ROTATION_TIME`] [`[--protection-level](https://cloud.google.com/sdk/gcloud/reference/kms/keys/create#--protection-level)`=`PROTECTION_LEVEL`; default="software"] [`[--rotation-period](https://cloud.google.com/sdk/gcloud/reference/kms/keys/create#--rotation-period)`=`ROTATION_PERIOD`] [`[--skip-initial-version-creation](https://cloud.google.com/sdk/gcloud/reference/kms/keys/create#--skip-initial-version-creation)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/keys/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a new key within the given keyring.
The flag `--purpose` is always required when creating a key. The flag
`--default-algorithm` is required when creating a symmetric signing
key, an asymmetric key, or an external key. Algorithm and purpose should be
compatible.
The optional flags `--rotation-period` and
`--next-rotation-time` define a rotation schedule for the key. A
schedule can also be defined by the `--create-rotation-schedule`
command.
The flag `--next-rotation-time` must be in ISO 8601 or RFC3339
format, and `rotation-period` must be in the form INTEGER[UNIT],
where units can be one of seconds (s), minutes (m), hours (h) or days (d).
The optional flag `--protection-level` specifies the physical
environment where crypto operations with the key happen. The default is
``software``; use
``hsm`` to create a hardware-backed key,
``external`` to create an externally backed
key, or ``external-vpc`` to create an external
key over vpc.
The optional flag `--labels` defines a user specified key/value pair
for the given key.
The flag `--skip-initial-version-creation` creates a CryptoKey with
no versions. If you import into the CryptoKey, or create a new version in that
CryptoKey, there will be no primary version until one is set using the
`--set-primary-version` command. You must include
`--skip-initial-version-creation` when creating a CryptoKey with
protection level ``external`` or
``external-vpc``.
The optional flag `--import-only` restricts the key to imported key
versions only. To do so, the flag `--skip-initial-version-creation`
must also be set.
The optional flag `--destroy-scheduled-duration` defines the destroy
schedule for the key, and must be in the form INTEGER[UNIT], where units can be
one of seconds (s), minutes (m), hours (h) or days (d).
The flag `--crypto-key-backend` defines the resource name for the
backend where the key resides. Required for
``external-vpc`` keys.
The optional flag `--allowed-access-reasons` defines the Key Access
Justifications Policy for the key, and is specified as a comma separated list of
zero or more justification codes defined in [https://cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes](https://cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes).
The key must be enrolled in Key Access Justifications to use this flag.

**EXAMPLES**

: The following command creates a key named
``frodo`` with protection level
``software`` within the keyring
``fellowship`` and location
``us-east1``:

```
gcloud kms keys create frodo --location=us-east1 --keyring=fellowship --purpose=encryption
```

The following command creates a key named
``strider`` with protection level
``software`` within the keyring
``rangers`` and location
``global`` with a specified rotation schedule:

```
gcloud kms keys create strider --location=global --keyring=rangers --purpose=encryption --rotation-period=30d --next-rotation-time=2017-10-12T12:34:56.1234Z
```

The following command creates a raw encryption key named
``foo`` with protection level
``software`` within the keyring
``fellowship`` and location
``us-east1`` with two specified labels:

```
gcloud kms keys create foo --location=us-east1 --keyring=fellowship --purpose=raw-encryption --default-algorithm=aes-128-cbc --labels=env=prod,team=kms
```

The following command creates an asymmetric key named
``samwise`` with protection level
``software`` and default algorithm
``ec-sign-p256-sha256`` within the keyring
``fellowship`` and location
``us-east1``:

```
gcloud kms keys create samwise --location=us-east1 --keyring=fellowship --purpose=asymmetric-signing --default-algorithm=ec-sign-p256-sha256
```

The following command creates a key named
``gimli`` with protection level
``hsm`` and default algorithm
``google-symmetric-encryption`` within the
keyring ``fellowship`` and location
``us-east1``:

```
gcloud kms keys create gimli --location=us-east1 --keyring=fellowship --purpose=encryption --protection-level=hsm
```

The following command creates a key named
``legolas`` with protection level
``external`` and default algorithm
``external-symmetric-encryption`` within the
keyring ``fellowship`` and location
``us-central1``:

```
gcloud kms keys create legolas --location=us-central1 --keyring=fellowship --purpose=encryption --default-algorithm=external-symmetric-encryption --protection-level=external --skip-initial-version-creation
```

The following command creates a key named
``bilbo`` with protection level
``external-vpc`` and default algorithm
``external-symmetric-encryption`` and an
EkmConnection of ``eagles`` within the keyring
``fellowship`` and location
``us-central1``:

```
gcloud kms keys create bilbo --location=us-central1 --keyring=fellowship --purpose=encryption --default-algorithm=external-symmetric-encryption --protection-level=external-vpc --skip-initial-version-creation --crypto-key-backend="projects/$(gcloud config get project)/
    locations/us-central1/ekmConnections/eagles"
```

The following command creates a key named
``arwen`` with protection level
``software`` within the keyring
``fellowship`` and location
``us-east1`` with a Key Access Justifications
policy that allows access reasons
``customer-initiated-access`` and
``google-initiated-system-operation``:

```
gcloud kms keys create arwen --location=us-east1 --keyring=fellowship --purpose=encryption --allowed-access-reasons=customer-initiated-access,google-initiated-system-operation
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

**REQUIRED FLAGS**

: **--purpose**:
The "purpose" of the key. `PURPOSE` must be one of:
`asymmetric-encryption`, `asymmetric-signing`,
`encryption`, `mac`, `raw-encryption`.

**OPTIONAL FLAGS**

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

**--crypto-key-backend**:
The resource name of the backend environment where the key material for all
CryptoKeyVersions associated with this CryptoKey reside and where all related
cryptographic operations are performed. Currently only applicable for
EXTERNAL_VPC and EkmConnection resource names.

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

**--destroy-scheduled-duration**:
The amount of time that versions of the key should spend in the
DESTROY_SCHEDULED state before transitioning to DESTROYED. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--import-only**:
Restrict this key to imported versions only.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--next-rotation-time**:
Next automatic rotation time of the key. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on time formats.

**--protection-level**:
Protection level of the key. `PROTECTION_LEVEL` must be
one of: `software`, `hsm`, `external`,
`external-vpc`.

**--rotation-period**:
Automatic rotation period of the key. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--skip-initial-version-creation**:
Skip creating the first version in a key and setting it as primary during
creation.

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
gcloud alpha kms keys create
```

```
gcloud beta kms keys create
```