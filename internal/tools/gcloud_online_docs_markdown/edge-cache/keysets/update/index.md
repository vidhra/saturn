# gcloud edge-cache keysets update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/update](https://cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/update)*

**NAME**

: **gcloud edge-cache keysets update - update an EdgeCacheKeyset resource**

**SYNOPSIS**

: **`gcloud edge-cache keysets update` (`[KEYSET](https://cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/update#KEYSET)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/update#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/update#--labels)`=[`KEY`=`VALUE`,…]] [`[--public-key](https://cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/update#--public-key)`=[`id`=`ID`],[`managed`=`MANAGED`],[`value`=`VALUE`]] [`[--validation-shared-key](https://cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/update#--validation-shared-key)`=[`secret_version`=`SECRET_VERSION`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an existing EdgeCacheKeyset resource.

**EXAMPLES**

: To update an EdgeCacheKeyset resource called 'my-keyset', run:

```
gcloud edge-cache keysets update my-keyset --public-key='id=KEYID,value=BASE64PUBLICKEY'
```

The `update` command appends keys to an existing EdgeCacheKeyset
resource. To add more than one key to an EdgeCacheKeyset resource, provide
multiple `--public-key` values:

```
gcloud edge-cache keysets update my-keyset --public-key='id=KEYID,value=BASE64PUBLICKEY' --public-key='id=EXISTING,value=EXISTINGPUBLICKEY'
```

You can specify, and an EdgeCacheKeyset resource can contain, up to three (3)
public keys. To delete unused public keys within an existing Keyset, use the
`import` command to specify the EdgeCacheKeyset resource in full,
omitting any unused publicKey items.

**POSITIONAL ARGUMENTS**

: **Keyset resource - The name of the EdgeCacheKeyset resource to update. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `keyset` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`KEYSET`**:
ID of the keyset or fully qualified identifier for the keyset.
To set the `keyset` attribute:

- provide the argument `keyset` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location Id.
To set the `location` attribute:

- provide the argument `keyset` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- use global location.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Human-readable description of the resource.

**--labels**:
List of KEY=VALUE labels to attach to this resource.

**--public-key**:
Set of public keys to use for validating signed requests, when associated with a
route. This flag can be repeated to create a Keyset with multiple public keys.
If you are providing your own public keys, specify the key in the form
`id=ID,value=BASE64ENCODEDPUBLICKEY`.
If you are using Google-managed public keys as part of a dual-token setup,
specify the key in the form `id=ID,managed=true`.

**`id`**:
id (name) name of the key within the keyset.

**`value`**:
URL-safe base64 encoded public key. Cannot be specified if
`managed=true`.

**`managed`**:
Boolean indicating this is a Google-managed key. Cannot be specified if
`value=true`.

To create a public key with `id` 'foo', pass
`--public-key='id=foo,value=VALUE'` to gcloud edge-cache keysets
update.
To create a Google-managed public key with `id` 'bar', pass
`--public-key='id=foo,managed=true'` to gcloud edge-cache keysets
update.
At least one of public-key or validation-shared-key must be specified.

**--validation-shared-key**:
An ordered list of shared keys to use for validating signed requests.
To create a validation shared key pointing to a Secret Manager secret version
with name `projects/PROJECT/secrets/SECRET/versions/VERSION`, pass
`--validation-shared-key='secret_version=projects/PROJECT/secrets/SECRET/versions/VERSION'`
to gcloud edge-cache keysets update.

**`secret_version`**:
The name of the secret in Secret Manager. Must be in the format
`projects/PROJECT/secrets/SECRET/versions/VERSION`.

At least one of public-key or validation-shared-key must be specified.

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

**API REFERENCE**

: This command uses the `networkservices/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/networking](https://cloud.google.com/networking)

**NOTES**

: This variant is also available:

```
gcloud alpha edge-cache keysets update
```