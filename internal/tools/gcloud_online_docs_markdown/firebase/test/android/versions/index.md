# gcloud firebase test android versions  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/versions](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/versions)*

**NAME**

: **gcloud firebase test android versions - explore Android versions available for testing**

**SYNOPSIS**

: **`gcloud firebase test android versions` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/versions#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/versions#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Explore Android versions available for testing.

**EXAMPLES**

: To list information about all versions of the Android OS available for running
tests, including details such as OS code name and release date, run:

```
gcloud firebase test android versions list
```

To view information about a specific Android OS version, run:

```
gcloud firebase test android versions describe VERSION_ID
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/versions/describe)`**:
Describe an Android OS version.

**`[list](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/versions/list)`**:
List all Android OS versions available for testing.

**NOTES**

: These variants are also available:

```
gcloud alpha firebase test android versions
```

```
gcloud beta firebase test android versions
```