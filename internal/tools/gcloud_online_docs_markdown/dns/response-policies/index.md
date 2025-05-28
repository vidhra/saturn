# gcloud dns response-policies  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/response-policies](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies)*

**NAME**

: **gcloud dns response-policies - manage your Cloud DNS response policy**

**SYNOPSIS**

: **`gcloud dns response-policies` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create a response policy, run:

```
gcloud dns response-policies create myresponsepolicy --description="My Response Policy" --network=''
```

To update a response policy, run:

```
gcloud dns response-policies update myresponsepolicy --description="My Response Policy" --network=''
```

To delete a response policy, run:

```
gcloud dns response-policies delete myresponsepolicy
```

To view the details of a response policy, run

```
gcloud dns response-policies describe myresponsepolicy
```

To see a list of all response policies, run

```
gcloud dns response-policies list
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[rules](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules)`**:
Manage your Cloud DNS response policy rules.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/create)`**:
Creates a new Cloud DNS response policy.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/delete)`**:
Deletes a Cloud DNS response policy.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/describe)`**:
Describes a Cloud DNS response policy.

**`[list](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/list)`**:
Displays the list of all Cloud DNS response policies in a given project.

**`[update](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/update)`**:
Updates a Cloud DNS response policy.

**NOTES**

: These variants are also available:

```
gcloud alpha dns response-policies
```

```
gcloud beta dns response-policies
```