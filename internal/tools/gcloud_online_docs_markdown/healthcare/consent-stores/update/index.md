# gcloud healthcare consent-stores update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/update](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/update)*

**NAME**

: **gcloud healthcare consent-stores update - update a Cloud Healthcare API consent store**

**SYNOPSIS**

: **`gcloud healthcare consent-stores update` (`[CONSENT_STORE](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/update#CONSENT_STORE)` : `[--dataset](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/update#--dataset)`=`DATASET` `[--location](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/update#--location)`=`LOCATION`) [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Cloud Healthcare API consent store.

**EXAMPLES**

: To update the consent store 'test-consent-store' with labels {"key1":"value1",
"key2":"value2"}, run:

```
gcloud healthcare consent-stores update test-consent-store --update-labels=key1=value1,key2=value2 --dataset=test-dataset
```

**POSITIONAL ARGUMENTS**

: **ConsentStore resource - Cloud Healthcare API consent store to update. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `consent_store` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CONSENT_STORE`**:
ID of the consentStore or fully qualified identifier for the consentStore.
To set the `consent_store` attribute:

- provide the argument `consent_store` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--dataset**:
Cloud Healthcare dataset.
To set the `dataset` attribute:

- provide the argument `consent_store` on the command line with a fully
specified name;
- provide the argument `--dataset` on the command line.

**--location**:
Google Cloud location.
To set the `location` attribute:

- provide the argument `consent_store` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `healthcare/location`.**

**FLAGS**

: **--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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

: This command uses the `healthcare/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/healthcare](https://cloud.google.com/healthcare)

**NOTES**

: These variants are also available:

```
gcloud alpha healthcare consent-stores update
```

```
gcloud beta healthcare consent-stores update
```