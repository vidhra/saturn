# gcloud network-security security-profile-groups describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/describe](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/describe)*

**NAME**

: **gcloud network-security security-profile-groups describe - describe a Security Profile Group**

**SYNOPSIS**

: **`gcloud network-security security-profile-groups describe` (`[SECURITY_PROFILE_GROUP](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/describe#SECURITY_PROFILE_GROUP)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/describe#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/describe#--organization)`=`ORGANIZATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Show details of a Security Profile Group.

**EXAMPLES**

: To show details of a Security Profile Group named
`my-security-profile-group` run:

```
gcloud network-security security-profile-groups describe my-security-profile-group --organization=1234 --location=global
```

**POSITIONAL ARGUMENTS**

: **Security profile group resource - Name of the Security Profile Group to be
described. The arguments in this group can be used to specify the attributes of
this resource.
This must be specified.

**`SECURITY_PROFILE_GROUP`**:
ID of the security_profile_group or fully qualified identifier for the
security_profile_group.
To set the `security_profile_group` attribute:

- provide the argument `security_profile_group` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location ID of the resource.
To set the `location` attribute:

- provide the argument `security_profile_group` on the command line
with a fully specified name;
- provide the argument `--location` on the command line;
- use default global location .

**--organization**:
Organization number.
To set the `organization` attribute:

- provide the argument `security_profile_group` on the command line
with a fully specified name;
- provide the argument `--organization` on the command line.**

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

: This command uses the `networksecurity/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/networking](https://cloud.google.com/networking)

**NOTES**

: These variants are also available:

```
gcloud alpha network-security security-profile-groups describe
```

```
gcloud beta network-security security-profile-groups describe
```