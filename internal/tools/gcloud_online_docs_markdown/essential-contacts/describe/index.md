# gcloud essential-contacts describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/essential-contacts/describe](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/describe)*

**NAME**

: **gcloud essential-contacts describe - describe an essential contact**

**SYNOPSIS**

: **`gcloud essential-contacts describe` `[CONTACT_ID](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/describe#CONTACT_ID)` [`[--folder](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/describe#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/describe#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/describe#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/describe#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To describe the contact with id ``123`` in the
current project, run:

```
gcloud essential-contacts describe 123
```

To describe the contact with id ``123`` in the
folder with id ``456``, run:

```
gcloud essential-contacts describe 123 --folder=456
```

To describe the contact with id ``123`` in the
organization with id ``456``, run:

```
gcloud essential-contacts describe 123 --organization=456
```

**POSITIONAL ARGUMENTS**

: **`CONTACT_ID`**:
id of contact to describe.

**FLAGS**

: **--folder**

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
gcloud alpha essential-contacts describe
```

```
gcloud beta essential-contacts describe
```