# gcloud firebase test ios versions  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/versions](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/versions)*

**NAME**

: **gcloud firebase test ios versions - explore iOS versions available for testing**

**SYNOPSIS**

: **`gcloud firebase test ios versions` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/versions#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/versions#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Explore iOS versions available for testing.

**EXAMPLES**

: To list information about all versions of iOS available for running tests,
including details such as OS major and minor versions, run:

```
gcloud firebase test ios versions list
```

To view information about a specific version of iOS, run:

```
gcloud firebase test ios versions describe VERSION_ID
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/versions/describe)`**:
Describe an iOS operating system version.

**`[list](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/versions/list)`**:
List all iOS versions available for testing.

**NOTES**

: These variants are also available:

```
gcloud alpha firebase test ios versions
```

```
gcloud beta firebase test ios versions
```