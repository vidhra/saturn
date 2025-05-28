# gcloud network-security security-profile-groups create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create)*

**NAME**

: **gcloud network-security security-profile-groups create - create a new Security Profile Group**

**SYNOPSIS**

: **`gcloud network-security security-profile-groups create` (`[SECURITY_PROFILE_GROUP](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create#SECURITY_PROFILE_GROUP)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create#--organization)`=`ORGANIZATION`) ([`[--custom-intercept-profile](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create#--custom-intercept-profile)`=`CUSTOM_INTERCEPT_PROFILE` : `[--custom-intercept-profile-location](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create#--custom-intercept-profile-location)`=`CUSTOM_INTERCEPT_PROFILE_LOCATION` `[--custom-intercept-profile-organization](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create#--custom-intercept-profile-organization)`=`CUSTOM_INTERCEPT_PROFILE_ORGANIZATION`] [`[--custom-mirroring-profile](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create#--custom-mirroring-profile)`=`CUSTOM_MIRRORING_PROFILE` : `[--custom-mirroring-profile-location](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create#--custom-mirroring-profile-location)`=`CUSTOM_MIRRORING_PROFILE_LOCATION` `[--custom-mirroring-profile-organization](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create#--custom-mirroring-profile-organization)`=`CUSTOM_MIRRORING_PROFILE_ORGANIZATION`] [`[--threat-prevention-profile](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create#--threat-prevention-profile)`=`THREAT_PREVENTION_PROFILE` : `[--threat-prevention-profile-location](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create#--threat-prevention-profile-location)`=`THREAT_PREVENTION_PROFILE_LOCATION` `[--threat-prevention-profile-organization](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create#--threat-prevention-profile-organization)`=`THREAT_PREVENTION_PROFILE_ORGANIZATION`]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Security Profile Group with the given name.

**EXAMPLES**

: To create a Security Profile Group with the name
`my-security-profile-group`, with a threat prevention profile using
`--threat-prevention-profile` flag and optional description as
`optional description`, run:

```
gcloud network-security security-profile-groups create my-security-profile-group --organization=1234 --location=global --threat-prevention-profile=`organizations/1234/locations/global/securityProfiles/my-security-profile` --description='optional description'
```

**POSITIONAL ARGUMENTS**

: **Security profile group resource - Security Profile Group Name. The arguments in
this group can be used to specify the attributes of this resource.
This must be specified.

**`SECURITY_PROFILE_GROUP`**:
ID of the security_profile_group or fully qualified identifier for the
security_profile_group.
To set the `security_profile_group` attribute:

- provide the argument `SECURITY_PROFILE_GROUP` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
location of the security_profile_group - Global.
To set the `location` attribute:

- provide the argument `SECURITY_PROFILE_GROUP` on the command line
with a fully specified name;
- provide the argument `--location` on the command line.

**--organization**:
Organization ID of Security Profile Group
To set the `organization` attribute:

- provide the argument `SECURITY_PROFILE_GROUP` on the command line
with a fully specified name;
- provide the argument `--organization` on the command line.**

**REQUIRED FLAGS**

: **--custom-intercept-profile**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `False`.

**--description**:
Brief description of the security profile group

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
gcloud alpha network-security security-profile-groups create
```

```
gcloud beta network-security security-profile-groups create
```