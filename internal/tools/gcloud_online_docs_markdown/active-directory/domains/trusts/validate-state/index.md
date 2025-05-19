# gcloud active-directory domains trusts validate-state  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/validate-state](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/validate-state)*

**NAME**

: **gcloud active-directory domains trusts validate-state - validate the state of a Managed Microsoft AD trust**

**SYNOPSIS**

: **`gcloud active-directory domains trusts validate-state` `[DOMAIN](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/validate-state#DOMAIN)` `[--target-domain-name](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/validate-state#--target-domain-name)`=`TARGET_DOMAIN_NAME` [`[--async](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/validate-state#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/validate-state#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Validate the state of a Managed Microsoft AD trust.
Verify that the trust has been properly created and that the domains/forests can
communicate with each other.
This command can fail for the following reasons:

- The AD domain specified does not exist.
- The active account does not have permission to access the given AD domain.
- The AD trust specified does not exist.
- The active account does not have permission to access the given AD trust.

**EXAMPLES**

: The following command validates state for an AD trust with the given target
domain name `my-target-domain.com`.

```
gcloud active-directory domains trusts validate-state my-domain.com --target-domain-name=my-target-domain.com
```

**POSITIONAL ARGUMENTS**

: **Domain resource - Name of the the Managed Microsoft AD trust for which you want
to validate state. This represents a Cloud resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `domain` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DOMAIN`**:
ID of the domain or fully qualified identifier for the domain.
To set the `domain` attribute:

- provide the argument `domain` on the command line.**

**REQUIRED FLAGS**

: **--target-domain-name**:
Target domain name of the Managed Microsoft AD Active Directory trust you want
to validate.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

: This command uses the `managedidentities/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/managed-microsoft-ad/](https://cloud.google.com/managed-microsoft-ad/)

**NOTES**

: These variants are also available:

```
gcloud alpha active-directory domains trusts validate-state
```

```
gcloud beta active-directory domains trusts validate-state
```