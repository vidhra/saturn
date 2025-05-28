# gcloud network-security security-profiles threat-prevention create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/create](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/create)*

**NAME**

: **gcloud network-security security-profiles threat-prevention create - create a new Threat Prevention Profile**

**SYNOPSIS**

: **`gcloud network-security security-profiles threat-prevention create` (`[SECURITY_PROFILE](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/create#SECURITY_PROFILE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/create#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/create#--organization)`=`ORGANIZATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Security Profile with the given name.

**EXAMPLES**

: To create a Security Profile with the name `my-security-profile` and
an optional description as `New Security Profile`, run:

```
gcloud network-security security-profiles threat-prevention create my-security-profile --description="New Security Profile"
```

**POSITIONAL ARGUMENTS**

: **Security profile resource - Security Profile Name. The arguments in this group
can be used to specify the attributes of this resource.
This must be specified.

**`SECURITY_PROFILE`**:
ID of the security_profile or fully qualified identifier for the
security_profile.
To set the `security_profile` attribute:

- provide the argument `security_profile` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
location of the security_profile - Global.
To set the `location` attribute:

- provide the argument `security_profile` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.

**--organization**:
Organization ID to which the changes should apply.
To set the `organization` attribute:

- provide the argument `security_profile` on the command line with a
fully specified name;
- provide the argument `--organization` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `False`.

**--description**:
Brief description of the security profile

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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
gcloud alpha network-security security-profiles threat-prevention create
```

```
gcloud beta network-security security-profiles threat-prevention create
```