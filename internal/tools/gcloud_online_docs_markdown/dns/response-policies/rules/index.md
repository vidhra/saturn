# gcloud dns response-policies rules  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules)*

**NAME**

: **gcloud dns response-policies rules - manage your Cloud DNS response policy rules**

**SYNOPSIS**

: **`gcloud dns response-policies rules` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create a new response policy rule with local data rrsets, run:

```
gcloud dns response-policies rules myresponsepolicyrule --response-policy="myresponsepolicy" --dns-name="www.zone.com." --local-data=name=www.zone.com.,type=CNAME,ttl=21600,rrdatas=zone.com.
```

To create a new response policy rule with behavior, run:

```
gcloud dns response-policies rules myresponsepolicyrule --response-policy="myresponsepolicy" --dns-name="www.zone.com." --behavior=bypassResponsePolicy
```

To update a new response policy rule with local data rrsets, run:

```
gcloud dns response-policies rules myresponsepolicyrule --response-policy="myresponsepolicy" --local-data=name=www.zone.com.,type=A,ttl=21600,rrdatas=1.2.3.4
```

To update a new response policy rule with behavior, run:

```
gcloud dns response-policies rules myresponsepolicyrule --response-policy="myresponsepolicy" --behavior=bypassResponsePolicy
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/create)`**:
Creates a new Cloud DNS response policy rule.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/delete)`**:
Deletes a Cloud DNS response policy rule.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/describe)`**:
Shows details about a Cloud DNS response policy rule.

**`[list](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/list)`**:
Displays the list of all a Cloud DNS response policy rules.

**`[update](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/update)`**:
Updates a new Cloud DNS response policy rule.

**NOTES**

: These variants are also available:

```
gcloud alpha dns response-policies rules
```

```
gcloud beta dns response-policies rules
```