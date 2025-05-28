# gcloud services api-keys undelete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/services/api-keys/undelete](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/undelete)*

**NAME**

: **gcloud services api-keys undelete - undelete an API key**

**SYNOPSIS**

: **`gcloud services api-keys undelete` ([`[KEY](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/undelete#KEY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/undelete#--location)`=`LOCATION`] `[--key-string](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/undelete#--key-string)`=`KEY_STRING`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/undelete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/undelete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: API Keys that are deleted will be retained in the system for 30 days. If a key
is still within this retention window, it can be undeleted with this command.

**EXAMPLES**

: UnDelete an API Key (Key or key-string should be specified):
To undelete with key `1234`, run:

```
gcloud services api-keys undelete 1234
```

To undelete with `1234` in project `myproject` using the
fully qualified API key name, run:

```
gcloud services api-keys undelete projects/myproject/locations/global/keys/1234
```

To undelete using a Key-string, run:

```
gcloud services api-keys undelete --key-string='my-key-string'
```

**POSITIONAL ARGUMENTS**

: **Exactly one of these must be specified:

**Key resource - The name of the key to undelete. The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `key` on the command line with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**`KEY`**:
ID of the key or fully qualified identifier for the key.
To set the `key` attribute:

- provide the argument `key` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the key.
To set the `location` attribute:

- provide the argument `key` on the command line with a fully specified
name;
- provide the argument `--location` on the command line;
- location will default to global.**

**--key-string**:
Key String of the key.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud alpha services api-keys undelete
```

```
gcloud beta services api-keys undelete
```