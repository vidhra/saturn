# gcloud services api-keys describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/services/api-keys/describe](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/describe)*

**NAME**

: **gcloud services api-keys describe - describe an API key's metadata**

**SYNOPSIS**

: **`gcloud services api-keys describe` (`[KEY](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/describe#KEY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe an API key's metadata.

**EXAMPLES**

: To describe an API key using Key:

```
gcloud services api-keys describe 1234 OR
gcloud services api-keys describe projects/myproject/locations/global/keys/1234
```

To describe an API key with key and project:

```
gcloud services api-keys describe 1234 --project=myproject
```

To describe an API key with key, project, and location:

```
gcloud services api-keys describe 1234 --project=myproject --location=global
```

**POSITIONAL ARGUMENTS**

: **Key resource - The name of the key to describe. The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `key` on the command line with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

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
gcloud alpha services api-keys describe
```

```
gcloud beta services api-keys describe
```