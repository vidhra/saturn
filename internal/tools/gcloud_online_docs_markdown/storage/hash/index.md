# gcloud storage hash  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/hash](https://cloud.google.com/sdk/gcloud/reference/storage/hash)*

**NAME**

: **gcloud storage hash - calculates hashes on local or cloud files**

**SYNOPSIS**

: **`gcloud storage hash` `[URLS](https://cloud.google.com/sdk/gcloud/reference/storage/hash#URLS)` [`[URLS](https://cloud.google.com/sdk/gcloud/reference/storage/hash#URLS)` …] [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/hash#--additional-headers)`=`HEADER`=`VALUE`] [`[--hex](https://cloud.google.com/sdk/gcloud/reference/storage/hash#--hex)`] [`[--skip-crc32c](https://cloud.google.com/sdk/gcloud/reference/storage/hash#--skip-crc32c)`     | `[--skip-md5](https://cloud.google.com/sdk/gcloud/reference/storage/hash#--skip-md5)`] [`[--decryption-keys](https://cloud.google.com/sdk/gcloud/reference/storage/hash#--decryption-keys)`=[`DECRYPTION_KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/hash#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Calculates hashes on local or cloud files that can be used to compare with
"gcloud storage ls -L" output. If a specific hash option is not provided, this
command calculates all gcloud storage-supported hashes for the file.
Note that gcloud storage automatically performs hash validation when uploading
or downloading files, so this command is only needed if you want to write a
script that separately checks the hash for some reason.
If you calculate a CRC32C hash for the file without a precompiled google-crc32c
installation, hashing will be very slow.

**EXAMPLES**

: To get the MD5 and CRC32C hash digest of a cloud object in Base64 format:

```
gcloud storage hash gs://bucket/object
```

To get just the MD5 hash digest of a local object in hex format:

```
gcloud storage hash /dir/object.txt --skip-crc32c --hex
```

**POSITIONAL ARGUMENTS**

: **`URLS` [`URLS` …]**:
Local or cloud URLs of objects to hash.

**FLAGS**

: **--additional-headers**:
Includes arbitrary headers in storage API calls. Accepts a comma separated list
of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides
the default `storage/additional_headers` property value for this
command invocation.

**--hex**:
Output hash digests in hex format. By default, digests are displayed in base64.

**--skip-crc32c**

**ENCRYPTION FLAGS**

: **--decryption-keys**:
A comma-separated list of customer-supplied encryption keys (RFC 4648 section 4
base64-encoded AES256 strings) that will be used to decrypt Cloud Storage
objects. Data encrypted with a customer-managed encryption key (CMEK) is
decrypted automatically, so CMEKs do not need to be listed here.

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
gcloud alpha storage hash
```