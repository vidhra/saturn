# gcloud iap  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iap](https://cloud.google.com/sdk/gcloud/reference/iap)*

**NAME**

: **gcloud iap - manage IAP policies**

**SYNOPSIS**

: **`gcloud iap` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/iap#GROUP)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iap#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Cloud Identity-Aware Proxy (Cloud IAP) controls access to your cloud
applications running on Google Cloud Platform. Cloud IAP works by verifying user
identity and context of the request to determine if a user should be allowed to
access the application.
More information on Cloud IAP can be found here: [https://cloud.google.com/iap](https://cloud.google.com/iap) and
detailed documentation can be found here: [https://cloud.google.com/iap/docs/](https://cloud.google.com/iap/docs/)

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[oauth-brands](https://cloud.google.com/sdk/gcloud/reference/iap/oauth-brands)`**:
Manage IAP OAuth brands.

**`[oauth-clients](https://cloud.google.com/sdk/gcloud/reference/iap/oauth-clients)`**:
Manage IAP OAuth clients.

**`[settings](https://cloud.google.com/sdk/gcloud/reference/iap/settings)`**:
Manage IAP settings.

**`[tcp](https://cloud.google.com/sdk/gcloud/reference/iap/tcp)`**:
Manage IAP TCP resources.

**`[web](https://cloud.google.com/sdk/gcloud/reference/iap/web)`**:
Manage IAP web policies.

**NOTES**

: These variants are also available:

```
gcloud alpha iap
```

```
gcloud beta iap
```