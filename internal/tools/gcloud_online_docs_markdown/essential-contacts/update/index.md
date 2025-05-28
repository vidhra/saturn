# gcloud essential-contacts update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/essential-contacts/update](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/update)*

**NAME**

: **gcloud essential-contacts update - update an essential contact**

**SYNOPSIS**

: **`gcloud essential-contacts update` `[CONTACT_ID](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/update#CONTACT_ID)` [`[--language](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/update#--language)`=`LANGUAGE`] [`[--notification-categories](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/update#--notification-categories)`=[`NOTIFICATION_CATEGORIES`,…]] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/update#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/update#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/update#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/update#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To update the notification category subscriptions for the contact with id
``123`` in the current project, run:

```
gcloud essential-contacts update 123 --notification-categories=legal,suspension
```

To update the language preference for the contact with id
``123`` in the folder with id
``456``, run:

```
gcloud essential-contacts update 123 --language=es --folder=456
```

To update the notification category subscriptions and language preference for
the contact with id ``123`` in the organization
with id ``456``, run:

```
gcloud essential-contacts update 123 --notification-categories=legal --language=en-US --organization=456
```

**POSITIONAL ARGUMENTS**

: **`CONTACT_ID`**:
id of contact

**FLAGS**

: **--language**:
preferred language of contact. Must be a valid ISO 639-1 language code.

**--notification-categories**:
list of notification categories contact is subscribed to.
`NOTIFICATION_CATEGORIES` must be one of:
`all`, `billing`, `legal`,
`notification-category-unspecified`, `product-updates`,
`security`, `suspension`, `technical`,
`technical-incidents`.

**--folder**

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
gcloud alpha essential-contacts update
```

```
gcloud beta essential-contacts update
```