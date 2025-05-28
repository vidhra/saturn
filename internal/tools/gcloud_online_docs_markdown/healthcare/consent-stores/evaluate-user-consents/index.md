# gcloud healthcare consent-stores evaluate-user-consents  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/evaluate-user-consents](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/evaluate-user-consents)*

**NAME**

: **gcloud healthcare consent-stores evaluate-user-consents - check the consents for a particular user's data**

**SYNOPSIS**

: **`gcloud healthcare consent-stores evaluate-user-consents` (`[CONSENT_STORE](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/evaluate-user-consents#CONSENT_STORE)` : `[--dataset](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/evaluate-user-consents#--dataset)`=`DATASET` `[--location](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/evaluate-user-consents#--location)`=`LOCATION`) `[--user-id](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/evaluate-user-consents#--user-id)`=`USER_ID` [`[--consent-list](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/evaluate-user-consents#--consent-list)`=[`CONSENT_LIST`,…]] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/evaluate-user-consents#--page-size)`=`PAGE_SIZE`] [`[--page-token](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/evaluate-user-consents#--page-token)`=`PAGE_TOKEN`] [`[--request-attributes](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/evaluate-user-consents#--request-attributes)`=[`KEY`=`VALUE`,…]] [`[--resource-attributes](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/evaluate-user-consents#--resource-attributes)`=[`KEY`=`VALUE`,…]] [`[--response-view](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/evaluate-user-consents#--response-view)`=`RESPONSE_VIEW`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/evaluate-user-consents#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Check if each matching user data mapping in the given Cloud Healthcare API
consent store is consented for a given use.

**EXAMPLES**

: To check if the data for user 'test-user-id' in the consent-store
'test-consent-store' can be used given request attributes
{"organization":"admins", "use_case":"research"}, run:

```
gcloud healthcare consent-stores evaluate-user-consents test-consent-store --user-id=test-user-id --request-attributes=organization=admins,use_case=research --dataset=test-dataset
```

**POSITIONAL ARGUMENTS**

: **ConsentStore resource - Cloud Healthcare API consent store where the requested
data is stored. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
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

**REQUIRED FLAGS**

: **--user-id**:
The unique identifier of the user to evaluate consents for.

**OPTIONAL FLAGS**

: **--consent-list**:
List of user consents to evaluate the access request against. They must have the
same user_id as the data to check access for, exist in the current
consent_store, and have a state of either ACTIVE or DRAFT. A maximum of 100
consents can be provided here.

**--page-size**:
Limit on the number of user data mappings to return in a single response. If
zero the default page size of 100 is used.

**--page-token**:
Token to retrieve the next page of results.

**--request-attributes**:
Comma-separated list of request attributes associated with this access request.
Each attribute has the form "KEY=VALUE".

**--resource-attributes**:
Comma-separated list of resource attributes associated with this access request.
Each attribute has the form "KEY=VALUE". If no values are specified, then all
data types are queried.

**--response-view**:
The requested view of information provided in the response (BASIC or FULL).
`RESPONSE_VIEW` must be one of: `basic`,
`full`, `response-view-unspecified`.

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
gcloud alpha healthcare consent-stores evaluate-user-consents
```

```
gcloud beta healthcare consent-stores evaluate-user-consents
```