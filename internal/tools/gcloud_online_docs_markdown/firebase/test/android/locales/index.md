# gcloud firebase test android locales  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/locales](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/locales)*

**NAME**

: **gcloud firebase test android locales - explore Android locales available for testing**

**SYNOPSIS**

: **`gcloud firebase test android locales` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/locales#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/locales#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Explore Android locales available for testing.

**EXAMPLES**

: To list all available Android locales which can be used for testing
international applications, run:

```
gcloud firebase test android locales list
```

To view information about a specific locale, run:

```
gcloud firebase test android locales describe LOCALE
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/locales/describe)`**:
Describe an Android locale.

**`[list](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/locales/list)`**:
List all Android locales available for testing internationalized apps.

**NOTES**

: These variants are also available:

```
gcloud alpha firebase test android locales
```

```
gcloud beta firebase test android locales
```