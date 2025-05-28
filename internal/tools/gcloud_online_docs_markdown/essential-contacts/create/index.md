# gcloud essential-contacts create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/essential-contacts/create](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/create)*

**NAME**

: **gcloud essential-contacts create - create an essential contact**

**SYNOPSIS**

: **`gcloud essential-contacts create` `[--email](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/create#--email)`=`EMAIL` `[--language](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/create#--language)`=`LANGUAGE` `[--notification-categories](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/create#--notification-categories)`=[`NOTIFICATION_CATEGORIES`,…] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/create#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/create#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/create#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/create#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create a contact in the current project, run:

```
gcloud essential-contacts create --email=contact-email@example.com --notification-categories=technical,product-updates --language=en-US
```

To create a contact in the folder with id
``456``, run:

```
gcloud essential-contacts create --email=contact-email@example.com --notification-categories=technical,product-updates --language=en-US --folder=456
```

To create a contact in the organization with id
``456``, run:

```
gcloud essential-contacts create --email=contact-email@example.com --notification-categories=technical,product-updates --language=en-US --organization=456
```

**REQUIRED FLAGS**

: **--email**:
email address of contact.

**--language**:
preferred language of contact. Must be a valid ISO 639-1 language code.

**--notification-categories**:
list of notification categories contact is subscribed to.
`NOTIFICATION_CATEGORIES` must be one of:
`all`, `billing`, `legal`,
`notification-category-unspecified`, `product-updates`,
`security`, `suspension`, `technical`,
`technical-incidents`.

**OPTIONAL FLAGS**

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
gcloud alpha essential-contacts create
```

```
gcloud beta essential-contacts create
```